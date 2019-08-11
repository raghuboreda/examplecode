import copy
def mergeAccounts( accounts ):
    retacc = copy.deepcopy( accounts )
    def mergeAc( accounts, i, j ):
        s1 = set(accounts[i][1:])
        s2 = set(accounts[j][1:])
        l = list(s1 | s2)



    aL = len(accounts)
    for i in range(aL):
        for j in range(i+1,aL):
            ac = accounts[i]
            bc = accounts[j]
            s1 = set(ac[1:])
            s2 = set(bc[1:])
            if len( s1 & s2 ) > 0:
                mergeAc( accounts, i, j )

