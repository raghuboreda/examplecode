def ints( start, end=None):
   i = start
   while i <= end or end is None:
      yield i
      i = i + 1

def all_ints():
   yield(0)
   for i in ints( 1, 25 ):
      yield(i)
      yield(-i)

for i in all_ints():
   print i  
