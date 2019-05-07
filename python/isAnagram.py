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

def isAna( a=None ):
   if len(a) == 1 or len(a) == 0:
      return 0
   length = len(a)
   for index in range(0, length/2):
      if( a[index] != a[length-1-index] ):
         return 1
   return 0

def rankAnagram( a=None ):
   if( isAna(a) == 0 ):
       return 0
   return( 1 + rankAnagram(a[1:]) )
   
assert(isAna('HerooreH') == 0)
assert(isAnagram( a='liberalism', b='imsalleirb' ) == 0)
assert(isAna('HeroPoreH') == 0)
assert(isAna('HeroPaoreH') == 1)
assert(rankAnagram('Herore') == 1)
assert(rankAnagram('Herore') == 1)
assert(rankAnagram('Herore') == 1)
assert(rankAnagram('Herore') == 1)
assert(rankAnagram('arrivi') == 3)
assert(rankAnagram('most') == 3)
assert(rankAnagram('malayalam') == 0)
