funcionarios = {
    101: {
        "nome": "Carlos",
        "cargo": "desenvolvedor",
        "habilidades": ["python","C##","Java"]   
    },
    102: {
       "nome": "lucas",
       "cargo": "gerente de projetos",
       "habilidades": ["Scrum","Gestão"]  
    }
}

print(funcionarios[101]["cargo"])
print(funcionarios.get(103,{}).get("nome","Funcionario não é"))