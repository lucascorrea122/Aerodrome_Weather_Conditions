import requests
import time 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

ioc = input("informe o código ICAO que deseja buscar informações: ")
url = url = f"https://www.aisweb.aer.mil.br/?i=aerodromos&codigo={ioc}"
print("Aguarde, informações sendo coletadas!")

option = Options()
option.headless = True

driver = webdriver.Firefox(options=option)
driver.get(url)
carts_elements = list()

try:
    element = driver.find_elements_by_class_name('list')
    size_element = len(element)
    start = 0

    for c in range(start, size_element):
        element = driver.find_elements_by_class_name('list')[start].find_elements_by_tag_name('li')
        amount_element = len(element)
        start_elementos = 0
        if(amount_element > 1):
            for d in range (start_elementos, amount_element ):
                elementary = driver.find_elements_by_class_name('list')[start].find_elements_by_tag_name('li')[start_elementos].text
                carts_elements.append(elementary)
                start_elementos = start_elementos + 1
        else:
            elementary = driver.find_elements_by_class_name('list')[start].find_elements_by_tag_name('li')[0].text       
            carts_elements.append(elementary)
        start = start + 1

    sunrise = driver.find_element_by_tag_name('sunrise').text
    sunset = driver.find_element_by_tag_name('sunset').text

    print("")
    print(f'Nascer do Sol: {sunrise} horas')
    print(f'Por do Sol: {sunset} horas')
    print("")

    carts = len(carts_elements)
    print (f'Total de {carts} cartas: ')
    aux = 0
    for z in range(aux, carts):
        print(carts_elements[aux])
        aux += 1

    print("")
    metar =  driver.find_element_by_css_selector("h5[class='mb-0 heading-primary'] + p").text
    if(metar == ""):
        print ('METAR indisponível')
    else:
        print (f'METAR: {metar}')    
    taf = driver.find_element_by_css_selector("h5[class='mb-0 heading-primary'] + p + h5 + p").text
    if(taf == ""):
        print ('TAF indiponível')
    else:
        print(f'TAF: {taf}')    
except:
     print('Você digitou um código ICAO inválido!')
driver.quit()