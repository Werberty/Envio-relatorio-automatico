# Envio-relatorio-automatico
---
 Envio de **relatório automático** por email usando pyautogui e pandas, 
 para funcionar especificamente no meu notebook com linux.
 
 ## Funcionamento
 1. Abri o navegador e acessa o link do dowload da planilha de dados
 2. Usa a planilha de vendas para gerar marcadores e tabelas com o pandas
 3. Entra no gmail e cria um corpo de email contendo a analise de dados da planilha e a envia
 
 ## Bibliotecas usadas
 ```
 import pyautogui
 import pyperclip
 import time
 import pandas as pd
 ```
