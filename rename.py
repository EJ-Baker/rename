import os, random

nums = list(range(len(os.listdir('test'))))
random.shuffle(nums)

for i, f in enumerate(os.listdir('test')):
	extention = os.path.splitext(f)[1]
	oldFile = f
	newFile = "%d%s"%(nums[i], extention)
	os.rename('test/' + oldFile, 'test/' + newFile)
