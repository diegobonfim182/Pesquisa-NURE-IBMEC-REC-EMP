#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Instalando o Selenium, que é um framework para fazer o webscraping dos dados nas páginas 


# In[2]:


pip install selenium


# In[ ]:


#Web drive manager é utilizado para manipular navegadores


# In[3]:


pip install webdriver-manager


# In[ ]:


#Importando os componentes necessários para rodar o projeto


# In[4]:


from selenium import webdriver
#A classe service é usada para iniciar uma instância do Chrome WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.relative_locator import locate_with


# In[ ]:


#O webdriver.Chrome serve para você não precisar ficar colocando versão do Chrome e em pastas específicas te dando trabalho
#Abre o drive


# In[6]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[ ]:


#Chamar o site


# In[7]:


url_site = 'https://scholar.google.com.br/scholar?as_ylo=2020&q=recupera%C3%A7%C3%A3o+judicial&hl=pt-BR&as_sdt=0,5&as_vis=1'

driver.get(url_site)


# In[8]:


palavras_chaves = input("Digite a palavra chave a ser utilizada: ")
print(f'\n  A palavra chave é: "{palavras_chaves}"')


# In[ ]:


#Aqui é onde vai ficar o loop
#De toda forma já vai pegar a palavra chave e vai procurar na nova página


# In[9]:


elemento = driver.find_element(By.PARTIAL_LINK_TEXT, palavras_chaves)
elemento
html_print = elemento.get_attribute("outerHTML")
html_print


# In[ ]:


#Abaixo foi colocado um if else com o find com a condição -1 que indica quando nada é encontrado


# In[11]:


url_pagina1 = 'https://scholar.google.com.br/scholar?start=10&q=recupera%C3%A7%C3%A3o+judicial&hl=pt-BR&as_sdt=0,5&as_ylo=2020&as_vis=1' 
lista_ids_coletados = []
resultado = html_print.find(palavras_chaves)
start = 2

while start > 1:
        url_presente = driver.current_url
        elements = driver.find_elements(By.PARTIAL_LINK_TEXT, palavras_chaves)
        print(f'Itens achados com a PALAVRA-CHAVE:  "{palavras_chaves}" \n')
        print(f'Número de itens achados no index: "{len(elements)}" \n')
        print(f'Substring achados no index:, "{resultado}" \n')
        print("------------------------------------------------")
        print(f"Artigos encontrados: \n")
        for e in elements:
            print(f'-"{e.text}" ; \n')
        print("------------------------------------------------")
        print(f'ID´s encontrados: \n')
        for e in elements:   
            coletando_id = e.get_attribute('id')
            if coletando_id == "":
                print('-Não tem ID e não serão copiadas')
            else:
               lista_ids_coletados.append(f'a[data-clk-atid="{coletando_id}"]')
               print(f"-{coletando_id} ; \n ")
        print(f'Número de id´s achados no index: "{len(lista_ids_coletados)}" \n ')
        print(f'{lista_ids_coletados} \n ')
        print("------------------------------------------------")
        print(f'Clicks realizados: \n')
       
        print(url_presente_dinamico)
        for e in lista_ids_coletados:
                 url_presente_dinamico = driver.current_url
                 driver.implicitly_wait(5)
                 if url_presente ==  url_presente_dinamico :
                    print("Status ok! \n")
                    print(e)
                    elemento4 = driver.find_element(By.CSS_SELECTOR, e)
                    elemento4.click()
                    print(f"{elemento4} \n")
                    #driver.get(url_site)
                    driver.implicitly_wait(3)
                    url_presente_dinamico = driver.current_url
                    if url_presente == url_presente_dinamico:
                        print("Status ok! Pós click \n")
                    else:
                        driver.back()
                        print("Entrou em um link e necessitou de retroceder! \n")
                 else:    
                    driver.back()
                    print("Entrou em um link e necessitou de retroceder! \n")
                    #driver.get(url_site)
                    #driver.back()

        botao_next = driver.find_element(By.CLASS_NAME, "gs_ico_nav_next")
        botao_next.click()
        print(botao_next)

        lista_ids_coletados.clear()
        print(lista_ids_coletados)


# In[ ]:


url_presente_dinamico = driver.current_url
print(url_presente_dinamico)
print(url_presente)

