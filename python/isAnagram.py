def isAnagram( a=None, b=None ):
   charA = {}
   charB = {}
   if len(a) != len(b):
      print a, b, 'are not anagrams'
      return 1
   for c in a:
      if c in charA:
         charA[c] = charA[c] + 1
      else:
         charA[c] = 1
   for c in b:
      if c in charB:
         charB[c] = charB[c] + 1
      else:
         charB[c] = 1
   for c in charA:
      if c not in charB or charB[c] != charA[c]:
         print a, b, 'are not anagrams'
         return 1
   print a, b, 'are anagrams'
   return 0

k = isAnagram( a='Hero', b='oreH' )
k = isAnagram( a='swiss', b='ssswi' )
k = isAnagram( a='ero', b='oren' )
k = isAnagram( a='gero', b='oreg' )
k = isAnagram( a='gero', b='oreh' )
k = isAnagram( a='eero', b='oree' )
k = isAnagram( a='liberalism', b='imsalleirb' )
