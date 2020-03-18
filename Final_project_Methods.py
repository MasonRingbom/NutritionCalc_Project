#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:46:34 2020

@author: masonringbom
"""
import PySimpleGUI as sg
import matplotlib.pyplot as plt
#Gets food nutrition info "Loopdy" on each loop so you can see it is working 
from Final_project_webscrape import *


class nutrition():

    total_calories = 0
    total_sat = 0
    total_fat = 0
    total_cholesterol = 0
    total_sodium = 0
    total_carbs = 0
    total_protein = 0
    
    #Creating a GUI make it as init
#    def __init__():
#        
#        sg.theme('BluePurple')
#        
#        layout = [[sg.Text("Hello! Welcome To Nutrition Calc")],
#                   [sg.Text('What is your height in inches?', size=(25, 1)), sg.InputText('')],
#                   [sg.Text('What is your weight in lbs?', size=(25, 1)), sg.InputText('')],
#                   [sg.Text('How old are you?', size=(25, 1)), sg.InputText('')],
#                   [sg.Text("What is your name?", size=(25,1)), sg.InputText('')],
#                   [sg.Text("Please list the corresponding number with the food ate")],
#                   [sg.Text(names)],
#                   [sg.Text("What foods did you eat?", size=(25,1)) , sg.InputText('')],
#                   [sg.Submit(), sg.Cancel()]
#                   ]

#        window = sg.Window('Pattern 2B', layout)
#        window.read()
#        window.close()
        
        
#        return your_height, your_weight, your_age, your_name, foods_chose
    
    #Getting stats and finding calories needed
    def __init__(self, height, weight, age, name):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        #Conversions from input
        self.height = self.height * 2.54
        self.weight = self.weight * 0.45
        bmr = lambda W, H, A: ((10*W)+(6.25*H)-(5*A)+5)*1.5
        mycals = bmr(self.weight, self.height, self.age)
        self.mycals = mycals
        
        return
    #Totalling each nutrient consumed
    def food_location(self, x):
        for i in x:
            self.total_calories += calories_nums[i]
            self.total_sat += sfats_nums[i]
            self.total_fat += total_fats_nums[i]
            self.total_cholesterol += cholesterol_nums[i]
            self.total_sodium += sodium_nums[i]
            self.total_carbs += carbs_nums[i]
            self.total_protein += protein_nums[i]
        
        return(self.total_calories, self.total_sat, self.total_fat, self.total_cholesterol, self.total_sodium, self.total_carbs, self.total_protein)
    
    #User entering what foods they ate
    def foods_chosen(self):
        proceed = True 
        #Printing "Menu"
        print("Hello", self.name,"!")
        for i in range(len(names)):
            print(i, names[i])
            
        #Tallies all the food eaten 
        foods_chose = []
        while proceed == True:
            #Getting user input 
            item = int(input("Please enter the corresponding number for the food. When you are finished entering type '-1'. "))
            #preventing a crash from a number outve range
            if item >= len(names) or item < -1:
                print("Number out of range try again")
            else:
                #Escapes loop
                if item == -1:
                    proceed = False
                else:
                    #Tallies food totals
                    foods_chose.append(item)
        self.food_location(foods_chose)
        return 
        
        #Making amount of nutrients true to your stats
    def scale_values(self,x):
        scale_percentage =  (x/2000)
        self.cals_needed = 2000 * scale_percentage
        self.sat_needed = 10 * scale_percentage
        self.fat_needed = 44.4 * scale_percentage
        self.cholesterol_needed = 300 * scale_percentage
        self.sodium_needed = 2400 * scale_percentage
        self.carbs_needed = 225 * scale_percentage
        self.protein_needed = 175 * scale_percentage
        
        return (self.cals_needed, self.sat_needed, self.fat_needed, self.cholesterol_needed, self.sodium_needed, self.carbs_needed, self.protein_needed)
        
    
    def pie_chart(self, total_fat, total_carbs, total_protein):
        pie_names = ["total_fat", "total_carbs", "total_protein"]
        piece_size = [total_fat, total_carbs, total_protein]
        fig1, ax1 = plt.subplots()
        ax1.pie(piece_size, labels = pie_names, autopct = '%.2f', startangle = 90)
        ax1.axis("equal")
        plt.savefig("/Users/masonringbom/Desktop/CS 112/Final_project/Reports/Daily_Report_Image.jpg")
        return
    
    def daily_report(self):
        with open("/Users/masonringbom/Desktop/CS 112/Final_project/Reports/Daily_Report.txt" , 'w') as report:
            report.write(self.name)
            report.write("\n")
            report.write(str(self.age))
            report.write(" years old."+ "\n")
            report.write(str(self.height/2.54) + " inches" + "\n")
            report.write(str(self.weight/0.45) + " lbs" + "\n")
            report.write("Your nutrient totals / Reccomended amounts" + "\n")
            report.write("CALORIES" + "\n")
            report.write(str(int(self.total_calories)) + " / " + str(int(self.cals_needed)) + "\n")
            report.write("WATER" + "\n")
            report.write("TOTAL FAT" + "\n")
            report.write(str(int(self.total_fat)) + "g" + " / " + str(int(self.fat_needed)) + "g" + "\n")
            report.write("SATURATED FAT" + "\n")
            report.write(str(int(self.total_sat)) + "g" + " / " + str(int(self.sat_needed)) + "g" + "\n")
            report.write("CARBOHYDRATE" + "\n")
            report.write(str(int(self.total_carbs)) + "g" + " / " + str(int(self.carbs_needed)) + "g" + "\n")
            report.write("PROTEIN" + "\n")
            report.write(str(int(self.total_protein)) + "g" + " / " + str(int(self.protein_needed)) + "g" + "\n")
            report.write("CHOLESTEROL" + "\n")
            report.write(str(int(self.total_cholesterol)) + "mg" + " / " + str(int(self.cholesterol_needed)) + "mg" + "\n")
            report.write("SODIUM" + "\n")
            report.write(str(int(self.total_sodium)) + "mg" + " / " + str(int(self.sodium_needed)) + "mg" + "\n")
            report.write("\n")
            report.write("ALL RECCOMENDATIONS BASED OFF OF HEIGHT,WEIGHT,AND AGE. A MACRO SPLIT OF 45/20/35 used" + "\n" + "\n" + "\n")
            mason.pie_chart(mason.total_fat, mason.total_carbs, mason.total_protein)


mason = nutrition(float(input("Enter your height in inches ")),float(input("Enter your weight in lbs ")), float(input("Enter your age ")), input("Whats your name? "))
mason.scale_values(mason.mycals)
mason.foods_chosen()
mason.daily_report()
#print("Calories consumed" ,mason.total_calories)
#print("Total fat" ,mason.total_fat)
#print("Saturated fat" ,mason.total_sat)
#print("Total cholesterol" ,mason.total_cholesterol)
#print("Total sodium" ,mason.total_sodium)
#print("Total carbs" ,mason.total_carbs)
#print("Total protein" ,mason.total_protein)
