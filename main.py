import PySimpleGUI as sg

name = sg.popup_get_text('What is your name?')

sg.popup('Hi ' + name)