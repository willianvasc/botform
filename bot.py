import pandas as pd;

from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;    
import time
arquivo = "pessoas.xlsx"

df = pd.read_excel(arquivo)

for index,row in df.iterrows():

    chrome = webdriver.Chrome(executable_path="chromedriver.exe")
    chrome.get("https://ampl.me/fOJqewOjz")
    inputNome = chrome.find_element(By.ID, "form-field-name")
    inputEmail = chrome.find_element(By.ID, "form-field-Email")
    inputTelefone = chrome.find_element(By.ID, "form-field-telefone")
    submit=chrome.find_element(By.XPATH, '//*[@id="carnaprime"]/div/div[4]/button')
    #envia os dados para os inputs
    inputNome.send_keys(row['nome'])
    inputEmail.send_keys(row['email'])
    inputTelefone.send_keys(row['telefone_fixo'])
    submit.click()
    time.sleep(7)
    chrome.quit()
