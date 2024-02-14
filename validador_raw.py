# Neste arquivo, ajuda a enteder a parte de validação de entrada e saida das requisições da API

from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.98,
        "elemento2": "olaMundo",
        "elemento3": "123",
    }
}

body_validador = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "required": True },
            "elemento2": { "type": "string", "required": True },
            "elemento3": { "type": "string" }  # Não é necessário "required" e "empty" para strings
        }
    }
})

response = body_validador.validate(body)
print(response)
