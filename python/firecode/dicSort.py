d = { 'Alpha':5, 'Beta':8, 'Comma':3, 'Delta':2 }

s_d = sorted( d.iteritems(), key=lambda (k,v):(v,k) )
print s_d
