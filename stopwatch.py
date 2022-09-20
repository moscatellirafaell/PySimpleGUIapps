import PySimpleGUI as sg
from time import time


def create_window():
    sg.theme('Black')
    layout = [
        [sg.Push(), sg.Image('cross.png', pad=0, enable_events=True, key='-CLOSE-')],
        [sg.VPush()],
        [sg.Text('0', font='Young 50', key='-TIME-')],
        [sg.Button('start', button_color=('#FFFFFF', '#00CF00'), border_width=0,
                   key='-STARTSTOP-'),
         sg.Button('lap', button_color=('#FFFFFF', '#0030FF'), border_width=0, key='-LAP-',
                   visible=False)],
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()]
    ]
    return sg.Window('Stopwatch', layout, size=(300, 300), no_titlebar=True,
                   element_justification='center')


window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active:
            # from active to stop
            active = False
            window['-STARTSTOP-'].update('reset', button_color=('#FFFFFF', '#00CF00'))
            window['-LAP-'].update(visible=False)
        else:
            # from stop to reset
            if start_time > 0:
                # from start to active
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1
            else:
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('stop', button_color=('white', 'red'))
                window['-LAP-'].update(visible=True)

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount), sg.VSeparator(),
                                                 sg.Text(elapsed_time)]])
        lap_amount += 1

window.close()
