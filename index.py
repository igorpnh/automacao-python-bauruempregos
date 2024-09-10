import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = uc.Chrome(headless=True)

def ChooseSearch():
    print("Onde deseja buscar suas vagas?")
    print("1 - Gupy")
    print("2 - Bauru Empregos")

    while True:
        opcao = input("Digite o número correspondente à sua escolha: ")

        if opcao == "1":
            return "gupy"
        elif opcao == "2":
            return "bauruempregos"
        else:
            print("Opção inválida. Tente novamente.")
            

def BauruEmpregosSearch():
    pagination = [200,400,600,800,1000,1200]
    result = list()

    print("Buscando dados...")

    print("Insira as palavras-chave que deseja usar para buscar vagas!")
    FLAG_1 =  input("Digite a primeira palavra-chave: ")
    FLAG_2 =  input("Digite a segunda palavra-chave: ")


    for(i) in pagination:
        driver.get(f"https://www.bauruempregos.com.br/home/vagas?offset={i}&max=200")
        vaga = driver.find_elements(By.CLASS_NAME, "descricao-vaga")
        
    
    for(i) in vaga:
        text = i.text
        if(text.__contains__(FLAG_1) or text.__contains__(FLAG_2)): 
            print(f"{len(result) + 1} Encontrados")
            children = i.find_elements(By.TAG_NAME, "a")
            href = children[0].get_attribute("href")
            result.append({
                "name":  text.capitalize(),
                "link": href
            })


    if(len(result) > 0):

        df = pd.DataFrame(result)
        df.to_excel(f"vagas-bauruempregos-{time.time()}.xlsx", index=False)

        print("Arquivo Excel gerado com sucesso!")

    else:
        print("Nenhuma vaga encontrada!")
    

    driver.quit()


def ChooseWorkType():
    print("Escolha o tipo de trabalho:")
    print("1 - Remoto")
    print("2 - Híbrido")
    print("3 - Presencial")

    while True:
        opcao = input("Digite o número correspondente à sua escolha: ")

        if opcao == "1":
            return "remote"
        elif opcao == "2":
            return "hybrid"
        elif opcao == "3":
            return "on-site"
        else:
            print("Opção inválida. Tente novamente.")


def GupySearch():
    result = list()
    FLAG_1 =  input("Digite a palavra-chave: ")
    FLAG_1_FORMATTED = FLAG_1.replace(" ", "%20")
    WORK_TYPE = ChooseWorkType()
    print("Buscando dados...")
    driver.get(f"https://portal.gupy.io/job-search/term=${FLAG_1_FORMATTED}&workplaceTypes[]={WORK_TYPE}")
    driver.implicitly_wait(15)
    a = driver.find_elements(By.CLASS_NAME, "IKqnq")
    
    
    
    for (i) in a:
        name = i.find_element(By.CLASS_NAME, "dZRYPZ")
        href = i.get_attribute("href")
        result.append({
                   "name":  name.text,
                   "link": href
               })
        
        
            
    if(len(result) > 0):

        df = pd.DataFrame(result)
        df.to_excel(f"vagas-gupy-{time.time()}.xlsx", index=False)

        print("Arquivo Excel gerado com sucesso!")

    else:
        print("Nenhuma vaga encontrada!")
    

    driver.quit()
        

        

initial_chose = ChooseSearch()

if(initial_chose == "gupy"): 
    GupySearch()
else:  
    BauruEmpregosSearch()

   