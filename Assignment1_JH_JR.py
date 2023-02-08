# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:03:13 2023

@author: Justin Roy and James Humpfrey
"""

import PySimpleGUI as sg

text = """Welcome to Pet Lyfe! This is an \"expert system\"  that will ask you a
series of questions to estimate what kind of pet fits your lifestyle best.
Select the different tabs and answer all questions to find out what kind
of pet best suits your lifestyle."""

column = [
    [sg.Text(text, size=(60,4), justification="center")],
    [
    sg.Text("First of all, what is your prefered pet?"),
    sg.Radio("Dog", "Group0"),
    sg.Radio("Cat", "Group0"),
    sg.Radio("Other", "Group0")
    ],
    [
    sg.Text("What age range best describes you?"),
    sg.Radio("Under 20", "Group1"),
    sg.Radio("20 - 29", "Group1"),
    sg.Radio("30 - 39", "Group1"),
    sg.Radio("40 - 49", "Group1"),
    sg.Radio("50+", "Group1")
    ],
    [
    sg.Text("What range of price are you willing to spend for the pet?"),
    sg.Radio("Under 100$", "Group2"),
    sg.Radio("100$ - 400$", "Group2"),
    sg.Radio("401$ - 700$", "Group2"),
    sg.Radio("700$+", "Group2")
    ],
    [
    sg.Text("On a scale from 1 to 5, how active would you say you are?"),
    sg.Radio("1", "Group3"),
    sg.Radio("2", "Group3"),
    sg.Radio("3", "Group3"),
    sg.Radio("4", "Group3"),
    sg.Radio("5", "Group3")
    ],
    [
    sg.Text("How many hours per day are you away from home, for work or other reasons?"),
    sg.Radio("1-2 hours", "Group4"),
    sg.Radio("2-3 hours", "Group4"),
    sg.Radio("3-5 hours", "Group4"),
    sg.Radio("5-8 hours", "Group4"),
    sg.Radio("8+ hours", "Group4")
    ],
    [sg.Button("Exit")]]

layout = [[sg.VPush()],
         [sg.Push(), sg.Column(column, element_justification='c'), sg.Push()],
         [sg.VPush()]]

window = sg.Window('Pet Lyfe', layout)

while True:
    event, values = window.read()
    
    if event == "Exit" or event ==  sg.WIN_CLOSED:
        break
    
window.close()