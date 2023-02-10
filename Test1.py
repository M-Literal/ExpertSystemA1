# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:03:13 2023

@author: Justin Roy and James Humphrey
"""

import PySimpleGUI as sg
import pandas as pd

df = pd.read_csv(r'KnowledgeBase.csv')
explanationSubsystem = "This pet was chosen for you because: "

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
explanationSubsystem = explanationSubsystem + "You are not alergic to it. "

#inference engine removing pets that the user is allergic to from list
if valuesQ1[0]:
    possiblePetList.remove("Dog")
    df = df.drop(0)
if valuesQ1[1]:
    possiblePetList.remove("Cat")
    df = df.drop(1)
if valuesQ1[2]:
    possiblePetList.remove("Bird")
    df = df.drop(2)
if valuesQ1[3]:
    possiblePetList.remove("Hamster")
    df = df.drop(5)


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

textCatWarning = """ Just a reminder that cats can cohabitate with any of the pets we will recomend as long as proper cat proofing is done to cages and aquariums."""


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


budgetMedianFloat = df['Yearly Budget'].median()
budgetMedianString = str(budgetMedianFloat)
column = [
    
    [
    sg.Text("Are you prepared to pay $"+budgetMedianString+" or more per year for your pet?",font=(fontQuestion, fontSizeQuestion)),
    sg.Radio("Yes","Group1", default=True, font=(fontQuestion, fontSizeQuestion)),
    sg.Radio("No", "Group1", font=(fontQuestion, fontSizeQuestion))
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

valuesQ3 = values
if valuesQ3[0]:
    df = df[df['Yearly Budget'] >= budgetMedianFloat]
    explanationSubsystem = explanationSubsystem + " You said you were comfortable paying more then "+ budgetMedianString + "$ per year."
else:
    df = df[df['Yearly Budget'] < budgetMedianFloat]
    explanationSubsystem = explanationSubsystem + " You said you wanted to pay less than "+ budgetMedianString + "$ per year."

if len(df.index)!= 1:
    timeRequirmentFloat = df['Time Commitment per day in Minutes'].median()
    timeRequirmentString = str(timeRequirmentFloat)
    column = [
    
    [
    sg.Text("Are you prepared to spend "+timeRequirmentString+" or more minutes per day taking care of your pet?",font=(fontQuestion, fontSizeQuestion)),
    sg.Radio("Yes","Group2", default=True, font=(fontQuestion, fontSizeQuestion)),
    sg.Radio("No", "Group2", font=(fontQuestion, fontSizeQuestion))
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

    valuesQ4 = values
    if valuesQ4[0]:
        df = df[df['Time Commitment per day in Minutes'] >= timeRequirmentFloat] 
        explanationSubsystem = explanationSubsystem + " You said you were comfortable spending "+ timeRequirmentString + " or more minutes per day on pet upkeep."
    else:
        df = df[df['Time Commitment per day in Minutes'] < timeRequirmentFloat] 
        explanationSubsystem = explanationSubsystem + " You said you were comfortable spending less than "+ timeRequirmentString + " minutes per day on pet upkeep."

if len(df.index)!= 1:
    timeAloneFloat = df['Hours pet can be left alone'].median()
    timeAloneString = str(timeAloneFloat)
    column = [
    
    [
    sg.Text("Are there times when you will be away from your pet for more then "+timeAloneString+" hours",font=(fontQuestion, fontSizeQuestion)),
    sg.Radio("Yes","Group3", default=True, font=(fontQuestion, fontSizeQuestion)),
    sg.Radio("No", "Group3", font=(fontQuestion, fontSizeQuestion))
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

    valuesQ4 = values
    if valuesQ4[0]:
        df = df[df['Hours pet can be left alone'] >= timeAloneFloat]
        explanationSubsystem = explanationSubsystem + " You said you might need to leave the pet more then "+ timeAloneString + " hours at a time." 
    else:
        df = df[df['Hours pet can be left alone'] < timeAloneFloat] 
        explanationSubsystem = explanationSubsystem + " You said you wouldn't need to leave the pet more then "+ timeAloneString + " hours at a time." 
df = df.reset_index()
petChosen = df._get_value(0, 'Pet')
if petChosen == "Cat":
    explanationSubsystem = explanationSubsystem + textCatWarning

petStats = petChosen+"s cost roughly"+ str(df._get_value(0, 'Yearly Budget'))+"$ per year. They require "
column = [
[sg.Text("The pet we recomend is: " + petChosen , size=(80,4), justification="center",font=(fontTitle, fontSizeTitle)) ],  
[sg.Text(explanationSubsystem , size=(80,10), justification="center",font=(fontTitle, fontSizeTitle)) ],
[sg.Text(petStats , size=(80,10), justification="center",font=(fontTitle, fontSizeTitle)) ],  
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
print(df)



