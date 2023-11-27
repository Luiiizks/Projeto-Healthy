import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar o WebDriver (no exemplo, estou usando o Chrome)
driver = webdriver.Chrome()

# Navegar para a página do seu aplicativo Django
driver.get('https://web-application-healthy.azurewebsites.net/accounts/login/')

# Definir o tempo de espera
wait = WebDriverWait(driver, 10)

# Encontrar e preencher o campo de usuário
username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
username_input.send_keys("daniloevirolivss")

# Aguardar alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

# Encontrar e preencher o campo de senha
password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
password_input.send_keys("senha12345")

# Aguardar alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

time.sleep(2)

# Encontrar e clicar no botão de entrar
entrar_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Entrar"]')))
entrar_button.click()

# Aguardar alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
time.sleep(2)
# Fechar o navegador
wait = WebDriverWait(driver, 10)

# Encontrar o elemento <span> com a classe 'navbar-toggler-icon'
navbar_toggler_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'navbar-toggler-icon')))

# Clique no elemento <span>
navbar_toggler_icon.click()

wait = WebDriverWait(driver, 10)

# Encontrar o elemento <a> com a classe 'nav-link', o ID 'exerciciosDropdown' e o atributo 'data-bs-toggle'
exercicios_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="exerciciosDropdown" and @data-bs-toggle="dropdown"]')))

# Clique no elemento <a> para abrir o dropdown
exercicios_dropdown.click()

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

link_definir_meta = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='dropdown-item' and contains(text(), 'Definir meta de percentual de gordura')]"))
)

# Clicar no link
link_definir_meta.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(2)

campo_percentual_gordura = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'percentage'))
)
time.sleep(2)
# Preencher o campo com um valor de percentual de gordura (por exemplo, '20.5')
campo_percentual_gordura.send_keys('20.5')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)
time.sleep(2)

botao_salvar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @class='salvar' and @value='Salvar']"))
)

# Clicar no botão "Salvar"
botao_salvar.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(2)

campo_percentual_gordura = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'percentage'))
)
time.sleep(2)
# Preencher o campo com um valor de percentual de gordura (por exemplo, '20.5')
campo_percentual_gordura.send_keys('15.5')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)
time.sleep(2)

botao_salvar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @class='salvar' and @value='Salvar']"))
)

# Clicar no botão "Salvar"
botao_salvar.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)