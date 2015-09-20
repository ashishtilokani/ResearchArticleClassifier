"""
Created On: 20th Sept 2015
@author: Amitayush Thakur
"""

import subprocess
import os
PDF_TO_TEXT = '../xpdfbin-win-3.04/bin64/pdftotext.exe'
PATH_TO_DATASET = '../TrainingData/'
PDF_TO_TEXT_win = '..\\xpdfbin-win-3.04\\bin64\\pdftotext.exe'
PATH_TO_DATASET_win = '..\\TrainingData\\'

def pdfToText(path):
    subprocess.call([PDF_TO_TEXT,path])


def convertTextToPDF():
    dirList = [x for x in os.listdir(PATH_TO_DATASET)]
    files = []
    for dirName  in dirList:
        for x in os.listdir(PATH_TO_DATASET+dirName):
            if str(x)[-3:] == 'pdf':
                pathName = PATH_TO_DATASET+dirName+'/'+str(x)
                files.append(pathName)
            pdfToText(pathName)
    context = {
               'dirList':str(dirList),
               'fileList':str(files)
               }
    return context

def __main__():
    #pdfToText(PATH_TO_DATASET+'PhysicsMathematics\\'+'PhysRevLett.105.136805.pdf')
    print(str(convertTextToPDF()))

__main__()