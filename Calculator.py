import tkinter as tk
import PySimpleGUI as sg

layout =  [

    [sg.Column([
        [sg.Text("Enter The Overworld cords.", font=("", 14))],
        [sg.Text("X Cords;")],
        [sg.Input(key="x")],
        [sg.Text("Z Cord;")],
        [sg.Input(key="z")],
        [sg.Button("Calculate")]
    ])],

    [sg.Column([
        [sg.Image(filename="index.png")]
    ])]
]

Window = sg.Window("My Simple PyGUI", layout, size=(296,732))

while True:
    event, values = Window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Calculate":
        X = int(values["x"]) * 8 
        Z = int(values["z"]) * 8
        sg.popup(f"The nether cords are: \n X:{X} \n Z:{Z} ")
        break

Window.close()
