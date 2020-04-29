##########################################################
#Author: Jessica Devine
#Date: 1/27/2020
#This is 1 of HW1
#########################################################
#Give instructions to the user to input values
print("Enter the following quantities in feet.")
#define the variable r for the length of the row
r= int(input("  How long is this row? "))
#define the variable e for the amount of space, which, like the variable r, should be entered in feet
e = int(float(input("  How wide is the end-post assembly? ")))
#define the variable s for the space between vines, also in feet
s= int(input("  How much space should be between the vines? "))
#calculate the number of grapevines that will fit in the row
v = (r -2*e)/s
#Print to the user the number of vines for which there is space in the row
print("\nThis row has enough space for", int(v), "vine(s).")


