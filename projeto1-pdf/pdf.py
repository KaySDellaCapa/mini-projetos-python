import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir()
lista_arquivos.sort()

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"mini-projetos-py/{arquivo}")
        

merger.write("Acoplado.pdf") #Vai criar um pdf final