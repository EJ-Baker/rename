import os, sys
import nameArray

def rename(newNames, prefix, suffix):
	for i, f in enumerate(os.listdir()):
		extention = os.path.splitext(f)[1]
		oldFile = f
		newFile = "{}{}{}".format(prefix, newNames[i], suffix)
		os.rename(oldFile, newFile)

if __name__ == '__main__':
	os.chdir(sys.argv[1])
	prefix = sys.argv[2]
	suffix = sys.argv[3]

	nums = nameArray.hex_array_random_padded(len(os.listdir()), 7)

	rename(nums, prefix, suffix)
