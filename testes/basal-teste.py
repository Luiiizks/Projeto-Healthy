import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # Adicione esta linha

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

# Encontrar o link <a> com a classe 'dropdown-item' e o atributo 'href'
calcular_metabolismo_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="dropdown-item" and @href="/calculos/metabolismo/"]')))

# Clique no link para calcular o metabolismo basal
calcular_metabolismo_link.click()

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

# Encontrar o elemento <select> com o name 'genero' e o id 'genero'
genero_select = wait.until(EC.visibility_of_element_located((By.XPATH, '//select[@name="genero" and @id="genero"]')))

# Criar um objeto Select para interagir com o elemento <select>
select = Select(genero_select)
time.sleep(2)
# Selecionar a opção desejada por valor
select.select_by_value('M')  # Isso selecionará a opção 'Mulher'

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

# Encontrar o campo de entrada <input> com o type 'number', name 'idade' e id 'idade'
idade_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="number" and @name="idade" and @id="idade"]')))

# Limpar qualquer valor existente no campo (opcional)
idade_input.clear()
time.sleep(2)
# Preencher o campo com um valor
idade_input.send_keys("25")  # Substitua "25" pelo valor desejado


# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

# Encontrar o campo de entrada <input> com o type 'number', name 'altura', id 'altura' e step '0.01'
altura_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="number" and @name="altura" and @id="altura" and @step="0.01"]')))

# Limpar qualquer valor existente no campo (opcional)
altura_input.clear()
time.sleep(2)
# Preencher o campo com um valor
altura_input.send_keys("1.75")  # Substitua "1.75" pelo valor desejado

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)

# Encontrar o campo de entrada <input> com o type 'number', name 'peso', id 'peso' e step '0.01'
peso_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="number" and @name="peso" and @id="peso" and @step="0.01"]')))

# Limpar qualquer valor existente no campo (opcional)
peso_input.clear()
time.sleep(2)
# Preencher o campo com um valor
peso_input.send_keys("70.5")  # Substitua "70.5" pelo valor desejado
time.sleep(2)
# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

# Encontrar o botão <button> com a classe 'saveButton' e o tipo 'submit'
calcular_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="saveButton" and @type="submit"]')))

# Clique no botão 'Calcular'
calcular_button.click()

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

time.sleep(2)
