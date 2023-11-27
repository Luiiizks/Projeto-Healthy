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

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)
botao_criar_refeicao = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='descriptionButton' and text()='Criar Nova Refeição']"))
)

# Clicar no botão
botao_criar_refeicao.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(2)

campo_titulo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'id_titulo'))
)

# Preencher o campo com um valor (por exemplo, 'Título da Dieta')
campo_titulo.send_keys('Dieta Otima')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

campo_notas = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'notas'))
)

# Preencher o campo de texto com um valor (por exemplo, 'Notas da Dieta')
campo_notas.send_keys('Quero comer cuscuz de manha, com ovo cozido. No almoço, terei arroz integral com frango, pois assim, consumirei menos calorias.')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

campo_calorias = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'id_calorias'))
)

# Preencher o campo com um valor numérico (por exemplo, 500)
campo_calorias.send_keys('1500')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)
botao_salvar_dieta = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @class='buttonNew' and @value='Salvar Dieta']"))
)

# Clicar no botão
botao_salvar_dieta.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)


time.sleep(2)

link_visualizar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='editButton' and contains(text(), 'Visualizar')]"))
)

# Clicar no link
link_visualizar.click()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)
campo_titulo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'titulo'))
)

# Limpar o campo
campo_titulo.clear()
time.sleep(2)

# Preencher o campo com um novo valor (por exemplo, 'Dieta Maravilhosa')
campo_titulo.send_keys('dietas sssss')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(2)
campo_notas = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'notas'))
)

# Limpar o texto existente
campo_notas.clear()
time.sleep(2)

# Preencher o campo com um novo valor (por exemplo, 'Quero comer cachorro quente')
campo_notas.send_keys('Quero comer cachorro quente')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

campo_calorias = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'calorias'))
)

# Limpar o valor existente
campo_calorias.clear()
time.sleep(2)
# Preencher o campo com um novo valor (por exemplo, '2000')
campo_calorias.send_keys('2000')

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

botao_salvar_alteracoes = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @class='buttonNew' and @value='Salvar Alterações']"))
)

# Clicar no botão
botao_salvar_alteracoes.click()

# Aguardar alguns segundos para visualização (opcional)
link_excluir = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='excButton' and contains(text(), 'Excluir')]"))
)

# Clicar no link "Excluir"
link_excluir.click()

# Aguardar o alerta e aceitá-lo
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

# Aguardar alguns segundos para visualização (opcional)
driver.implicitly_wait(5)

time.sleep(10)





