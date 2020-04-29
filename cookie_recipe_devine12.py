##########################################################
#Author: Jessica Devine
#Date: 1/27/2020
#This is 3 of HW1
#########################################################
#Ask the user how many cookies he or she would like to make
c = float(input("How many cookies do you want to make? "))
#enter the variables to determine the amount of ingredients per the recipe
#define amount of sugar needed in cups
s =(1.5/48)*c
#define amount of butter needed in cups
b= c/48
#define amount of flour needed in cups
f= c*(2.75/48)
#Print results for the user
print("To make", int(c), "cookies, you will need:\n  ", format(s, '.2f'), "cups of sugar\n  ", format(b, '.2f'), "cups of butter\n  ", format(f, '.2f'), "cups of flour")
        
