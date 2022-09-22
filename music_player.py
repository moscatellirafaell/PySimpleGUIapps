import PySimpleGUI as sg
import base64
from io import BytesIO
from PIL import Image
from pygame import mixer
mixer.init()


def base64_image_import(path):
    image = Image.open(path)
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    b64 = base64.b64encode(buffer.getvalue())
    return b64


# import song
path = sg.popup_get_file('Open', no_window=True)
song_name = path.split('/')[-1].split('.')[0]
song = mixer.Sound(path)
song.play()

sg.theme('reddit')

play_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Text(song_name, font='Arial 20'), sg.Push()],
    [sg.VPush()],
    [sg.Push(),
     sg.Button(image_data=base64_image_import('play.png'), key='-PLAY-',
               button_color='white', border_width=0),
     sg.Text(' '),
     sg.Button(image_data=base64_image_import('pause.png'), key='-PAUSE-',
               button_color='white', border_width=0),
     sg.Push()],
    [sg.VPush()],
    [sg.Progress(100, size=(20, 20), key='-PROGRESS-')]
]

volume_layout = [
    [sg.VPush()],
    [sg.VPush(), sg.Slider(range=(0, 100), default_value=50, orientation='h',
                           key='-VOLUME-'), sg.VPush()],
    [sg.VPush()]
]

layout = [
    [sg.TabGroup([[sg.Tab('Play', play_layout), sg.Tab('Volume', volume_layout)]])]
]

window = sg.Window('Music Player', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
