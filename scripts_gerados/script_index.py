from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Configuração do ambiente para usar o Chrome
chrome_options = Options()
chrome_service = Service('..\driver\chromedriver.exe')  # Especifique o caminho do seu chromedriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Acessar a URL da plataforma AcordeLab
driver.get('https://almsantana.github.io/')

# Cenário de teste: Login com credenciais válidas
def test_login_valido():
    # Preencher o campo de e-mail
    driver.find_element(By.ID, 'email').send_keys('email@acordelab.com.br')
    # Preencher o campo de senha
    driver.find_element(By.ID, 'senha').send_keys('123senha')
    # Clicar no botão de login
    driver.find_element(By.CLASS_NAME, 'botao-login').click()
    
    # Verificar se o redirecionamento ocorreu para a página inicial
    #assert driver.current_url == 'http://acordelab.com/home.html'  # URL esperada da página inicial

# Cenário de teste: Login com e-mail inválido
def test_login_email_invalido():
    # Preencher o campo de e-mail com um valor inválido
    driver.find_element(By.ID, 'email').send_keys('invalido@acordelab.com.br')
    # Preencher o campo de senha válida
    driver.find_element(By.ID, 'senha').send_keys('123senha')
    # Clicar no botão de login
    driver.find_element(By.CLASS_NAME, 'botao-login').click()
    
    # Verificar se uma mensagem de erro é exibida
    assert driver.find_element(By.CLASS_NAME, 'mensagem-erro').is_displayed()

# Cenário de teste: Login com senha inválida
def test_login_senha_invalida():
    # Preencher o campo de e-mail válido
    driver.find_element(By.ID, 'email').send_keys('email@acordelab.com.br')
    # Preencher o campo de senha com um valor inválido
    driver.find_element(By.ID, 'senha').send_keys('senhaerrada')
    # Clicar no botão de login
    driver.find_element(By.CLASS_NAME, 'botao-login').click()
    
    # Verificar se uma mensagem de erro é exibida
    assert driver.find_element(By.CLASS_NAME, 'mensagem-erro').is_displayed()

# Cenário de teste: Login com campos vazios
def test_login_campos_vazios():
    # Clicar no botão de login sem preencher os campos
    driver.find_element(By.CLASS_NAME, 'botao-login').click()
    
    # Verificação adicional para garantir que uma mensagem é exibida (se aplicável)

# Executar os testes
test_login_valido()
test_login_email_invalido()
test_login_senha_invalida()
test_login_campos_vazios()

# Pausa de 3 segundos antes de fechar
time.sleep(3)

# Encerrar o driver após os testes
driver.quit()