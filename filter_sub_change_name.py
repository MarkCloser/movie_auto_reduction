import re

def cleantxt(raw):
	fil = re.compile(u'[^0-9a-zA-Z\-]+', re.UNICODE)
	return fil.sub('', raw)

a = 'ABP-108 桃谷エリカ'
b = '@ABP-623愛音まりあ'
print(cleantxt(b))

