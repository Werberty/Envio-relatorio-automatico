import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1

# Abrindo o navegador
pyautogui.hotkey('alt', 'tab')
pyautogui.press('win')
time.sleep(7)
pyautogui.write('chrome')
pyautogui.press('enter')

# Baixando base de dados
pyautogui.hotkey('ctrl', 't')
pyperclip.copy(
    'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrlleft', 'v')
pyautogui.press('enter')
time.sleep(3)

pyautogui.doubleClick(x=424, y=328)
time.sleep(3)

pyautogui.click(x=381, y=405)
pyautogui.click(x=1160, y=217)
pyautogui.click(x=934, y=617)
time.sleep(5)

# analisando dados
try:
    dados = pd.read_excel(r'/home/werberty/Downloads/Vendas - Dez.xlsx')
except FileExistsError as e:
    print('Arquivo não encontrado.')
total_vendas = dados['Valor Final'].sum()
quantidade_produtos = dados['Quantidade'].sum()
melhores_lojas = pd.pivot_table(
    dados, index=['ID Loja'], values='Quantidade', aggfunc='sum').sort_values(ascending=False,
                                                                              by='Quantidade')[:5]
mais_vendidos = pd.pivot_table(
    dados, index=['Produto'], values='Quantidade', aggfunc='sum').sort_values(ascending=False,
                                                                              by='Quantidade')[:5]

# enviando o email
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/2/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(4)

pyautogui.click(x=77, y=229)
time.sleep(2)
pyautogui.write('werbertydroid@gmail.com')
    # pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

corpo_email = f'''
Total de vendas: R${total_vendas:,.2f}
Total de produtos vendido: {quantidade_produtos:,}

Top 5 lojas em vendas:
{melhores_lojas}

Top 5 produtos mais vendidos:
{mais_vendidos}'''
pyperclip.copy(corpo_email)
pyautogui.hotkey('ctrl', 'v')
# pyautogui.hotkey('ctrl', 'enter')
