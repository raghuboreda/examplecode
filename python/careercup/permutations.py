#from itertools import permutations
#s = 'cap'
#p = [''.join(p) for p in permuations(s) ]
#k = set(p)

def permute_helper( slate, step=0,result=None ):
    if step == len(slate):
        result.append(''.join(slate))

    for index in range(step, len(slate)):
        slate = [c for c in slate]
        if step != index:
            slate[step], slate[index] = slate[index], slate[step]
        permute_helper(slate, step+1, result)

def permute_string( word ):
    results = []
    permute_helper(word, step=0, result=results)
    return results

def permute2_helper( slate, numPlaced, result ):
    if numPlaced >= len(slate):
        tmp = slate.copy()
        result.append(tmp)
    else:
        for i in range(numPlaced, len(slate)):
            if i != numPlaced:
                slate[numPlaced], slate[i] = slate[i], slate[numPlaced]
            permute2_helper( slate, numPlaced+1, result)
            if i != numPlaced:
                slate[numPlaced], slate[i] = slate[i], slate[numPlaced]

def permute_list( arr ):
    result = []
    permute2_helper( arr, numPlaced=0, result=result)
    return result

print(permute_string('cap'))
print(permute_string('less'))
print(permute_list([1,2,3]))