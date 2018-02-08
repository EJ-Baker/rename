import os, sys
import nameArray

def rename(newNames):
	for i, f in enumerate(os.listdir()):
		extention = os.path.splitext(f)[1]
		oldFile = f
		newFile = "%d%s"%(newNames[i], extention)
		os.rename(oldFile, newFile)

if __name__ == '__main__':
	os.chdir(sys.argv[1])

	nums = nameArray.int_array_random(len(os.listdir()), 10)

	rename(nums)
