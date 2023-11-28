import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar o WebDriver (no exemplo, estou usando o Chrome)
driver = webdriver.Chrome()

# Navegar para a página do seu aplicativo Django
driver.get('https://web-application-healthy.azurewebsites.net/accounts/login/')

time.sleep(1)
# Localizar o link "Create Account" usando um seletor CSS ou XPath
# Aqui estou usando um seletor CSS
create_account_link = driver.find_element(By.CSS_SELECTOR, 'p.change-form-p a[href="/accounts/register"]')

# Clicar no link "Create Account"
create_account_link.click()
time.sleep(1)
wait = WebDriverWait(driver, 10)
username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))

# Insira algum texto no campo de entrada
username_input.send_keys("daniloevirolivsssss")

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)
password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))

# Insira sua senha no campo de senha
password_input.send_keys("senha12345")

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
confirm_password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'confirm_password')))

# Insira a confirmação da senha no campo
confirm_password_input.send_keys("senha12345")

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
register_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Register"]')))

# Clique no botão de envio
register_button.click()

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)
username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))

# Insira algum texto no campo de entrada
username_input.send_keys("daniloevirolivsssss")

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)
password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))

# Insira sua senha no campo de senha
password_input.send_keys("senha12345")

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

time.sleep(2)

wait = WebDriverWait(driver, 10)
entrar_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Entrar"]')))

# Clique no botão de envio
entrar_button.click()

# Aguarde alguns segundos para visualizar o resultado (opcional)
driver.implicitly_wait(5)

time.sleep(2)

