import os, random

nums = list(range(len(os.listdir('test'))))
random.shuffle(nums)

for f in range(len(os.listdir('test'))):
	extention = os.path.splitext(os.listdir('test')[f])[1]
	oldFile = os.listdir('test')[f]
	newFile = "%d%s"%(nums[f], extention)
	os.rename('test/' + oldFile, 'test/' + newFile)
