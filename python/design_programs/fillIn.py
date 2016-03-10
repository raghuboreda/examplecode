import string, re, itertools

def solve( formula ):
   """Give a formula like 'ODD + ODD == EVEN', fill in digits to solve
      it, Input formula is a string; output is a digit-filled-in string
      or None. """
   for f in fill_in( formula ):
      if valid( f ):
         return f

def fill_in( formula ):
   """ Generate all possible fillings-in of letters in formula with digits."""
   #letters = '' 
   #for f in formula:
   #   if f in string.ascii_letters and f not in letters:
   #      letters += f
   # Above can be accomplished by this one liner
   letters = ''.join(set(re.findall('[A-Z]', formula)))
   #letters = ''.join(set(f for f in formula if f in string.ascii_letters))
   for digits in itertools.permutations('1234567890', len(letters) ):
      table = string.maketrans( letters, ''.join(digits))
      yield formula.translate( table )

def valid( f ):
   """ formula f is valid if and only if it has no numbers
       with leading zero and evals true """
   try:
      return not re.search(r'\b0[0-9]', f) and eval(f) is True
   except ArithmeticError:
      return False

print solve ( 'ODD + ODD == EVEN' )
