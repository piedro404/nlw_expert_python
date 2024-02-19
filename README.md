# NLW Expert (Python) 🚀
Este repositório foi desenvolvido durante a trilha Python do evento NLW Expert da Rocketseat. O projeto é focado na criação de códigos de barras e está alinhado com conceitos de arquitetura de projeto.

# Principais Tecnologias Utilizadas 🌐
- Flask: Framework web utilizado para construir a API.
- Python: Linguagem de programação principal.
- Barcode: Utilizamos bibliotecas específicas para a geração de códigos de barras.
- Outras Bibliotecas: O resto das bibliotecas pode ser encontradas no requirements.txt

# Documentação 📖
- /create_tag [POST]: Gera um Barcode apartir da biblioteca
  
    ```bash
    {
      "product_code": "123-456-789"
    }
   ```
    
  - Respostas:
    - 200 OK
    ```bash
    {
      "data": {
        "count": 1,
        "path": "123-456-789.png",
        "type": "Tag Image"
      }
    }
    ```

    - 422 UNPROCESSABLE ENTITY
    ```bash
    {
    "errors": [
    {
      "detail": {
        "produc_code": [
          "unknown field"
        ],
        "product_code": [
          "required field"
        ]
      },
      "title": "UnprocessableEntity"
        }
      ]
    }
    ```
  
# Como Executar o Projeto 🛠️
1. Clone este repositório:
   
   ```bash
   git clone https://github.com/seu-usuario/nlw_expert_python.git
   ```
   
2. Instale as dependências: 

   ```bash
   pip install -r requirements.txt
   ```
   
3. Execute o servidor localmente: 

   ```bash
   python run.py
   ```
   
4. Acesse a API em [http://127.0.0.1:3000](http://127.0.0.1:3000).

# Sobre
Obrigado a todos, desejo ótimos estudos, caso queira, entre em contato em pedro.henrique.martins404@gmail.com
