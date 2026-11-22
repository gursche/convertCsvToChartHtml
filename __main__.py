# -*- coding: utf-8 -*-
#!/usr/bin/env python
""" 
version: 0.0.0

"""
import os
from tkinter import filedialog
import zipfile
import json
def main():
    file_path = os.path.realpath(__file__)
    installExample=askExample()
    installChartJsLocal=askChart()
    configCfgData=False
    configDirectories=False
    file_path='/home/arming/Projekte/7001/code/test/test.zip'
    if not os.path.isfile(file_path):
        # do not run iside of code
        pass
    else:
        # asure it's a zip
        if file_path.lower().endswith('.zip'):
            # read the archive
            thisZip=zipfile.ZipFile(file_path)
            for file in thisZip.filelist:
                path=file.filename
                b=path.split('/')
                if len(b) == 1:
                    # single Files
                    if '__' in path:
                        # no need to extract 
                        pass
                    elif path == 'convertCsvToChartHtml.py':
                        # python convertCsvToChartHtml.py
                        thisZip.extract(path)
                    elif path == 'directories.py':
                        # directory setup
                        configDirectories=handleDirectories(thisZip,path,installExample)
                    elif path == 'chartsCfg.py':
                        # chart.js
                        configCfgData=handleCfgData(thisZip,path,installExample)
                    elif 'README.MD' in path.upper():
                        # read me
                        thisZip.extract(path)
                    else:
                        print('Files not handled:',path)
                elif len(b)==2 and b[1]=='':
                    # directories
                    if path.startswith('exampleOutput'):
                        if installExample:
                            # example data
                            thisZip.extract(path)
                else:
                    # directories content
                    if path.startswith('example'):
                        # install example data
                        if installExample:
                            if path.startswith('exampleData/'):
                                # data
                                thisZip.extract(path)
                    elif path == 'helper/ChartData.py':
                        # class file
                        thisZip.extract(path)
                    elif path == 'chartJS/chart.umd.min.js':
                        if installChartJsLocal:
                            thisZip.extract(path)
                    elif path.startswith('htmlFi') and 'online' not in path:
                        # html templates
                        if path=='htmlFiles/__init__.py':
                            # dir init
                            thisZip.extract(path)
                        elif path=='htmlFiles/chartTemplate.py':
                            # chart template
                            thisZip.extract(path)
                        elif path=='htmlFiles/index.html':
                            # charts.js set local
                            if installChartJsLocal:
                                thisZip.extract(path)
                            else:
                                # set oline
                                tPath='htmlFiles/online/index.html'
                                htmlF=thisZip.read(tPath)
                                # save the extraced file 
                                f = open('htmlFiles/index.html', 'wb')
                                f.write(htmlF)
                                f.close()
                    else:
                        print('// not handled',path)


def askExample():
    """ prints description and question, 
    :returns: bool: """
    print("""
#########################################
CSV to HTML chart converter installation
_________________________________________

reads csv file, add columns from other csv files exports html, csv

read the README befor next steps
""")
    return askYN('do you want to install example data?(y/n)')


def askChart():
    """ prints description and questions, 
    :returns: bool: """
    print("""
The html file depends on 'https://www.chartjs.org/' to ensure actual version
and to run output.html everywhere type: n

Or use local version of chart.js, output.html requires chartJS/chart.umd.min.js:
to install included local version type: y

    """)
    chlocal=askYN('install chart.js localy?(y/n)')
    if chlocal:
        print("""
asure html file reaches the chart script: chartJS/chart.umd.min.js
_________________________________________

""")
    else:
        print(""" share your html with anyone
________________________________________
""")
    return chlocal


