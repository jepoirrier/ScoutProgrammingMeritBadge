#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scouts Degree Converter F -> C
"""
 
#...initialize looping variable, assume 'yes' as the first answer
continueYN = "y"
 
while continueYN == "y":
   #...get temperature input from the user
   sDegreeF = input("Enter next temperature in degrees Farenheight (F):")
 
   #...convert text entry to number value that can be used in equations
   nDegreeF = int(sDegreeF)
 
   #...convert temperature from F to Celsius
   nDegreeC = (nDegreeF - 32) * 5 / 9
   
   #...check for temperature below freezing..
   if nDegreeF < 32:
      print ("Pack long underwear!")
 
   #...check for it being a hot day...
   if nDegreeF > 100:
      print ("Remember to hydrate!")
 
   print ("Temperature in degrees C is:", nDegreeC)
 
 
   continueYN = input("Input another?")
 
#exit the program