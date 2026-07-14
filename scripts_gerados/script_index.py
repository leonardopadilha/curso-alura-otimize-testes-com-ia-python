```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurações do Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Executa o Chrome em modo headless (opcional)
service = Service('caminho/para/chromedriver')  # Colocar o caminho para o seu chromedriver executável

# Lista de casos de teste
test_cases = [
    {
        "name": "Test Login Valido",
        "description": "Teste de login com credenciais válidas.",
        "input": {
            "email": "email@acordelab.com.br",
            "senha": "123senha"
        },
        "expectedOutcome": {
            "redirect": "home.html",
            "status": "Aprovado"
        }
    },
    {
        "name": "Test Login Invalido Senha Errada",
        "description": "Teste de login com senha errada.",
        "input": {
            "email": "email@acordelab.com.br",
            "senha": "senhaerrada"
        },
        "expectedOutcome": {
            "errorMessage": "E-mail ou senha incorretos. Tente novamente.",
            "pageStay": "login.html",
            "status": "Reprovado"
        }
    },
    {
        "name": "Test Login Invalido Email Errado",
        "description": "Teste de login com email errado.",
        "input": {
            "email": "wrongemail@acordelab.com.br",
            "senha": "123senha"
        },
        "expectedOutcome": {
            "errorMessage": "E-mail ou senha incorretos. Tente novamente.",
            "pageStay": "login.html",
            "status": "Reprovado"
        }
    },
    {
        "name": "Test Login Invalido Campos Vazios",
        "description": "Teste de login com campos vazios.",
        "input": {
            "email": "",
            "senha": ""
        },
        "expectedOutcome": {
            "errorMessage": "E-mail ou senha não podem estar vazios.",
            "pageStay": "login.html",
            "status": "Reprovado"
        }
    }
]

# Função para testar cada caso
def run_test_case(test_case):
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://path.to.acordelab/index.html")  # URL da aplicação

    # Encontra os campos de email e senha
    email_input = driver.find_element(By.ID, "email")
    senha_input = driver.find_element(By.ID, "senha")
    botao_login = driver.find_element(By.CLASS_NAME, "botao-login")
    
    # Insere os dados de entrada
    email_input.send_keys(test_case["input"]["email"])
    senha_input.send_keys(test_case["input"]["senha"])
    botao_login.click()
    
    time.sleep(2)  # Espera a resposta do servidor

    if test_case[" expectedOutcome"]["status"] == "Aprovado":
        # Verificação para redirecionamento
        assert "home.html" in driver.current_url, f"Teste {test_case['name']} falhou: O usuário não foi redirecionado corretamente."
    else:
        # Verificação de mensagem de erro
        mensagem_erro = driver.find_element(By.CLASS_NAME, "mensagem-erro")  # Ajustar de acordo com a classe correta de erro
        assert mensagem_erro.is_displayed(), f"Teste {test_case['name']} falhou: Mensagem de erro não exibida."

    driver.quit()

# Execução dos casos de teste
for test_case in test_cases:
    run_test_case(test_case)

time.sleep(3)  # Pausa antes de fechar o script
```