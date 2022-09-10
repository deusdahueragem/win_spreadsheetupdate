from PySimpleGUI import PySimpleGUI as sg
import gspread, re
from oauth2client.service_account import ServiceAccountCredentials

sg.theme('Reddit')
layout = [
    [sg.Text('Caminho do TXT:'),sg.Input(key='txt_path'),sg.FileBrowse('Buscar')],
    [sg.Text('Autenticação JSON:'),sg.Input(key='json_path'),sg.FileBrowse('Buscar')],
    [sg.Text('Nome da planilha:'),sg.Input(key='spreadsheet_name')],
    [sg.Button('Atualizar Planilha')]
]

janela = sg.Window('Atualizador de Planilhas', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if valores['txt_path'] != "" and valores['json_path'] != "" and valores['spreadsheet_name']:
        #Abre a conexão com as planilhas do Google
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(valores['json_path'], scope)
        client = gspread.authorize(creds)
        #Seleciona qual planilha será usada
        sheet = client.open(valores['spreadsheet_name']).sheet1
        #Abre o arquivo TXT onde está armazenado os nomes dos hosts que serão pesquisados na planilha
        arquivo = open(valores['txt_path'], 'r')
        #Laço de repetição para ler linha a linha o arquivo TXT
        for i in arquivo.readlines():
            #Busca apenas palavras sem espaço na linha I do laço de repetição
            nomehost = re.findall('\S+', i)
            #Transforma o nome encontrado em cada linha em tudo minúsculo
            nomehost = (nomehost.pop()).lower()
            #Busca o indice X e Y de acordo com o nome do host
            list_of_hashes = sheet.find(nomehost)
            #Grava na variavel apenas o indice que indica a linha na planilha
            att_x = list_of_hashes.row
            #Condicional para checar se a coluna de status da linha indicada se encontra como Aguardando
            if sheet.cell(att_x, 4).value == "AGUARDANDO":
                #Atualiza a coluna de status da linha indicada de AGUARDANDO para OK
                sheet.update_cell(att_x, 4, 'OK')
        #Fecha o documento TXT
        arquivo.close()
    else:
        sg.popup('Você precisa preencher todos os campos para continuar',title='Preencha todos os campos',button_color='red')