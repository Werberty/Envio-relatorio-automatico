import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1

# Abrindo o navegador
# pyautogui.hotkey('alt', 'tab')
# pyautogui.press('win')
# time.sleep(7)
# pyautogui.write('chrome')
# pyautogui.press('enter')

# # Baixando base de dados
# pyautogui.hotkey('ctrl', 't')
# pyperclip.copy(
#     'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
# pyautogui.hotkey('ctrlleft', 'v')
# pyautogui.press('enter')
# time.sleep(3)

# pyautogui.doubleClick(x=424, y=328)
# time.sleep(3)

# pyautogui.click(x=381, y=405)
# pyautogui.click(x=1160, y=217)
# pyautogui.click(x=934, y=617)
# time.sleep(5)

# analisando dados
dados = pd.read_excel(r'/home/werberty/Downloads/Vendas - Dez.xlsx')
# print(dados)
total_vendas = dados['Valor Final'].sum()
quantidade_produtos = dados['Quantidade'].sum()
melhores_lojas = pd.pivot_table(
    dados, index=['ID Loja'], values='Quantidade', aggfunc='sum').sort_values(ascending=False,
                                                                              by='Quantidade')[:5]
mais_vendidos = pd.pivot_table(
    dados, index=['Produto'], values='Quantidade', aggfunc='sum').sort_values(ascending=False,
                                                                              by='Quantidade')[:5]
print(melhores_lojas)
print()
print(mais_vendidos)
