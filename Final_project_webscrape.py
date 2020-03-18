#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:39:55 2020

@author: masonringbom
"""
#IMPORTING 
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import numpy as np



#Making list of foods webpage
foods = ["https://tools.myfooddata.com/nutrition-facts.php?food=05336&serv=wt1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=9003&serv=wt1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=173944&serv=wt2&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=169097&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=171287&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=171140&serv=wt9&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=475389&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=173379&serv=wt9&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=339463&serv=100g&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=703030&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=439803&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=484842&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=171304&serv=100g&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=171265&serv=wt9&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=648792&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=587763&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=465370&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=173905&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=487765&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=167762&serv=wt3&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=171711&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=170008&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=173647&serv=wt2&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=168462&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=173414&serv=wt4&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=171413&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=173410&serv=wt1&qty=1",
         "https://tools.myfooddata.com/nutrition-facts.php?food=173418&serv=wt1&qty=1"
         ]

#List of each value from food
names = []
calories = []
sfats = []
total_fats = []
cholesterol = []
sodium = []
carbs = []
protein = []

#Split and measurement removed lists
total_fats_strings = []
sfats_strings = []
cholesterol_strings = []
sodium_strings = []
carbs_strings = []
protein_strings = []

#List of numbers as floats 
calories_nums = []
total_fats_nums = []
sfats_nums = []
cholesterol_nums = []
sodium_nums = []
carbs_nums = []
protein_nums = []

#***************************************
        #SCRAPE THE WEBSITE GETTING ALL WANTED INFO 
#***************************************

#Getting to the website/food of choice 
for i in range(len(foods)):
    page = requests.get(foods[i])
    sleep(3)
    print('Please wait loading food')

#Setting up the content with the parser w/ prettify example
    soup = BS(page.content, "html.parser")

#Getting the name of the food
    title_name = soup.find(class_="nftitle")
    name = title_name
    names.append(name.get_text())

#Getting inside nutrition label
    nutrition_label = soup.find_all(class_="nutrition-facts-table")
    in_food = nutrition_label[0]
    total_cals = nutrition_label[0]
    saturated_fats = nutrition_label[0]

#Calories per serving 
    kcal = total_cals.find_all(class_="nft-cal-amt")
    calories.append(kcal[0].get_text())

#Grams of saturated fats
    sat_fat = saturated_fats.find(class_="sub-amt")
    sfats.append(sat_fat.get_text())

#What is inside of a serving macros
    in_serving = in_food.find_all(class_="nfttd")
    for i in range(0,1):
        total_fats.append(in_serving[0].get_text())
        cholesterol.append(in_serving[1].get_text())
        sodium.append(in_serving[2].get_text())
        carbs.append(in_serving[3].get_text())
        protein.append(in_serving[4].get_text())

#***************************************
        #FUNCTIONS
#***************************************
        
#Splitting the values
def splitter(the_list,split_list):
    for i in the_list:
        numbers = i.split()
        split_list.append(numbers) 
    return split_list

#Removing gram and title 
def gram_remover(gram_list):
    for i in gram_list:
        for x in i:
            i[2] = i[2][:-1:]
            del i[1]
            del i[0]
    return gram_list

#Removing mg and title 
def mg_remover(mg_list):
    for i in mg_list:
        for x in i:
            i[1] = i[1][:-2:]
            del i[0]
    return mg_list

#Removes g on special case protein
def protein_remover(the_list):
    for i in the_list:
        for x in i:
            i[1] = i[1][:-1:]
            del i[0]
    return the_list

#Casting list of strings to floats
def make_float(string_list, float_list):
    string_list = np.array(string_list)
    float_list = string_list.astype(np.float)
    return float_list
#***************************************
        #USING FUNCTIONS 
#***************************************
        
#Splitting list to prepare to remove title and get number
total_fats_strings = splitter(total_fats, total_fats_strings)
sfats_strings = splitter(sfats, sfats_strings)
cholesterol_strings = splitter(cholesterol, cholesterol_strings)
sodium_strings = splitter(sodium, sodium_strings)
carbs_strings = splitter(carbs, carbs_strings)
protein_strings = splitter(protein, protein_strings)

#Remove measurement and titles leave values
gram_remover(total_fats_strings)
gram_remover(sfats_strings)
gram_remover(carbs_strings)
protein_remover(protein_strings)
mg_remover(sodium_strings)
mg_remover(cholesterol_strings)

#Changing ~ value to 0 
sfats_strings[21] = ['0']

#Casting Values as floats
calories_nums = make_float(calories, calories_nums)
total_fats_nums = make_float(total_fats_strings,total_fats_nums)
sfats_nums = make_float(sfats_strings,sfats_nums)
carbs_nums = make_float(carbs_strings,carbs_nums)
protein_nums = make_float(protein_strings,protein_nums)
sodium_nums = make_float(sodium_strings,sodium_nums)
cholesterol_nums = make_float(cholesterol_strings,cholesterol_nums)

#print(calories_nums)
#print(total_fats_nums)
#print(sfats_nums)
#print(carbs_nums)
#print(protein_nums)
#print(sodium_nums)
#print(cholesterol_nums)



#UNUSED CODE

#    printing content of page
#    print(page.content)

#    print(soup.prettify())

#    print(name.get_text())

#    print(kcal[0].get_text())

#    print(sat_fat.get_text())

        #print(in_serving[i].get_text())

#List of all nutrition facts 
#print(sfats)
#print(names)
#print(calories)
#print(total_fats)
#print(cholesterol)
#print(sodium)
#print(carbs)
#print(protein)

