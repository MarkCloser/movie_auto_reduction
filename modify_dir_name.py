# 去除文件名中高频且和视频无关的字符

import os
import json
import re

# 获取脚本的绝对路径
absPath = os.path.dirname(os.path.abspath(__file__))

# 加载 JSON 文件
def loadConfig():
    jsonFile = open("config.json", encoding='utf-8')
    return json.load(jsonFile)

# 判断是否有关键词并处理关键词
def filtedName(name):
	if '[pixiv]' in name:
    		return re.sub(r'[\[pixiv\]]', '', name)
	if '[Pixiv]' in name:
		return re.sub(r'[\[Pixiv\]]', '', name)
	if '[真人漫画]' in name:
		return re.sub(r'[\[真人漫画\]]', '', name)
	if ' ' in name:
		return re.sub(r' ', '', name)

# 判断是否为文件夹并返回文件夹路径
def modify(checkPath):
	for category in os.listdir(checkPath):
		if os.path.isdir(os.path.join(checkPath, category)) == True:
			newDirName = filtedName(category)
			if newDirName:
				os.rename(os.path.join(checkPath, category), os.path.join(checkPath, newDirName))
			#dirPathList.append(os.path.join(checkPath, category))

# 加载配置文件
configJson = loadConfig()
rootDirPath = absPath +'/' + configJson["modifyMovieName"]["rootDirPath"]

modify(rootDirPath)
