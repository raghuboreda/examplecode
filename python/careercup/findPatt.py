import os
import fnmatch

def find( pattern ):
   #matches = []
   pkgsToSearch = ['Dos','DosSystem','DosSystemBase','DosStrata','Diags']
   for pkg in pkgsToSearch:
      startdir = '/src/' + 'pkg'
      for root, dirs, files in os.walk( startdir, findvisitor, (matches, pattern)):
         for file in files:
            print file
   return 'found'


if __name__ == '__main__':
    import sys
    namepattern = sys.argv[1] 
    for name in find(namepattern): print name