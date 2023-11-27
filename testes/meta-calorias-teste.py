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

navbar_toggler_icon.click()
time.sleep(2)
botao_dieta = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(),'Dieta')]"))
)

# Clicar no botão
botao_dieta.click()

botao_planejar_dieta = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='dropdown-item' and text()='Planejar Dieta']"))
)

# Clicar no botão
botao_planejar_dieta.click()
time.sleep(2)


# Localizar o link pelo texto "Definir Meta de Calorias"
link_definir_meta_calorias = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='descriptionButton' and contains(text(), 'Definir Meta de Calorias')]"))
)

# Clicar no link "Definir Meta de Calorias"
link_definir_meta_calorias.click()
time.sleep(2)
# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

campo_calorias_meta = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'calorias_meta'))
)
time.sleep(2)
# Preencher o campo com um valor de meta de calorias (por exemplo, '2000')
campo_calorias_meta.send_keys('2000')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

botao_salvar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @class='salvar' and @value='Salvar']"))
)
time.sleep(2)
# Clicar no botão "Salvar"
botao_salvar.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(4)

link_definir_meta_calorias = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='descriptionButton' and contains(text(), 'Definir Meta de Calorias')]"))
)

# Clicar no link "Definir Meta de Calorias"
link_definir_meta_calorias.click()
time.sleep(2)
# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

campo_calorias_meta = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'calorias_meta'))
)
time.sleep(2)
# Preencher o campo com um valor de meta de calorias (por exemplo, '2000')
campo_calorias_meta.send_keys('1500')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

botao_salvar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @class='salvar' and @value='Salvar']"))
)
time.sleep(2)
# Clicar no botão "Salvar"
botao_salvar.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(4)