import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from utils import funcoes_texto  # Cria a interface do usuário
from utils import funcoes_chatbot
from streamlit_chat import message

def main():
    st.set_page_config(page_title="ChatbotPDF",page_icon=":books:")
 
    if "session_id" not in st.session_state:
        st.session_state.session_id = "sessao_aula_1" 
    
    if"chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for mensagem in st.session_state.chat_history:
        message(mensagem["text"], is_user=mensagem["is_user"])

    pergunta_usuario = st.chat_input("Qual é sua dúvida?")

    if pergunta_usuario:
        st.session_state.chat_history.append({"text":pergunta_usuario,"is_user":True})
        message(pergunta_usuario,is_user=True) 

        if "vectorstore" in st.session_state:
            fluxo_chatbot = funcoes_chatbot.criar_chatbot_chain(st.session_state.vectorstore)

            resposta = fluxo_chatbot.invoke(
                {"input":pergunta_usuario},
                config={"configurable":{"session_id":st.session_state.session_id}}
            )

            st.session_state.chat_history.append({"text":resposta,"is_user":False})
            message(resposta,is_user=False)

        else:
            st.warning("Por favor,processe os PDFs na barra lateral primeiro!")

    # Criar barra lateral   esquerda da aplicação
    with st.sidebar:
        st.subheader("Seus Arquivos")
        pdf_docs=st.file_uploader("Carregar arquivos PDF",type="pdf",label_visibility="visible",accept_multiple_files=True)

        print(pdf_docs)

        if st.button('Processar'):
            pass
            texto_completo = funcoes_texto.ler_pdf(pdf_docs)      
            #print(texto_completo)  

            chunks = funcoes_texto.criar_texto_chunks(texto_completo)
            #print(chunks)
            
            vectorstore = funcoes_chatbot.criar_vectorstore(chunks)
            #print(vectorstore)

            st.session_state.vectorstore = vectorstore

        else:
            st.warning("Por favor, selecione ao menos um arquivo de PDF antes de processar.")


if __name__ == "__main__": 
    main()


