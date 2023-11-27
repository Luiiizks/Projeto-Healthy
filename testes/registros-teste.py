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

registros_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link dropdown-toggle' and @id='exerciciosDropdown' and contains(text(), 'Registros')]"))
)

# Clicar no link "Registros"
registros_link.click()

time.sleep(2)

registros_diarios_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and @href='/registro/listar_registros/']"))
)

# Clicar no link "Registros Diarios"
registros_diarios_link.click()
time.sleep(2)
criar_novo_registro_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='descriptionButton' and @href='/registro/criar_registro/']"))
)

# Clicar no link "Criar Novo Registro"
criar_novo_registro_link.click()
time.sleep(2)
campo_data = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'id_data'))
)
driver.implicitly_wait(5)
# Preencher o campo de data com uma data específica (por exemplo, '2023-11-27')
campo_data.send_keys('21092023')
time.sleep(2)
# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)
campo_texto_area = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'id_nota'))
)

# Preencher o campo de texto em área com o texto desejado
texto_desejado = "hoje eu fui pra academia duas vezes e to bem feliz com meus resultados!"
campo_texto_area.send_keys(texto_desejado)

driver.implicitly_wait(5)
time.sleep(2)

botao_salvar_registro = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @class='buttonNew' and @value='Salvar Registro']"))
)

# Clicar no botão "Salvar Registro"
botao_salvar_registro.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)
time.sleep(2)

link_visualizar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='editButton' and contains(@href, '/registro/editar_registro/2/')]"))
)

# Clicar no link "Visualizar"
link_visualizar.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(2)
campo_data = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'data'))
)

# Limpar o valor atual do campo de data
driver.execute_script("arguments[0].value = '';", campo_data)

# Preencher o campo de data com um novo valor (por exemplo, '2023-11-09')
novo_valor_data = '11092023'
campo_data.send_keys(novo_valor_data)

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(2)

campo_texto_area = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'nota'))
)

# Limpar o conteúdo atual do campo de texto em área
campo_texto_area.clear()

# Preencher o campo de texto em área com um novo texto
novo_texto = "oiiii"
campo_texto_area.send_keys(novo_texto)

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

botao_salvar_alteracoes = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @class='buttonNew' and @value='Salvar Alterações']"))
)

# Clicar no botão "Salvar Alterações"
botao_salvar_alteracoes.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)
time.sleep(2)
link_excluir = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='excButton' and contains(@href, '/registro/excluir_registro/3/')]"))
)

# Clicar no link "Excluir"
link_excluir.click()

# Aguardar o pop-up de confirmação
time.sleep(1)  # Espera curta para garantir que o pop-up tenha carregado

# Aceitar o pop-up clicando em "OK"
driver.switch_to.alert.accept()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(1) 