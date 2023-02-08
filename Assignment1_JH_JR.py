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
    sg.Text("What age range best describes you?"),
    sg.Radio("Under 20", "Group1"),
    sg.Radio("20 - 29", "Group1"),
    sg.Radio("30 - 39", "Group1"),
    sg.Radio("40 - 49", "Group1"),
    sg.Radio("50+", "Group1")
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