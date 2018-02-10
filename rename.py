import os, sys, argparse
import nameArray

def rename(newNames, prefix, suffix):
	for i, f in enumerate(os.listdir()):
		extention = os.path.splitext(f)[1]
		oldFile = f
		newFile = "{}{}{}".format(prefix, newNames[i], suffix)
		os.rename(oldFile, newFile)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "Renames all files in a directory")
	parser.print_help()
