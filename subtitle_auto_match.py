import os
import shutil
import json

# 获取脚本的绝对路径
absPath = os.path.dirname(os.path.abspath(__file__))

# 加载 JSON 文件
def loadConfig():
    jsonFile = open("config.json", encoding='utf-8')
    return json.load(jsonFile)

# 遍历获取文件路径
def getFilesPath(rootDirPath):
    for home, dirs, files in os.walk(rootDirPath):
        for dir in dirs:
            if '-' in dir:
                for root, subDirs, subFiles in os.walk(absPath + '/subtitle'):
                    for subFile in subFiles:
                        itemOne = subFile.split('.')[0].split('_')
                        intemTwo = subFile.split('.')[0].split('-')
                        if len(itemOne) == 2:
                            subName = itemOne[0].upper() +'-'+ itemOne[1]
                            if subName == dir:
                                shutil.move(root +'/'+ subFile, home +'/'+ dir)
                                os.rename(home +'/'+ dir +'/'+ subFile, home +'/'+ dir +'/'+ subFile.split('.')[0].upper() +'.'+ subFile.split('.')[1])
                        if len(intemTwo) == 2:
                            subName = intemTwo[0].upper() +'-'+ intemTwo[1]
                            if subName == dir:
                                shutil.move(root +'/'+ subFile, home +'/'+ dir)
                                os.rename(home +'/'+ dir +'/'+ subFile, home +'/'+ dir +'/'+ subFile.split('.')[0].upper() +'.'+ subFile.split('.')[1])

getFilesPath(absPath + '/movies')

