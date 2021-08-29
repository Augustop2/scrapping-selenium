# web scrapping com selenium


#aqui o programa abre o google crhome
import time
from selenium import webdriver
from time import sleep
chrome_path = r"C:\webdrivers\chromedriver.exe"
navegador =  webdriver.Chrome(chrome_path)
#aqui o programa navega ate o site de RI da magazine  luiza
navegador.get('https://ri.magazineluiza.com.br/')
#aqui ele espera 2 segundos para começar a procurar o elemento
time.sleep(2)
#aqui ele busca o elemento pelo xpath e clica 
navegador.find_element_by_xpath('/html/body/form/div[11]/div/div/div[1]/div/div[4]/div/a/img').click()
time.sleep(2)
#aqui ele encontra o elemento(no caso uma planilha )pelo xpath e clica para fazer o download
#PS: SEMPRE LEMBRA DE COLOCAR O XPATH EM ASPAS SIMPLES.
navegador.find_element_by_xpath('//*[@id="bWtQ7n6RcQdDDDCgCcH3yg=="]').click()



