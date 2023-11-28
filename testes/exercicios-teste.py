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

time.sleep(2)


# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

elemento_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "treinoDropdown"))
)

# Clicar no elemento dropdown
elemento_dropdown.click()
elemento_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//a[@class="dropdown-item" and contains(text(), "Planejar Treino")]'))
)

time.sleep(2)
# Clicar no link
elemento_link.click()
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "addTreino")) or
    EC.presence_of_element_located((By.CLASS_NAME, "width-area"))
)

time.sleep(2)
# Clicar no link "Adicionar Treino"
elemento_link_adicionar_treino = driver.find_element(By.CLASS_NAME, "addTreino")
elemento_link_adicionar_treino.click()

time.sleep(2)
# Esperar até que o textarea esteja presente
elemento_textarea = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "width-area"))
)

time.sleep(2)
# Preencher o textarea
texto_para_inserir = "supino 20kg"
elemento_textarea.send_keys(texto_para_inserir)

# Clicar no botão "Salvar"
elemento_botao_salvar = driver.find_element(By.CLASS_NAME, "saveButton")
elemento_botao_salvar.click()

elemento_link_editar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "edit"))
)

# Clicar no link "Editar"
elemento_link_editar.click()

time.sleep(2)
# Preencher o <textarea> com novo texto
elemento_textarea = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "width-area"))
)
elemento_textarea.clear()  # Limpar o conteúdo existente, se houver

time.sleep(2)
novo_texto = "Braço 23"
elemento_textarea.send_keys(novo_texto)

# Clicar no botão "Salvar"
elemento_botao_salvar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "saveButton"))
)
elemento_botao_salvar.click()

time.sleep(2)


elemento_link_excluir = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "delete"))
)

# Clicar no link "Excluir"
elemento_link_excluir.click()

time.sleep(2)
elemento_botao_excluir = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "saveButton"))
)

# Clicar no botão "Sim, Excluir"
elemento_botao_excluir.click()

time.sleep(2)
