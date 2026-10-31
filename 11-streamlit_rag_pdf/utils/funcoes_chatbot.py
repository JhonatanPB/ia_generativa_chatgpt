import os
from operator import itemgetter
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory


def criar_vectorstore(chunks):
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )

    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore


# Dicionário global para armazenar o histórico das sessões
historico_sessoes = {}

def recuperar_historico_sessoes(session_id: str) -> BaseChatMessageHistory:
    if session_id not in historico_sessoes:
        historico_sessoes[session_id] = ChatMessageHistory()
    return historico_sessoes[session_id]


def criar_chatbot_chain(vectorstore):
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME")),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        temperature=0.0
    )

    retriever = vectorstore.as_retriever()

    def formatar_vetor_texto(trecho_recuperado):
        return "\n\n".join(trecho.page_content for trecho in trecho_recuperado)
    
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """Você é um assistente de inteligência artificial especializado em responder dúvidas com base em documentos internos.

DIRETRIZES:
1. **Fonte da Verdade:** Responda à pergunta do usuário usando **apenas** o Contexto fornecido abaixo.
2. **Ausência de Informação:** Se a resposta não estiver clara ou presente no contexto, responda exatamente: "Desculpe, não encontrei informações sobre isso nos documentos fornecidos."
3. **Proibido Alucinar:** Não use conhecimentos prévios ou externos para responder. Atenha-se estritamente ao texto recuperado.
4. **Tom e Estilo:** Seja claro, objetivo, cordial e utilize formatação em Markdown (tópicos e negrito) para facilitar a leitura.

---
**CONTEXTO DOS DOCUMENTOS:**
{base_conhecimento}
---"""
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])

    cadeia_resposta = (
        RunnablePassthrough.assign(
            base_conhecimento=itemgetter("input") | retriever | formatar_vetor_texto
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    chatbot_com_memoria = RunnableWithMessageHistory(
        cadeia_resposta,
        recuperar_historico_sessoes,
        input_messages_key="input",
        history_messages_key="chat_history"
    )

    return chatbot_com_memoria