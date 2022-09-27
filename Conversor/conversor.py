import PySimpleGUI as sg

layout = [
    [sg.Input(key='-input-'), sg.Spin(['km p/ milhas', 'kg p/ lb', 'seg p/ min'], key='-unidades-'),
     sg.Button('Converter', key='-converter-')],
    [sg.Text('', key='-resultado-')]
]

window = sg.Window('Conversor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-converter-':
        valor_input = values['-input-']
        if valor_input.isnumeric():
            match values['-unidades-']:
                case 'km p/ milhas':
                    resultado = round(float(valor_input) * 0.6214, 2)
                    resultado_string = f'{valor_input}km é igual a {resultado} milhas'
                case 'kg p/ lb':
                    resultado = round(float(valor_input) * 2.20462, 2)
                    resultado_string = f'{valor_input}kg é igual a {resultado}lb'
                case 'seg p/ min':
                    resultado = round(float(valor_input) / 60, 2)
                    resultado_string = f'{valor_input} seg é igual a {resultado} min'
            window['-resultado-'].update(resultado_string)
        else:
            window['-resultado-'].update('Por favor, apenas números')
window.close()
