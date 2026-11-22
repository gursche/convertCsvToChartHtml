# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
:author:        gursche.xyz
function:       chartCFG() 
returns:        charts:[{title:str,'columns':[],'columnsType':['bar','line'],'options':{}}]
description:    configuration file for ChartData 
settings:       define charts, make sure columns and columnsType are same lenght, for columns ids use ChartData.printHeader()
usage:          from chartsCfg import chartCFG, ChartData.importCFG(chartCFG())
requiredBy:     ChartData.importCFG(chartCFG())
presetOptions:  Chart Options ''
- default:    'options': ', options: { scales: { y: { beginAtZero: true }}, plugins: { title: { display: true, text: "ChartTitle" } } } '
- stacked:    'options': ', options: { scales: { y: { beginAtZero: true, stacked: true }, x: { stacked: true }}, plugins: { title: { display: true, text: "ChartTitle" } } } '

"""
charts=[]
# define chart
chart={
    'title':'PV Erzeugung',
    # 5:    'Gesamte Solarstromerzeugung (kWh)'
    # 5 Gesamte Solarstromerzeugung (kWh) 
    # 12:   'PV1-Erzeugung (kWh)',
    # 13:   'PV2-Erzeugung (kWh)', 
    # 14:   'PV3-Erzeugung (kWh)',
    # 15:   'PV4-Erzeugung (kWh)', 
    # 10:   'Speicher zu Haushalt (kWh)'
    # 11:   'Speicher-Einspeisung (kWh)'
    # 22:   'Freie Energie (Off-Grid) (kWh)'
    'columns':[5,12,13,14,15,10,11,22],
    'columnsType':['bar','line','line','line','line','line','line','line'],
    # options stacked: values on top of eachother 
    'options': ', options: { scales: { y: { beginAtZero: true, stacked: true }, x: { stacked: true }}, plugins: { title: { display: true, text: "ChartTitle" } } } '
}
# add chart to charts
if len(chart['columns']) == len(chart['columnsType']):
    charts.append(chart)
else:
    print(chart['title'],'not added -> columns: ',len(chart['columns']),' columnsType: ',len(chart['columnsType']))
#end define chart
# next chart
chart={
    'title':'Erzeugung - Verbrauch',
    #  5:    'Gesamte Solarstromerzeugung (kWh)'
    # 19:   'Verbrauch über Smart Plug (kWh)'
    #  8:    'Solarstrom-Einspeisung (kWh)'
    #  7:    'Solarstrom zu Speicher (kWh)'
    # 11:   'Speicher-Einspeisung (kWh)' 
    # 22:   'Freie Energie (Off-Grid) (kWh)'
    # 24:   'kelag'
    #  6:    'Solarstrom zu Haushalt (kWh)' 
    # 25: 'Kelag Vorjahr'
    'columns':[5,24, 8, 7, 11, 22, 19,  6,25],
    'columnsType':['line', 'line', 'bar', 'bar', 'bar','line', 'line', 'bar','line'],
    # options: not stacked
    'options': ', options: { scales: { y: { beginAtZero: true }}, plugins: { title: { display: true, text: "ChartTitle" } } } '
}
# add chart to charts
if len(chart['columns']) == len(chart['columnsType']):
    charts.append(chart)
else:
    print(chart['title'],'not added -> columns: ',len(chart['columns']),' columnsType: ',len(chart['columnsType']))
# next chart
chart={
    'title':'Speichernutzung',
    # 16:   'Speicherladung (kWh)'
    # 9:    'Speicherentladung (kWh)'
    # 7:    'Solarstrom zu Speicher (kWh)'
    # 11:   'Speicher-Einspeisung (kWh)'
    # 10:   'Speicher zu Haushalt (kWh)'
    # 4:    'Netzstrom zu Speicher (kWh)'
    'columns':[16,9,7,11,10,4],
    'columnsType':['bar','bar','line','line','line','line'],
    # options stacked: values on top of eachother 
    'options': ', options: { scales: { y: { beginAtZero: true, stacked: true }, x: { stacked: true }}, plugins: { title: { display: true, text: "ChartTitle" } } } '    
}
# add chart to charts
if len(chart['columns']) == len(chart['columnsType']):
    charts.append(chart)

else:
    print(chart['title'],'not added -> columns: ',len(chart['columns']),' columnsType: ',len(chart['columnsType']))
# next chart
# ...


def chartCFG():
    """ Charts as list
    return: charts:[{title:str,'columns':[],'columnsType':[],'options':{}}]
    """
    return charts

def main():
    pass

if __name__ == '__main__':
    main()