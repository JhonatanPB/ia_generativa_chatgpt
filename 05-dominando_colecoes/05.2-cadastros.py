
cadastros = [
    {
       "id":1042,
        "perfil":{
            "nome":"beatriz Souza",
            "email":"beatriz@gmail.com"
    }
    },
    {
         "id":1043,
         "perfil":{
             "nome":"beatriz Souza",
             "email":"beatriz@gmail.com"
        }
    }
]
for item in cadastros:
    id_formulario = item.get("id")
    perfil_extraido = item.get("perfil")
    nome_usuario = perfil_extraido.get("nome")
    telefone_usuario = perfil_extraido.get("telefone")

    print(f"ID: {id_formulario:} | Usuário: {nome_usuario} | Telefone: {telefone_usuario}")