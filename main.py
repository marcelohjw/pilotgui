import PySimpleGUI as sg

hours = sg.popup_get_text('Quantas horas você estudou hoje?')

resu = int(hours) * 10
if resu < 20:
    sg.popup_annoying('Preguiçoso! Estude mais!')
else:
    sg.popup_annoying('Muito bem! Continue nesse ritmo!')