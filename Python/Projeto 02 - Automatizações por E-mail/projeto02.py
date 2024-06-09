import pyautogui
import pyperclip
import webbrowser
import time
import yfinance as yf

#Obtendo as informações da ação

ticker = input("Digite o código da ação desejada: ")
dados = yf.Ticker(ticker)

data_inicial = input("Digite a data inicial ('aaaa-mm-dd'): ")
data_final = input("Digite a data final ('aaaa-mm-dd'): ")

tabela = dados.history(start=data_inicial, end=data_final)
fechamento = tabela.Close

#Análises

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

print(maxima)
print(minima)
print(valor_medio)

#Ajustando as informações para o email

destinatario = "marioluka88@gmail.com"
assunto = "Análise da Ação"
mensagem = f"""
Prezado gestor, 

Seguem as análises da ação ${ticker}:

Valor máximo: ${maxima}
Valor mínimo: ${minima}
Valor médio: ${valor_medio}

Att.
Mário Luka
"""

#Abrindo o gmail
webbrowser.open("gmail.com")
time.sleep(3)

#Clicando no botão escrever
pyautogui.PAUSE = 2
pyautogui.click(x=133, y=241)

#Escrever o email destinatario
pyautogui.PAUSE = 2
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#Escrevendo o assunto
pyautogui.PAUSE = 2
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#Escrevendo a mensagem e enviando
pyautogui.PAUSE = 2
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1114, y=950)

#Fechando a aba
pyautogui.hotkey("alt", "f4")