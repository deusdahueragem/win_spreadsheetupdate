HOW IT WORKS

The program searches row by row by host names and searches the spreadsheet, finding it, it saves the value of the index of the row and uses it to update the Status column of the spreadsheet automatically.
You will need a spreadsheet with 2 columns (but you will need to change the code because mine is configured for 4 columns), the first column should be the hostname, my fourth column is the Status. With the worksheet ready you need to configure the access to the worksheet using the Google API (don't forget to allow editing access to the user inside your worksheet too).
After configuring the Google API you will receive a JSON credentials file, and finally you need the TXT file with the hostnames, each hostname must be separated by a line break, if they are together on the same line it will not work .
Run the program, enter the TXT path containing the hostnames, enter the JSON file with the credentials and finally the exact name of the worksheet as it is in your Google Drive, press the "Update Worksheet" button and you will see the magic happen.

COMO FUNCIONA

O programa busca linha a linha por nomes de host e pesquisa na planilha, encontrando ele guarda o valor do indice da linha e utiliza para atualizar a coluna de Status da planilha automaticamente.
Você irá precisar de uma planilha com 2 colunas(porém será necessário fazer alteração no código pois a minha está configurada para 4 colunas), a primeira coluna deve ser o nome do host, minha quarta coluna fica o Status. Com a planilha pronta você precisa configurar o acesso a planilha usando a API do Google(não esqueça de liberar acesso de edição ao usuário dentro da sua planilha também).
Após configurar a API do Google você vai receber um arquivo de credenciais em JSON, e por fim precisa do arquivo TXT com os nomes do host, cada nome de host deve ser separados por quebra de linha, caso estejam juntos na mesma linha não irá funcionar.
Execute o programa, informe o caminho do TXT contendo os nomes do host, informe o arquivo JSON com as credenciais e por fim o nome exato da planilha conforme está em seu Google Drive, aperte o botão "Atualizar Planilha" e verá a magica acontecer.