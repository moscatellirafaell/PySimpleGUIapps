import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 14', button_element_size=(6, 3))
    button_size = (6, 3)
    layout = [
              # [sg.Text('resultado', font='Franklin 26', justification='right', expand_x=True)],
              [sg.Push(), sg.Text('0', font='Franklin 26', pad=(10, 20), right_click_menu=theme_menu,
                                  key='-RESULTADO-')],
              [sg.Button('c', size=button_size), sg.Button('√', size=button_size), sg.Button('%', size=button_size),
               sg.Button('÷', size=button_size)],
              [sg.Button('7', size=button_size), sg.Button('8', size=button_size), sg.Button('9', size=button_size),
               sg.Button('x', size=button_size)],
              [sg.Button('4', size=button_size), sg.Button('5', size=button_size), sg.Button('6', size=button_size),
               sg.Button('-', size=button_size)],
              [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button('3', size=button_size),
               sg.Button('+', size=button_size)],
              [sg.Button('0', size=button_size), sg.Button('.', size=button_size), sg.Button('=', expand_x=True)]
    ]

    return sg.Window('Calculadora', layout)


theme_menu = ['menu', ['LightGrey', 'Dark', 'HotDogStand', 'Random']]
window = create_window('LightGrey1')

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in '0123456789.':
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-RESULTADO-'].update(num_string)

    if event in '+-x÷%√':
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-RESULTADO-'].update('0')

    if event == '=':
        full_operation.append(''.join(current_num))
        resultado = eval(''.join(full_operation))
        window['-RESULTADO-'].update(resultado)
        full_operation = []

    if event == 'c':
        current_num = []
        full_operation = []
        window['-RESULTADO-'].update('0')

window.close()
