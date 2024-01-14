#Passo a passo do projeto
#1-Login https://dlp.hashtagtreinamentos.com/python/intensivao/login
#2- Importar base de dados 
#3- Cadastrar produto
#4- Cadastrar Repetir até acabar base
# instalar libbs pyautogui

import pyautogui
import time
    
#clicar >pyautogui.click
#escrever >pyautogui.write
#apertar uma tecla >pyautogui.press
#clicar >pyautogui.click
#atalho >pyautogui.hotkey
#scroll>pyautogui.scroll(500) +/-
pyautogui.PAUSE = 1

#apertar tecla Win (command+ barra de espaço)
pyautogui.press("win") 
#digitar o nome do programa (chrome)
pyautogui.write("chrome")
#apertar enter
pyautogui.press("enter")
#digitar link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
#apertar enter
pyautogui.press("enter")
#esperar 5 segundos 
time.sleep(5)

#Passo 2 -Fazer login usuário
pyautogui.click(x=456, y=394)

#acessar milenepergon@gmail.com 123456com email
pyautogui.write("milenepergon@gmail.com")

#Fazer login usuário
#pyautogui.click(x=430, y=495)
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=667, y=568)
time.sleep(2)

#3- Cadastrar produto
#importar base de dados
import pandas as pd
tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    #cadastrar o primeiro produto 
    pyautogui.click(x=391, y=300)
    #codigo
    #pyautogui.write("MOLO000251")
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha,"marca"])
    #pyautogui.write("Logitech")
    pyautogui.press("tab")
    #tipo
    #pyautogui.write("Mouse")
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")
    #categoria
    #pyautogui.write(str(1)) 
    #colocar no formato str
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    #preco
    #pyautogui.write(str(25.95))
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    #custo
    #pyautogui.write(str(6.5))
    pyautogui.write(str(tabela.loc[linha,"custo"]))  
    pyautogui.press("tab")
    #obs
    #pyautogui.press("")
    #pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write("obs")
    pyautogui.press("tab")
    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

#Repetir isso com todos os dados
#cadastrar item para cada linha da tabela
#estrutura do for no ptython
