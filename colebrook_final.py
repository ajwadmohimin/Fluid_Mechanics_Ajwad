#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 03:16:03 2021

@author: md.ajwadmohimin
"""
# This is a python script to calculate Darcy Friction Factor from Colebrook
# Equation. This was made actually for my assignment purpose. Here, the velociy
# was function of ID number. In the equation, except friction factor, f , everything
# was known. So, it was designed in a way that, f was guessed at first based on 
# the Re and e/D, actually from moody chart, little bit below the actual f value
# found from the chart, then the guess was gradually increased. The increment 
# was designed to be half of the difference between the guess_f and found_f. 
# Options for convergence crieteria and decimal pricision have been given. 

from math import log
from math import sqrt
roll=float(input("enter last 3 digit of your ID/roll no."))
D=(100+roll)/1000 # Diameter. In the assignment it was 100+(last 3 digit of id)
print("D ",D)
v=round(0.05*4/(3.1416*(D**2)),2) # Velocity
print("v ",v)
e_D=round(0.12/(D*1000),4) #Realtive Roughness
print("e by D=",e_D)
Re=(v*D)/(1e-6) # Reynolds Number
Re=float("%.1E"%Re)
print("Re=","%.2E" % Re)
if(Re>4000): # For Pipe flow Turbulent flow ocurs when Re<4000
    print("Turbulent Flow")
else:
    print("Laminar")

f_guess=float(input("enter friction factor guess, f_guess")) # f is friction factor
f_diff=float(1)
it=1
f_o=f_guess
#p=int(input("wanted decimal precision"))
p=16 #default decimal precision set to 16, uncomment the previous line to set
            #it on the run. DOn't forget to comment this value of p also.
#con_criteria=1e-6 #comment it to set it on the run and uncomment the below
con_criteria=float(input("enter the convergence criterion,fn+1-fn? "))

while(f_diff>=con_criteria):
    print("\niteration no ",it)
    print("f_old",f_o)
    f_n=round(1/((-2.0)*log((e_D/3.7)+(2.51/(Re*(sqrt(f_o)))),10))**2,p)
    f_diff=round(abs(f_o-f_n),p)
    print("f_diff",f_diff)
    print("friction factor,f",f_n)
    f_o+=(f_diff/2)
    it+=1
    