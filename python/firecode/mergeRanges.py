class Range(object):
    def __init__( self, l, u):
        self.l = l
        self.u = u

    def __str__( self ):
        return "["+str(self.l)+","+str(self.u)+"]"

def merge_ranges(input_range_list=None):
    rangeList = []
    for item in input_range_list:
        r = Range( item[0], item[1] )
        rangeList.append(r)

    l0 = rangeList[0].l
    u0 = rangeList[0].u
    newR = []
    for i in range( 1, len(rangeList)):
        l1 = rangeList[i].l
        u1 = rangeList[i].u
        if l1 < u0 and u1 < u0:
            continue
        elif l1 < u0 and u1 > u0:
            u0 = u1
        elif l1 > u0:
            newR.append( [l0, u0] )
            l0 = l1
            u0 = u1
    newR.append( [l0, u0] )
    return newR

print merge_ranges( input_range_list= [[1,10],[8,15]] )
print merge_ranges( input_range_list= [[1,5],[8,15], [7, 35]] )
print merge_ranges( input_range_list= [[1,5],[4,15], [7, 35]] )
print merge_ranges( input_range_list= [[1,5],[4,15], [7, 35], [49,55]] )
