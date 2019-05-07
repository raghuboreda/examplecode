### compile_word('YOU') => '(1*U + 10*O + 100*Y)'
import string, re, itertools


def compile_formula( formula, verbose=False ):
   """ Compile formula into a function. Also return letters found,
       a str, in same order as params of function.
       The first digit of a multi-digit number can't be 0.
       so if YOU is a word in the formula, and the function is called
       with Y equal to 0, the function should return False
   """
   letters = ''.join(set(re.findall('[A-Z]', formula)))
   parms = ', '.join(letters)
   tokens = map(compile_word, re.split('([A-Z]+)', formula))
   print tokens
   body = ''.join(tokens)
   f = 'lambda %s: %s' % (parms, body)
   if verbose: print f
   return eval(f), letters

def compile_word( word ):
   if word.isupper():
      terms = [('%s*%s' % (10**i, d)) 
                for i, d in enumerate(word[::-1])]
      return '(' + '+'.join(terms) + ')'
   else:
      return word

def faster_solve( formula ):
   f, letters = compile_formula(formula, verbose=True)
   for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
      try:
         if f(*digits) is True:
            table = string.maketrans( letters, ''.join(map(str, digits)))
            return formula.translate(table)
      except ArtithmeticError:
         pass

#print faster_solve( 'A**2 + B**2 == C**2' )
assert faster_solve( 'A + B == BA' ) == None
