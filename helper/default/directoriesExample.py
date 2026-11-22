# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
:author:        gursche.xyz
function:       none
returns:        initialDir, destinationDir, optionalCsvDir
description:    configuration file for helper/ChartData
settings:       define directories to use
usage:          from directories import initialDir, destinationDir, optionalCsvDir
requiredBy:     helper/ChartData.py in /
"""
initialDir='exampleData/anker/'
destinationDir='exampleOutput/'
optionalCsvDir='exampleData/kelag/'
initialCsvInfo={
        'columnHeaderRow':1,
        'columnDataFromRow':2,
        'columnDataWhereTf':-1, 
        'seperator':',' 
        }

optionalCsvInfo={
        'columnHeaderRow':8,
        'columnDataFromRow':9,
        'columnDataWhereTf':3, 
        'seperator':'' 
    }