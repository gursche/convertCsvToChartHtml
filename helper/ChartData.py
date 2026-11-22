# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
:author: gursche.xyz
:description: reads export .csv files, adds spezific column from other csv - checks column[0] before adding to ChartData, creates .html with charts or csv export
:converts: Anker data export csv to easy import csv (01/12/2026 -> 01.12.2026, 0.00 -> 0,00)
:adds: ChartData Anker App Data + power provider Data
:creates: html file with configurable charts
:configuration: chartCfg.py: define columns to put on chart 'columns':[], 
    select bar or line for each column 'columnsType':[], 
    set optopns like values stacked or not 'options': https://www.chartjs.org/docs/latest/general/options.html
    make html changes in /html/index.html | chartTemplate.py, 
"""
import os
import tkinter.filedialog as tkfd
import pkgutil
import json
from htmlFiles.chartTemplate import templateCanvas, templateChartStart, templateChartEnd, templateChartTitle

def main():
    pass

class ChartData:
    """
    ChartData(name) sets name and language
    :param name: str on startImport() name is rearranged if _Energiedetails_,_Energy_Details_ found
    :param language: de -> 01/12/2026 to 01.12.2026, 0.00 to 0,00 | en -> no changes
    :param description: reads csv and creates charts in html file, using chart.js
        made to read energy production values from Anker App and show data in chart 
    """
    def __init__(self, name, language:'en'):
        self.titel=name
        self.test=False
        self.language=language
        self.columnHeader=[]
        self.labels=[]
        self.data=[]
        self.chartData=[]
        self.cfg={}
        self.canvasArray=[]
        self.scriptArray=[]
        self.charts=[]
        self.initialDir=''
        self.destinationDir=''
        self.csvPathToSave=''
        self.htmlPathToSave=''
        self.initialCsvInfo={
            'columnHeaderRow':-1,
            'columnDataFromRow':-1,
            'columnDataWhereTf':-1, # not in use,
            'seperator':''
            }
        self.optionalCsvInfo={
            'columnHeaderRow':-1,
            'columnDataFromRow':-1,
            'columnDataWhereTf':-1,
            'seperator':''
            }


    def setTest(self,test=False):
        # @todo
        self.test=test


    def startImport(self, initialDir, destinationDir, initialCsvInfo):
        """
        startImport(initialDir, destinationDir, initialCsvInfo)
        :param initialDir: path to data export csv directory
        :param destinationDir: path to save files
        :param initialCsvInfo: self.initialCsvInfo with correct values
        :param result: ChartData filled with main content
        :param description: checks if directories exist, asks for file to select, changes name, starts addDataFromCSV()
        :param OSError: directories not valid 
        """
        if os.path.isdir(initialDir):
            self.initialDir=initialDir
        if os.path.isdir(destinationDir):
            self.destinationDir=destinationDir
        if self.initialDir=='' or self.destinationDir=='':
            if not self.test:
                raise OSError('initialDir or destinationDir, set in directories.py')
        # get user input
        a=True
        while a:
            if self.test:
                print('test initialDir',initialDir)
                pathToFile=initialDir
            else:
                pathToFile=tkfd.askopenfilename(initialdir=self.initialDir)
            if pathToFile[-4:].lower()=='.csv':
                print('selected File:',pathToFile)
                a=False
            else:
                print('select csv file')
        newF=pathToFile.split('/')
        #set path
        self.csvPathToSave=os.path.join(self.destinationDir, newF[len(newF)-1])
        # create chart object
        # define name from given file
        name=newF[len(newF)-1].replace('.csv','')
        # change to from to first
        # older app version
        nameA=name.split('_Energy_Details_')
        # language 'de'
        # since app update to version 3.24.2
        if len(nameA)==1:
            nameA=name.split('_Energiedetails_')
        # replace _ from string
        na=nameA[1].replace('_',' ')
        nb=nameA[0]
        # recreate name
        name=na+' - '+nb
        self.titel=name
        self.addDataFromCSV(pathToFile,initialCsvInfo)

        
    def setHeader(self,columns:list):
        """ set column names
        :param: columns: [], 
        """
        for ind in columns:
            self.columnHeader.append(ind)


    def printHeader(self):
        """prints column header with id
        :param description: id for chartCfg.py  _"""
        i=-1
        for ind in self.columnHeader:
            i+=1
            print(i,ind)


    def appendLabel(self, d:str):
        """ append Lable for x axis
        :param: d: string, 
        """
        self.labels.append(d)

    def getLabels(self):
        """ 
        :return: labels from x axsis
        """
        return self.labels


    def addDataFromCSV(self,pathToFile,initialCsvInfo):
        """ Fills data with values
        :param pathToFile: str, absolute path to csv file for reading
        :param columnHeaderRow: int
        :param columnDataFromRow: int 
        :param description: reads .csv, fills self.data with values _
        """
        newFile=[]
        newColumns={}
        with open(pathToFile, mode='r', encoding='utf-8-sig') as fp:
            i=-1
            for line in fp:
                i+=1
                if i == initialCsvInfo['columnHeaderRow']:
                    line=line.replace('\n','')
                    #cut in columns
                    column=line.split(initialCsvInfo['seperator'])
                    # set column header names
                    self.setHeader(column)
                    k=-1
                    for val in column:
                        k+=1
                        newColumns[k]=[]
                elif i >= initialCsvInfo['columnDataFromRow']:
                    # data lines
                    column=line.split(initialCsvInfo['seperator'])
                    # cut date from columns, change date from / to .
                    # create self.labels, append data
                    newRow=[]
                    j=-1
                    for item in column:
                        j+=1
                        if j==0:
                            # column: datum
                            if self.language=='en':
                                datum=item
                            elif self.language=='de':
                                datum=item.replace('/','.')
                            self.appendLabel(datum)
                            newColumns[j].append(datum)
                        elif j==len(column)-1:
                                # last column: end, convert and add
                                item=item.replace('\n','')
                                newRow.append(item)
                                newColumns[j].append(item)
                        else:
                            # line: all in between
                            newRow.append(item)
                            newColumns[j].append(item)
                        # append data line
                    self.data.append(newRow)
                    self.chartData=newColumns
                    # first line definition, no relevant data
                    pass
                else:
                    # handle other lines
                    pass
        pass


    def addAditionalCsv(self,optionalCsvDir,headerName,optionalCsvInfo):
        """ Fills data with values, adds header
        :param optionalCsvDir: str, path to additional csv directory
        :param headerName: str, name on chart
        :param optionalCsvInfo: self.optionalCsvInfo
        :param description: reads csv adds spezific column to self.columnHeader and self.data _
        """
        a=True
        while a:
            if self.test:
                print('test optionalCsvDir', optionalCsvDir)
                pathToFile=optionalCsvDir
            else:
                pathToFile=tkfd.askopenfilename(initialdir=optionalCsvDir)
            if pathToFile[-4:].lower()=='.csv':
                print('selected File:',pathToFile)
                a=False
            else:
                print('select csv file')
        powerProviderData=[]
        # optional
        powerProviderColumns=[]
        with open(pathToFile, mode='r', encoding='utf-8-sig') as fp:
            i=-1
            for line in fp:
                line=line.replace('\n','')
                i+=1
                if i == optionalCsvInfo['columnHeaderRow']:
                    # column header, optional if needed
                    columns=line.split(optionalCsvInfo['seperator'])
                    for val in columns:
                        powerProviderColumns.append(val)
                    pass
                elif i >=optionalCsvInfo['columnDataFromRow']:
                    values=line.split(optionalCsvInfo['seperator'])
                    # print(values)
                    # values[0]: date
                    # values[1]: time
                    # values[2]: value
                    # values[3]: description
                    # check if date in labels
                    date=values[0]
                    if date in self.labels:
                        # replace: 0,00 -> 0.00
                        powerProviderData.append(values[optionalCsvInfo['columnDataWhereTf']].replace(',','.'))
                    elif '.' in date:
                        for val in self.labels:
                            if date[:-2] in val:
                                # yyy - no last digit: enable previous years
                                powerProviderData.append(values[optionalCsvInfo['columnDataWhereTf']].replace(',','.'))
                    else:
                        # data not required as no dataset to compare with
                        pass
        # add to header
        self.columnHeader.append(headerName)
        self.chartData[len(self.chartData)]=powerProviderData
        # optional add powerProviderColumns
        # add to data
        j=-1
        for i in powerProviderData:
            j+=1
            self.data[j].append(i)
        pass


    def importCFG(self,cfg:dict):
        """gets chart cfg an runns import
        :param: dict cfg: run chartCFG() from chartsCfg.py
        :param result: prepares for html output
        """
        self.cfg=cfg
        # self.createChartData()
        self.runImportedCfg()

    def runImportedCfg(self):
        """
        @todo: 
        """
        ret=''
        c=-1
        for i in self.cfg:
            c+=1
            j=-1
            # add myTitle and canvas
            canvasName=i['title'].replace(' ', '')
            self.canvasArray.append(templateChartTitle.replace('MyTitle',i['title']))
            self.canvasArray.append(templateCanvas.replace('myChart',canvasName))
            # add script
            t0=templateChartStart.replace('ctx','ctx'+str(c))
            t0=t0.replace('myChart',canvasName)
            a=json.dumps(self.labels)
            # add labels
            t1='labels: '+a+','
            t1+='datasets:['
            for ind in i['columns']:
                j+=1
                if not ind in self.chartData.keys():
                    no=ind
                else:
                    a=json.dumps(self.chartData[ind])
                    t1+='  {type: "'+i['columnsType'][j]+'", label: "'+self.columnHeader[ind]+'", data:'+a+'},'
            t1=t1[:len(ret)-1]
            t1+=']}'
            #print(i['options'])
            t0+=t1+i['options'].replace('ChartTitle',i['title'])+templateChartEnd
            self.scriptArray.append(t0)

    def writeCsv(self):
        """
        @todo: 
        """
        line=''
        lines=[]
        linesHelper=[]
        # get headers and data[]
        for i in self.columnHeader:
            line+=i+'|'
        lines.append(line)
        # mix with labels with data
        j=-1
        for i in self.getLabels():
            j+=1
            line=''
            line+=i+'|'
            c=-1
            for ind in self.columnHeader:
                c+=1
                cc=-1
                for index in self.data[j]:
                    cc+=1
                    if c==cc:
                        if self.language=='de':
                            index=index.replace(".",",")
                        line+=index+'|'
            lines.append(line)
        # write to file
        with open(self.csvPathToSave, 'w') as f:
            f.write('\n'.join(lines))
        print('file saved:',self.csvPathToSave)

    def writeHtmlFile(self):
        """
        @todo: 
        """
        # get index.html template
        data=''
        with open('./htmlFiles/index.html', 'r') as file:
            data = file.read()
        # data = pkgutil.get_data('.html', 'index.html').decode("utf-8")
        xData=data.split('\n')
        indexHtml={'part0':[],'title':'','part1':[],'canvas':[],'script':[],'part2':[]}
        switchParts=0
        for line in xData:
            line=line.replace('\n','')
            if '<title>' in line:
                switchParts=1
            elif '/favicon.ico' in line:
                switchParts=2
            elif '<chartTemplate />' in line:
                switchParts=2
            elif '<scriptTemplate />' in line:
                switchParts=3
            elif switchParts==3:
                indexHtml['part2'].append(line)
            elif switchParts==1:
                indexHtml['part1'].append(line)
            elif switchParts==0:
                indexHtml['part0'].append(line)
        # mix template with data -> write to file
        self.htmlPathToSave=os.path.join(self.destinationDir,self.titel+'.html')
        with open(self.htmlPathToSave, 'w') as f:
            for ind in indexHtml:
                if ind == 'title':
                    line='<title>'+self.titel+'</title>'+'\n'
                    f.write(line)
                elif ind == 'canvas':
                    for canI in self.canvasArray:
                        line=canI+'\n'
                        f.write(line)
                elif ind == 'script':
                    for scrI in self.scriptArray:
                        line=scrI+'\n'
                        f.write(line)
                else:
                    for inde in indexHtml[ind]: 
                        line=inde+'\n'
                        f.write(line)
        print('file saved:',self.htmlPathToSave)

if __name__ == '__main__':
    main()