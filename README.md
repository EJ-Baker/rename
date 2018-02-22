# rename

This is a command line application designed to rename all of the files inside of a directory. I use it to rename pictures mostly. It can add prefixes and suffixes to files which is useful for tagging photos. It can rename all of the files as ints which is useful when dealing with scanned pictures. It can also randomize the order of files. I use this for slideshows that are being played on smart TVs that don’t support randomizing the picture order.
##### help message
```
usage: rename.py [-h] [-pre PREFIX] [-suf SUFFIX] [-i | -x] [-r] [-p]
                 [-o OFFSET] [-v | -q]
                 [dir]

Renames all files in a directory

positional arguments:
  dir                   the directory to rename, default cwd

optional arguments:
  -h, --help            show this help message and exit
  -pre PREFIX, -prefix PREFIX
                        a string to prepend the files
  -suf SUFFIX, -suffix SUFFIX
                        a string to append the files
  -i, -int              renames the files as a series of ints
  -x, -hex              renames the files as a series of hexes
  -r, -random           randomizes the order of the files, dependent on -i or
                        -x
  -p, -pad              pads -i or -x with zeros to keep names the same
                        length, dependent on -i or -x
  -o OFFSET, -offset OFFSET
                        adds an offset for -i or -x to start from, dependent
                        on -i or -x
  -v, -verbose          adds confirmation and dislpays information about what
                        is being renamed
  -q, -quiet            removes confirmation and information about what is
                        being renamed
```

##### examples
Adding a prefix to vacation photos
```
python rename.py C:\Users\EJ-Baker\Pictures\vacation -pre Florida_
```
Adding a suffix to tag the year for easier searching later
```
python rename.py C:\Users\EJ-Baker\Pictures\vacation -suf [2018]
```
Renaming photos for a slideshow
```
python rename.py C:\Users\EJ-Baker\Pictures\slideshow -pre Slideshow -irp
```
*This command will rename everything in the \slideshow directory a random number that is zero padded to be equal length and prefixed with "Slideshow"*
