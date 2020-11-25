#importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
#navegar até o wpp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#definir contatos, grupos e mensagen a ser enviada
contatos = 'Wserver'

#buscar contatos/grupos
#enviar mensagens para o contato/grupo