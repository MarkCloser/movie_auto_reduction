import os
import shutil
import json

# 获取脚本的绝对路径
absPath = os.path.dirname(os.path.abspath(__file__))

# 加载 JSON 文件
def loadConfig():
    jsonFile = open("config.json", encoding='utf-8')
    return json.load(jsonFile)

# 过滤需要的格式
def formatSelect(name):
    if name == '.mp4' or name == '.avi' or name == '.mkv':
        return True

# 遍历获取文件路径
def getFilesPath(rootDirPath):
    fileList = []
    for home, dirs, files in os.walk(rootDirPath):
        for fileName in files:
            if formatSelect(os.path.splitext(fileName)[1]) == True:
                fileList.append(os.path.join(home, fileName))
    return fileList
    
# 加载配置文件
configJson = loadConfig()

# 遍历指定文件目录下所有的子文件，筛选将所有的指定格式的视频文件移动到指定文件夹下
for itemFilePath in getFilesPath(absPath +'/'+ configJson['moveMovie']['rootDirPath']):
    shutil.move(itemFilePath, absPath +'/'+ configJson['moveMovie']['targetDirPath'])
  

    
    

        



