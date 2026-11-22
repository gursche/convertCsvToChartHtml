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
    # set title
    'title':'',
    # set column: numbers
    'columns':[],
    # set type: 'bar','line'
    'columnsType':[],
    # options stacked: values on top of eachother 
    'options': ', options: { scales: { y: { beginAtZero: true, stacked: true }, x: { stacked: true }}, plugins: { title: { display: true, text: "ChartTitle" } } } '
    # options: not stacked
    #'options': ', options: { scales: { y: { beginAtZero: true }}, plugins: { title: { display: true, text: "ChartTitle" } } } '
}
# add chart to charts
if len(chart['columns']) == len(chart['columnsType']):
    charts.append(chart)
else:
    print(chart['title'],'not added -> columns: ',len(chart['columns']),' columnsType: ',len(chart['columnsType']))
#end define chart
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