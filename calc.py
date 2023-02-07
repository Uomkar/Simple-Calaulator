import PySimpleGUI as sg

sg.theme('PythonPlus')
sg.set_options(font="Calibri 14", button_element_size=(6, 3))
btnSize = (6, 3)
layout = [[sg.Input(disabled=True, size=(22), key='output', justification='right'), sg.Button("AC", size=(5), expand_x=True)],
          [sg.Button(7, size=btnSize), sg.Button(8, size=btnSize), sg.Button(9, size=btnSize), sg.Button('+', size=btnSize)],
          [sg.Button(4, size=btnSize), sg.Button(5, size=btnSize), sg.Button(6, size=btnSize), sg.Button('-', size=btnSize)],
          [sg.Button(1, size=btnSize), sg.Button(2, size=btnSize), sg.Button(3, size=btnSize), sg.Button('*', size=btnSize)],
          [sg.Button('=', key='Calc', button_color="orange", size=btnSize),sg.Button(0, size= btnSize),sg.Button('.', size =btnSize), sg.Button('/', size=btnSize)],
          ]

window = sg.Window("Simple_Calculator", layout)

data = []

full_operator = []

while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Calculate':
        print(values)
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.']:
        data.append(event)
        num = ''.join(data)
        window['output'].update(num)
    if event in ['+', '/', '*', '-']:
        full_operator.append(''.join(data))
        data = []
        full_operator.append(event)
        window['output'].update(full_operator)
    if event == 'Calc':
        full_operator.append(''.join(data))
        try:
            res = eval(''.join(full_operator))
            window['output'].update(res)
            full_operator = []
        except:
            window['output'].update("Infinity")

    if event == 'AC':
        full_operator = []
        data = []
        window['output'].update('')



window.close()