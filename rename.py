import os, sys, argparse
import nameArray

def rename(prefix, suffix, newNames = None):
	if newNames != None:
		for i, f in enumerate(os.listdir()):
			extention = os.path.splitext(f)[1]
			oldFile = f
			newFile = "{}{}{}".format(prefix, newNames[i], suffix)
			os.rename(oldFile, newFile)
	else:
		for f in os.listdir():
			extention = os.path.splitext(f)[1]
			oldFile = f
			newFile = "{}{}{}".format(prefix, oldFile, suffix)
			os.rename(oldFile, newFile)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "Renames all files in a directory")
	parser.add_argument('dir', nargs = '?', default = os.getcwd(), help = 'the directory to rename, default cwd')
	parser.add_argument('-pre', '-prefix', default = '', help = 'a string to prepend the files', metavar = 'PREFIX')
	parser.add_argument('-suf', '-suffix', default = '', help = 'a string to append the files', metavar = 'SUFFIX')

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-i', '-int', action = 'store_true', help = 'renames the files as a series of ints')
	group.add_argument('-x', '-hex', action = 'store_true', help = 'renames the files as a series of hexes')

	parser.add_argument('-r', '-random', action = 'store_true', help = 'randomizes the order of the files, dependent on -i or -x')
	parser.add_argument('-p', '-pad', action = 'store_true',
		help = 'pads -i or -x with zeros to keep names the same length, dependent on -i or -x')
	parser.add_argument('-o', '-offset', default = 0, type = int,
		help = 'adds an offset for -i or -x to start from, dependent on -i or -x', metavar = 'OFFSET')

	group2 = parser.add_mutually_exclusive_group()
	group2.add_argument('-v', '-verbose', action = 'count', default = 1,
		help = 'adds confirmation and dislpays information about what is being renamed')
	group2.add_argument('-q', '-quiet', action = 'store_true',
		help = 'removes confirmation and information about what is being renamed')

	args = parser.parse_args()

	if not (args.i or args.x) and (args.r or args.p or args.o):
		parser.error('-r -p -o are dependent on -i or -x')
	if not (args.o >= 0):
		parser.error('-o must be a positive int')

	names = None
	size = len(os.listdir(args.dir))
	offset = args.o
	if args.i:
		if args.r and args.p:
			names = nameArray.int_array_random_padded(size, offset)
		elif args.r:
			names = nameArray.int_array_random(size, offset)
		elif args.p:
			names = nameArray.int_array_padded(size, offset)
		else:
			names = nameArray.int_array(size, offset)
	elif args.x:
		if args.r and args.p:
			names = nameArray.hex_array_random_padded(size, offset)
		elif args.r:
			names = nameArray.hex_array_random(size, offset)
		elif args.p:
			names = nameArray.hex_array_padded(size, offset)
		else:
			names = nameArray.hex_array(size, offset)

	os.chdir(args.dir)
	rename(args.pre, args.suf, names)
