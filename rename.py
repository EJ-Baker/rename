import os
import nameArray

nums = nameArray.int_array_random(len(os.listdir('test')))

def rename(newNames):
	for i, f in enumerate(os.listdir('test')):
		extention = os.path.splitext(f)[1]
		oldFile = f
		newFile = "%d%s"%(newNames[i], extention)
		os.rename('test/' + oldFile, 'test/' + newFile)

rename(nums)
