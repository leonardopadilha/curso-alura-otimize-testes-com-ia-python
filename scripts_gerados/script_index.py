```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Configurações do ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless
service = Service('caminho/para/chromedriver')  # Substitua pelo caminho do seu ChromeDriver

# Casos de teste
test_cases = [
    {
        "case_id": 1,
        "description": "Login bem-sucedido de Ana",
        "user": {
            "email": "email@acordelab.com.br",
            "senha": "123senha"
        },
        "expected_result": {
            "redirected_to": "home.html",
            "error_message_visible": False
        },
        "status": "Aprovado"
    },
    {
        "case_id": 2,
        "description": "Login com senha incorreta",
        "user": {
            "email": "email@acordelab.com.br",
            "senha": "senhaErrada"
        },
        "expected_result": {
            "redirected_to": "index.html",
            "error_message_visible": True
        },
        "status": "Rejeitado"
    },
    {
        "case_id": 3,
        "description": "Login com email incorreto",
        "user": {
            "email": "emailErrado@acordelab.com.br",
            "senha": "123senha"
        },
        "expected_result": {
            "redirected_to": "index.html",
            "error_message_visible": True
        },
        "status": "Rejeitado"
    },
    {
        "case_id": 4,
        "description": "Login com campos em branco",
        "user": {
            "email": "",
            "senha": ""
        },
        "expected_result": {
            "redirected_to": "index.html",
            "error_message_visible": True
        },
        "status": "Rejeitado"
    }
]

# Inicializa o driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Itera pelos casos de teste
for test_case in test_cases:
    # Acessa a página de login
    driver.get('caminho/para/index.html')  # Substitua pelo caminho do arquivo index.html
    
    # Preenche o formulário com os dados do usuário
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "senha")
    login_button = driver.find_element(By.CSS_SELECTOR, ".botao-login")
    
    # Preenche email e senha
    email_field.send_keys(test_case["user"]["email"])
    password_field.send_keys(test_case["user"]["senha"])
    
    # Clica no botão de login
    login_button.click()
    
    # Aguarda alguns segundos para a página carregar
    time.sleep(2)
    
    # Verifica o resultado
    current_url = driver.current_url
    error_message_visible = False
    
    # Verifica se a mensagem de erro está visível
    try:
        driver.find_element(By.CSS_SELECTOR, ".error-message")  # Substitua pelo seletor correto
        error_message_visible = True
    except:
        error_message_visible = False
    
    # Determina se o teste foi Aprovado ou Rejeitado
    if (current_url.endswith(test_case["expected_result"]["redirected_to"]) and
        error_message_visible == test_case["expected_result"]["error_message_visible"]):
        result = "Aprovado"
    else:
        result = "Rejeitado"

    # Exibe o resultado do teste
    print(f'Caso de Teste {test_case["case_id"]}: {test_case["description"]} - Resultado: {result}')

# Pausa de 3 segundos antes de fechar o script
time.sleep(3)
driver.quit()
```