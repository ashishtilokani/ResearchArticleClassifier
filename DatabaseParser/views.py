"""
Created On: 20th Sept 2015
@author: Amitayush Thakur,Jaiwant Rawat,Ashish Tilokani
"""

from DatabaseParser.models import WordTable, DocFreqTable, DocClass
import os

# Create your views here.
PATH_TO_DATASET = '../TrainingData/'
MAX_NUM_OF_WORDS_READ = 3

def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char

def get_my_string(file_path):
    s = ""
    l = len(file_path)
    i = 0
    while i < l:
        s += onlyascii(file_path[i])
        i += 1
    s = s.lower()
    return s

def parseTextToDb(fileList):
    #logic for counting and reading the text file
    for file in fileList:
        fileToken = file.split('/')
        if len(DocClass.objects.filter(className = fileToken[1],docName=fileToken[2])) != 0:
            continue
        DocClass.objects.create(className = fileToken[1],docName=fileToken[2])
        fp = open(file,encoding="latin-1")
        wordList = fp.read().split()
        cnt = 0
        for word in wordList:
            word = get_my_string(word)
            print(word)
            if len(WordTable.objects.filter(word=word,docName = fileToken[2]))== 0 :
                WordTable.objects.create(word = word,docName = fileToken[2],freq = 1)
                if len(DocFreqTable.objects.filter(word=word))==0:
                    DocFreqTable.objects.create(word=word,docFreq = 1)
                else:
                    docIns = DocFreqTable.objects.filter(word=word)[0]
                    docIns.docFreq += 1
                    docIns.save()
            else:
                wordIns = WordTable.objects.filter(word=word,docName = fileToken[2])[0]
                wordIns.freq += 1
                wordIns.save()
            cnt += 1
            if cnt==NUM_OF_WORDS:
                break
                
def __main__():
    dirList = [x for x in os.listdir(PATH_TO_DATASET)]
    files = []
    for dirName  in dirList:
        for x in os.listdir(PATH_TO_DATASET+dirName):
            if str(x)[-3:]== 'txt':
                pathName = PATH_TO_DATASET+dirName+'/'+str(x)
                files.append(pathName)
    parseTextToDb(files)

#__main__()
