# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:03:13 2023

@author: Justin Roy and James Humphrey
"""

import PySimpleGUI as sg
import pandas as pd

df = pd.read_csv(r'KnowledgeBase.csv')
print(df)

text = """Welcome to Pet Lyfe! This is an \"expert system\"  that will ask you a
series of questions to estimate what kind of pet fits your lifestyle best.
Select the different tabs and answer all questions to find out what kind
of pet best suits your lifestyle Click NEXT to continue."""

# Blackboard containing all the possible pets, owned pets will be
# added to petsAlreadyOwnedList 
possiblePetList = ["Dog", "Cat", "Bird", "Hamster", "Lizard", "Fish"]
petsAlreadyOwnedList = []

fontTitle = "Helvetica"
fontSizeTitle = 25

fontQuestion = "Helvetica"
fontSizeQuestion = 20

column = [
    [sg.Text(text, size=(60,4), justification="center",font=(fontTitle, fontSizeTitle)) ],
    
    [sg.Button("Next", font=(fontQuestion, fontSizeQuestion))]]

layout = [[sg.VPush()],
         [sg.Push(), sg.Column(column, element_justification='c'), sg.Push()],
         [sg.VPush()]]

window = sg.Window('Pet Lyfe', layout)

while True:
    event, values = window.read()

    if event == "Next" or event ==  sg.WIN_CLOSED:
        break
    
window.close()
column = [
    
    [
    sg.Text("Are you alergic to any of these pets? (check all that apply)",font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Dog", default=False,  font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Cat", default=False,font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Bird", default=False, font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Hamster",default=False, font=(fontQuestion, fontSizeQuestion))
    ],
    [sg.Button("Next", font=(fontQuestion, fontSizeQuestion))]]

layout = [[sg.VPush()],
         [sg.Push(), sg.Column(column, element_justification='c'), sg.Push()],
         [sg.VPush()]]

window = sg.Window('Pet Lyfe', layout)

while True:
    event, values = window.read()

    if event == "Next" or event ==  sg.WIN_CLOSED:
        break
    
window.close()
valuesQ1 = values 

#inference engine removing pets that the user is allergic to from list
if valuesQ1[0]:
    possiblePetList.remove("Dog")
if valuesQ1[1]:
    possiblePetList.remove("Cat")
if valuesQ1[2]:
    possiblePetList.remove("Bird")
if valuesQ1[3]:
    possiblePetList.remove("Hamster")

column = [
    
    [
    sg.Text("Do you own any of these pets? (check all that apply)",font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Dog", default=False,  font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Cat", default=False,font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Bird", default=False, font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Hamster",default=False, font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Lizard", default=False,  font=(fontQuestion, fontSizeQuestion)),
    sg.Checkbox("Fish", default=False,font=(fontQuestion, fontSizeQuestion)),
    ],
    [sg.Button("Next", font=(fontQuestion, fontSizeQuestion))]]

layout = [[sg.VPush()],
         [sg.Push(), sg.Column(column, element_justification='c'), sg.Push()],
         [sg.VPush()]]

window = sg.Window('Pet Lyfe', layout)

while True:
    event, values = window.read()

    if event == "Next" or event ==  sg.WIN_CLOSED:
        break
    
window.close()

#inference engine taking note of owned pets
valuesQ2 = values
if valuesQ2[0]:
    petsAlreadyOwnedList.append("Dog")
if valuesQ2[1]:
    petsAlreadyOwnedList.append("Cat")
if valuesQ2[2]:
    petsAlreadyOwnedList.append("Bird")
if valuesQ2[3]:
    petsAlreadyOwnedList.append("Hamster")
if valuesQ2[4]:
    petsAlreadyOwnedList.append("Lizard")
if valuesQ2[5]:
    petsAlreadyOwnedList.append("Fish")

textCatWarning = """Just a reminder that cats can cohabitate with any of the pets we will recomend as long as proper cat proofing is done to cages and aquariums."""
print(petsAlreadyOwnedList)

#inference engine that warns the user of they own a cat
if (valuesQ2[1]):
    column = [
    [sg.Text(textCatWarning, size=(60,4), justification="center",font=(fontTitle, fontSizeTitle)) ],
    
    [sg.Button("Next", font=(fontQuestion, fontSizeQuestion))]]
    layout = [[sg.VPush()],
        [sg.Push(), sg.Column(column, element_justification='c'), sg.Push()],
        [sg.VPush()]]
    window = sg.Window('Pet Lyfe', layout)
    while True:
        event, values = window.read()

        if event == "Next" or event ==  sg.WIN_CLOSED:
            break
    
    window.close()


