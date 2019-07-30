#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:28:50 2019
@author: merrickcampbell
"""
#==============================================================================
# Derivative of RODEO2, modified just to count the number of sequence motifs
# for Chayanid Ongpipattanakul
#==============================================================================
# Copyright (C) 2017 Bryce L. Kille
# University of Illinois
# Department of Chemistry
#
# Copyright (C) 2017 Christopher J. Schwalen
# University of Illinois
# Department of Chemistry
#
# Copyright (C) 2017 Douglas A. Mitchell
# University of Illinois
# Department of Chemistry
#
# License: GNU Affero General Public License v3 or later
# Complete license availabel in the accompanying LICENSE.txt.
# or <http://www.gnu.org/licenses/>.
#
# This file is part of RODEO2.
#
# RODEO2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RODEO2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
#==============================================================================
# Special thanks goes to AntiSmash team, whose antiSMASH-rodeo repository at
# https://bitbucket.org/mmedema/antismash-rodeo/ provided the backbone code for 
# a great deal of the heuristic calculations.
#==============================================================================

import re

class Ripp:
    def __init__(self):
        #Set Counter
        self.countY = 0
        self.countW = 0
        self.countE = 0                
                
    def count_sequence(self, sequence):
        # Count Y
        matches = re.findall("(Y..P)", sequence)
        #print(matches)
        self.countY += len(matches)            
        #print(self.countY)
        
        # Count W
        matches = re.findall("(W..P)", sequence)
        #print(matches)
        self.countW += len(matches)            
        #print(self.countW)        
        
        # Count E
        matches = re.findall("(E..P)", sequence)
        #print(matches)
        self.countE += len(matches)            
        #print(self.countE)

file = open("countedfile.txt","r")

# myRipp.sequence = "YAAPALAAAGAAAAATYAAPALAAAGBBBBBTYCCPCLCACGDDDDDT"
myRipp = Ripp()

for line in file: 
	if '>' in line: 
		continue 
	else: 
#		line = myRipp = Ripp(-1,-1,'FOO','BAR',-1)
		myRipp.count_sequence(line)
print(myRipp.countY, myRipp.countW, myRipp.countE)