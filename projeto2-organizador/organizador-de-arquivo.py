import os
from tkinter.filedialog import askdirectory # importa uma função dessa biblioteca

caminho = askdirectory("Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

#Locais para onde vou querer jogar este arquivos

locais = {
    "imagens": [".png", "jpg"],
    "planilhas": [".xlsx"],
    "documentos": [".docx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "executaveis": [".exe"]
}

for arquivo in lista_arquivos:
    nome, extesao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extesao in locais[pasta]:
            if not os.path.exist(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

print("Ação realizada com sucesso!")
        