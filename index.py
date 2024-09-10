import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = uc.Chrome(headless=True)

pagination = [200,400,600,800,1000,1200]

print("Insira as palavras-chave que deseja usar para buscar vagas!")
FLAG_1 = input("Digite a primeira palavra-chave: ")
FLAG_2 = input("Digite a segunda palavra-chave: ")

result = list()

print("Processing...")

for(i) in pagination:
    driver.get(f"https://www.bauruempregos.com.br/home/vagas?offset={i}&max=200")
    vaga = driver.find_elements(By.CLASS_NAME, "descricao-vaga")
        
    
    for(i) in vaga:
        text = i.text.lower()
        if(text.__contains__(FLAG_1.lower()) or text.__contains__(FLAG_2.lower())): 
            print(f"{len(result) + 1} Encontrados")
            children = i.find_elements(By.TAG_NAME, "a")
            href = children[0].get_attribute("href")
            result.append({
                "name":  text.capitalize(),
                "link": href
            })


if(len(result) > 0):

    df = pd.DataFrame(result)
    df.to_excel("vagas_encontradas.xlsx", index=False)

    print("Arquivo Excel gerado com sucesso!")

else:
    print("Nenhuma vaga encontrada!")
    

driver.quit()
