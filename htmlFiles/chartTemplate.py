# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
:author:        gursche.xyz
function:       no function
returns:        templateCanvas:str, templateChartStart:str, templateChartEnd:str
description:    templates for ChartData 
settings:       templateCanvas: html and styling 
requiredBy:     ChartData.writeHtmlFile()
scripts:        templateChartStart, templateChartEnd
"""
templateChartTitle='<div style="width:100%;"><h1>MyTitle</h1></div>'
# do not change <canvas id="myChart">
templateCanvas='<div style="width:70%;margin:auto;"><canvas id="myChart"></canvas></div>'
# script: js template
templateChartStart='<script>  const ctx = document.getElementById("myChart"); new Chart(ctx, { data: {'
templateChartEnd='})</script>'
def main():
    pass
if __name__ == '__main__':
    main()