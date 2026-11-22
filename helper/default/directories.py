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
initialDir=''
destinationDir=''
optionalCsvDir=''
initialCsvInfo={ 'columnHeaderRow':-1, 'columnDataFromRow':-1, 'columnDataWhereTf':-1, 'seperator':'' }
optionalCsvInfo={'columnHeaderRow':-1, 'columnDataFromRow':-1, 'columnDataWhereTf':-1, 'seperator':'' }