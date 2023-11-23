import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]
    
    return sg.Window('Minha Lista', layout=layout, finalize=True)

# Cria a janela
janela = criar_janela_inicial()

# Regras dessa janela. Informações dos eventos na tela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Nova Tarefa":
        # Especificando o que deve ser adicionado de fato. Um layout precisa estar fechado em []
        janela.extend_layout(janela['container'], [[sg.Checkbox(' '), sg.Input(' ')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
