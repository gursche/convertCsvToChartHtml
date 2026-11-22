# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
:author: gursche.xyz
:description: reads data export .csv, adds spezific column from optional .csv to ChartData
:converts: csv to easy import csv for local language german - deutsch (01/12/2026 -> 01.12.2026, 0.00 -> 0,00)
:adds: adds sezific column from additional .csv
:creates: converted csv including added columns, html file with charts
:settings: goto settings:   

"""
def main():
    from helper.ChartData import ChartData

    # settings:
    #   set directories and csvInfo in in file: directories.py
    from directories import initialDir, destinationDir, optionalCsvDir, initialCsvInfo, optionalCsvInfo
    #   set charts in file: chartsCfg.py
    from chartsCfg import chartCFG
    #   for HTML/CSS/JS changes: /html/index.html, html/chartTemplate.py
    # end settings

    # language default: 'en' -> ChartData('')
    MyCharts=ChartData('',language='de')
    
    print("Wähle Anker App Export Csv")
    MyCharts.startImport(initialDir, destinationDir, initialCsvInfo)

    # add provider export csv for same period
    print("wähle Kelag Export csv")
    header='Kelag'
    MyCharts.addAditionalCsv(optionalCsvDir,header,optionalCsvInfo)

    print("wähle Kelag Export vom Vorjahr csv")
    # add provider export csv for same period previous year
    header='Kelag Vorjahr'
    MyCharts.addAditionalCsv(optionalCsvDir,header,optionalCsvInfo)
    
    # --
    # uncomment to see id and name for setting 'columns' in chartsCfg.py
    # MyCharts.printHeader()
    # --

    MyCharts.writeCsv()
    # import chartCFG and prepare data
    MyCharts.importCFG(chartCFG())
    # write html file
    MyCharts.writeHtmlFile()

if __name__ == '__main__':
    main()