def handleDirectories(thisZip,path,installExample):
    # set Example Data 
    if installExample:
        tPath='helper/default/directoriesExample.py'
        htmlF=thisZip.read(tPath)
        f = open('directories.py', 'wb')
        f.write(htmlF)
        f.close()
        return True
    # start
    print("""
to run the script properly you need to set some folders:

    initialDir = '/home/user/myCSV/' requires initialCsvInfo={}
    optionalCsvDir='/home/user/powerProvider/' requires optionalCsvInfo={}
    destinationDir='/home/user/myOutput'

if these are not set propperly to existing folders you will get an OS error.
to handle the expected csv, a dict is required to spezify header row and data starts from row, ...

if you want to set this manually type: y
if you preffer the guided tour type: n

    """)
    manualInstall=askYN('do you want to set directories manually?(y/n)')
    if manualInstall:
        thisZip.extract(path)
    else:
        print("""

next step set default directories and values
for rows and columns start with 0
""") 
        dirDict={
            'initialDir': '',
            'optionalCsvDir':'',
            'destinationDir':'',
            'seperator':''
        }
        dirDict, dirDictInfo=askForDirectories(dirDict)
        tPath='helper/default/directories.py'
        htmlF=thisZip.read(tPath).decode("utf-8")
        hf=htmlF.split('\n')
        newLines=[]
        for line in hf:
            if line.startswith('initialDir='):
                newLine="initialDir='"+dirDict['initialDir']+"'"
                newLines.append(newLine)
            elif line.startswith('optionalCsvDir='):
                newLine="optionalCsvDir='"+dirDict['optionalCsvDir']+"'"
                newLines.append(newLine)
            elif line.startswith('destinationDir='):
                newLine="destinationDir='"+dirDict['destinationDir']+"'"
                newLines.append(newLine)
            elif line.startswith('initialCsvInfo='):
                val=json.dumps(dirDictInfo['initialDir'])
                newLine='initialCsvInfo='+val
                newLines.append(newLine)
            elif line.startswith('optionalCsvInfo='):
                val=json.dumps(dirDictInfo['optionalCsvDir'])
                newLine='optionalCsvDir='+val
                newLines.append(newLine)
            else:
                newLines.append(line)
        with open('directories.py', 'w') as f:
            f.write('\n'.join(newLines))
        return True
    return False

def handleCfgData(thisZip,path,installExample):
    
    if installExample:
        thisZip.extract(path)
    else:
        tPath='helper/default/chartsCfg.py'
        htmlF=thisZip.read(tPath)
        # save the extraced file 
        f = open('chartsCfg.py', 'wb')
        f.write(htmlF)
        f.close()

def askYN(question):
    """ prints question, gets user input
    :param: question: str
    :returns: bool: y:True|n:False
    """
    b=True
    while b:
        a=input(question)
        if a.lower()=='y':
            return True
        if a.lower()=='n':
            return False


def askNumber():
    b=True
    while b:
        a=input('only numbers ')
        try:
            c=int(a)+int(a)
            return int(a)
        except ValueError as e:
            print('Numbers only, try again')
        except e:
            print(e)

def askForDirectories(dirDict):
    ret={}
    for ind in dirDict:
        if ind == 'initialDir':
            print("""

choose folder for where to find your main csv: 
""")
            dirDict[ind]=filedialog.askdirectory()
            ret[ind]=askCsvRpwColumnDetails(ind) 
        elif ind =='optionalCsvDir':
            print("""

choose folder for where to find your optional csv: 
""")
            dirDict[ind]=filedialog.askdirectory()
            ret[ind]=askCsvRpwColumnDetails(ind)
        elif ind == 'destinationDir':
            print("""

choose folder for where to save the output files: 
""")
            dirDict[ind]=filedialog.askdirectory()
            print(dirDict[ind])
        elif ind == 'destinationDir':
            pass
    return dirDict,ret
def askCsvRpwColumnDetails(index,):
    ret={
        'columnHeaderRow':-1,
        'columnDataFromRow':-1,
        'columnDataWhereTf':-1, 
        'seperator':''  
    }
    if index == 'initialDir':
        a=input('type column seperator: ')
        ret['seperator']=a
        print('set row number for headers: ')
        ret['columnHeaderRow']=askNumber()
        print('set row number from where data starts')
        ret['columnDataFromRow']=askNumber()
    elif index == 'optionalCsvDir':
        a=input('type column seperator: ')
        ret['seperator']=a
        print('set row number for headers: ')
        ret['columnHeaderRow']=askNumber()
        print('set row number from where data starts')
        ret['columnDataFromRow']=askNumber()
        print('set column number of data to add')
        ret['columnDataWhereTf']=askNumber()
    return ret
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()