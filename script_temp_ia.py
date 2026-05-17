from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Configurando o caminho do driver do Chromium
chrome_driver_path = "driver/chromedriver.exe"

# Configurando as opções do navegador
chrome_options = Options()
chrome_options.headless = False

# Inicializando o serviço do driver
service = Service(chrome_driver_path)

# Inicializando o navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Abrir o navegador e acessar a URL da plataforma AcordeLab
    driver.get("https://almsantana.github.io/")
    time.sleep(3)

    # Verificar se a página inicial foi carregada corretamente
    assert "AcordeLab" in driver.title

    # Preencher o campo de e-mail
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("email@acordelab.com.br")

    # Preencher o campo de senha
    password_input = driver.find_element(By.ID, "senha")
    password_input.send_keys("123senha")

    # Clicar no botão "Entrar"
    enter_button = driver.find_element(By.CLASS_NAME, "botao-login")
    enter_button.click()

    # Dando uma pausa de 3 segundos antes de fechar o script
    time.sleep(3)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechar o navegador
    driver.quit()