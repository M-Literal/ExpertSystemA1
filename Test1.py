# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:03:13 2023

@author: Justin Roy and James Humphrey
"""

import PySimpleGUI as sg

text = """Welcome to Pet Lyfe! This is an \"expert system\"  that will ask you a
series of questions to estimate what kind of pet fits your lifestyle best.
Select the different tabs and answer all questions to find out what kind
of pet best suits your lifestyle."""

fontTitle = "Helvetica"
fontSizeTitle = 25

fontRadio = "Helvetica"
fontSizeRadio = 20

column = [
    [sg.Text(text, size=(60,4), justification="center",font=(fontTitle, fontSizeTitle)) ],
    [
    sg.Text("What range of price are you willing to spend for the pet?",font=(fontRadio, fontSizeRadio)),
    sg.Radio("Under 100$", "Group1", default=True, font=(fontRadio, fontSizeRadio)),
    sg.Radio("100$ - 700$", "Group1", font=(fontRadio, fontSizeRadio)),
    sg.Radio("700$+", "Group1", font=(fontRadio, fontSizeRadio))
    ],
    [
    sg.Text("How active would you say you are?", font=(fontRadio, fontSizeRadio)),
    sg.Radio("Not very active", "Group2",default=True, font=(fontRadio, fontSizeRadio)),
    sg.Radio("Somewhat active", "Group2",font=(fontRadio, fontSizeRadio)),
    sg.Radio("Very active", "Group2", font=(fontRadio, fontSizeRadio)),
    ],
    [
    sg.Text("How many hours per day are you away from home, for work or other reasons?", font=(fontRadio, fontSizeRadio)),
    sg.Radio("Less that 2 hours", "Group3", default=True, font=(fontRadio, fontSizeRadio)),
    sg.Radio("2-6 hours", "Group3", font=(fontRadio, fontSizeRadio)),
    sg.Radio("6+ hours", "Group3", font=(fontRadio, fontSizeRadio))
    ],
    [
    sg.Text("How many hours per week are you willing to spend on training with your pet?",font=(fontRadio, fontSizeRadio)),
    sg.Radio("Less that 1 hour", "Group4",default=True, font=(fontRadio, fontSizeRadio)),
    sg.Radio("1-3 hours", "Group4", font=(fontRadio, fontSizeRadio)),
    sg.Radio("3+ hours", "Group4", font=(fontRadio, fontSizeRadio))
    ],
    [sg.Button("Submit", font=(fontRadio, fontSizeRadio))]]

layout = [[sg.VPush()],
         [sg.Push(), sg.Column(column, element_justification='c'), sg.Push()],
         [sg.VPush()]]

window = sg.Window('Pet Lyfe', layout)

while True:
    event, values = window.read()

    if event == "Submit" or event ==  sg.WIN_CLOSED:
        break
    
window.close()



print(values)