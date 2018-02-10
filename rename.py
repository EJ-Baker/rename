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
	parser.add_argument('dir', default = '', help = 'the directory to rename, default cwd')
	parser.add_argument('-p', '-prefix', nargs = 1, default = '', help = 'a string to prepend the files', metavar = 'PREFIX')
	parser.add_argument('-s', '-suffix', nargs = 1, default = '', help = 'a string to append the files', metavar = 'SUFFIX')
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-i', '-int', action = 'store_true', help = 'renames the files as a series of ints')
	group.add_argument('-x', '-hex', action = 'store_true', help = 'renames the files as a series of hexes')
	args = parser.parse_args()
