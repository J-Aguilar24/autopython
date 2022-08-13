from selenium import webdriver #Importar webdriver
from selenium.webdriver.common.keys import Keys #Importar Keys de webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#! Ignorar estas dos lineas
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

PATH = "C:\Program Files (x86)\chromedriver.exe" #Ubicacion del driver
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://www.google.com/search?q=%22el+Salvador%22+AND+(%22fintech%22+OR+%22BCR%22+OR+%E2%80%9Cfinanza%E2%80%9D+OR+%22BANCA%22+OR+%E2%80%9Cregulacion%E2%80%9D+OR+%E2%80%9Ceconomia%E2%80%9D+OR+%E2%80%9Cexportacion%E2%80%9D+OR+%E2%80%9Ccomercio%E2%80%9D+OR+%E2%80%9Cturismo%E2%80%9D+OR+%E2%80%9Cbursatil%E2%80%9D+OR+%E2%80%9Cimportaciones%E2%80%9D+OR+%E2%80%9CHACIENDA%E2%80%9D+OR+%E2%80%9CDNM%E2%80%9D+OR+%E2%80%9Calejandro+zelaya%E2%80%9D+OR+%E2%80%9Cmaria+luisa+hayem%E2%80%9D+OR+%E2%80%9Cmexico%E2%80%9D+OR+%E2%80%9CPr%C3%A9stamo%E2%80%9D)&oq=%22el+Salvador%22+AND+(%22fintech%22+OR+%22BCR%22+OR+%E2%80%9Cfinanza%E2%80%9D+OR+%22BANCA%22+OR+%E2%80%9Cregulacion%E2%80%9D+OR+%E2%80%9Ceconomia%E2%80%9D+OR+%E2%80%9Cexportacion%E2%80%9D+OR+%E2%80%9Ccomercio%E2%80%9D+OR+%E2%80%9Cturismo%E2%80%9D+OR+%E2%80%9Cbursatil%E2%80%9D+OR+%E2%80%9Cimportaciones%E2%80%9D+OR+%E2%80%9CHACIENDA%E2%80%9D+OR+%E2%80%9CDNM%E2%80%9D+OR+%E2%80%9Calejandro+zelaya%E2%80%9D+OR+%E2%80%9Cmaria+luisa+hayem%E2%80%9D+OR+%E2%80%9Cmexico%E2%80%9D+OR+%E2%80%9CPr%C3%A9stamo%E2%80%9D)&aqs=chrome.0.69i59l2.6407j0j9&sourceid=chrome&ie=UTF-8") #Hacia adonde irá el driver


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Noticias"))
    )
    element.click()

    #! Para darle click a herramientas
    id_boton_herramientas ="hdtb-tls"
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id_boton_herramientas))
    )
    element.click()

    #! Que le de a ultimas 24 horas

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div[4]/div/div[2]/div/span[2]/g-popup/div[1]/div/div/span"))
    )
    driver.execute_script("arguments[0].click();", element)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div[6]/div/g-menu/g-menu-item[3]/div"))
    )
    driver.execute_script("arguments[0].click();", element)
    element.click()
    
    noticias_xpath = '//*[@id="rso"]'
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, noticias_xpath))
        
    )
    print(element)

    print("LISTO!")

except:
    print("ERROR")
    driver.quit()
