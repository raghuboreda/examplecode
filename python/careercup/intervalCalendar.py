class Event( object ):
    def __init__( self, st, et ):
        self.startTime = st
        self.endTime = et

    def __str__( self ):
        s = '( %d, %d )' % (self.startTime, self.endTime )
        return s

tupleInitList = [ (1,10), (2,8), (3,9), (4,10),
                  (7,15), (11,16), (3,6), (7,10) ]

def findNonIntersectingEvents( tupL=None ):
    eventIns = []
    for st, et in tupL:
        eventIns.append( Event( st=st, et=et ) )
    eventIns.sort( key=lambda event : event.endTime )

    #for event in eventIns:
    #    print event

    intEvents = []
    while( len(eventIns) > 0 ):
        item = eventIns.pop(0)
        tempList = [] 
        for event in eventIns:
            #print 'Comparing ', item, ' with ', event  
            if not event.startTime < item.endTime:
                # intersecting event - remove
                # print 'removing ', event  
                tempList.append(event)
        eventIns = tempList
        intEvents.append( item )

    print len(intEvents)
    for ev in intEvents:
        print ev,
    print ''

findNonIntersectingEvents( tupL=tupleInitList )
    
