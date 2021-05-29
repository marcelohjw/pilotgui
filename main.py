import PySimpleGUI as sg

hours = sg.popup_get_text('Quantas horas você estudou hoje?')

resu = int(hours) * 10

sg.popup_annoying(str(resu))