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

# Encontrar o link <a> com a classe 'dropdown-item' e o atributo 'href'
water_goal_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="dropdown-item" and @href="/goals/water_goal"]')))

# Clique no link para ir para a página de definir meta de água
water_goal_link.click()

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

# Encontrar o campo de entrada <input> com a classe 'input', tipo 'float', name 'liters' e id 'liters'
liters_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="input" and @type="float" and @name="liters" and @id="liters"]')))

# Limpar qualquer valor existente no campo (opcional)
liters_input.clear()

# Preencher o campo com um valor
liters_input.send_keys("3")  # Substitua "2.5" pelo valor desejado

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

# Encontrar o botão <input> do tipo 'submit' com a classe 'salvar' e o valor 'Salvar'
salvar_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="salvar" and @type="submit" and @value="Salvar"]')))

# Clique no botão 'Salvar'
salvar_button.click()

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

time.sleep(2)

wait = WebDriverWait(driver, 10)

# Encontrar o link <a> com a classe 'dropdown-item' e o atributo 'href'
weight_goal_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="dropdown-item" and @href="/goals/weight_goal"]')))

# Clique no link para ir para a página de definir meta de peso
weight_goal_link.click()

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)


