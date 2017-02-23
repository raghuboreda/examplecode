import argparse

class DatapathPort( object ):
   _supportedFuncs = 0x0
   _LINK_STATUS_FUNC = 0x1
   _SET_INIT_SPEED_FUNC = 0x2
   _CONFIGURE_SPEED_FUNC = 0x3
   portType = None

   def isLinkedUp( self, lane=0 ):
      pass

   def setInitSpeed( self, lane=0, speedStr=None ):
      pass

   def configureSpeed( self, lane=0, speedStr=None ):
      pass

class FrontPanel( DatapathPort ):
   def __init__( self, id ):
      self._id = id
      self.portType = 'fpPort'

class MacPort( DatapathPort ):
   def __init__( self, id ):
      self._quadId = id
      self.portType = 'switchPort'
      self._supportedFuncs |= DatapathPort._LINK_STATUS_FUNC
      self._supportedFuncs |= DatapathPort._SET_INIT_SPEED_FUNC
      self._supportedFuncs |= DatapathPort._CONFIGURE_SPEED_FUNC

   def isLinkedUp( self, lane=0 ):
      print 'Linked up'
      print 'call LinkedUpSdk:Quad %d Lane %d' % (self._quadId, lane)

   def configureSpeed( self, lane=0, speedStr=None ):
      if speedStr == '40G' or speedStr == '100G':
         print 'call AddportSdk:Quad %d Lane 0' % self._quadId
      elif speedStr == '25G' or speedStr == '10G':
         print 'call AddportSdk:Quad %d Lane %d' % (self._quadId, lane)
      else:
         print 'Unsupported Speed'

class SwitchChip( object ):
   def __init__( self, numPorts ):
     self.macPort = []
     for index in range( 1, numPorts+1 ):
        self.macPort.append(MacPort( index ))

class SimpleDatapath( object ):
   def __init__( self, a=None ):
      self.dpPorts = []
      self.portLaneSelects = dict()
      for dpPort in a:
	 self.dpPorts.append(dpPort)

   def isLinkedUp( self, lane=0 ):
      for dpPort in self.dpPorts:
	 dpPort.isLinkedUp( lane=lane )

   def setInitSpeed( self, lane=0, speedStr=None ):
      for dpPort in self.dpPorts:
	 dpPort.setInitSpeed( lane=lane, speedStr=speedStr )

   def configureSpeed( self, lane=0, speedStr=None ):
      if speedStr == '100G' or speedStr == '40G':
         self.portLaneSelects[ 0 ] = 0x1
      elif speedStr == '25G' or speedStr == '10G':
         for laneIndex in range(4):
            self.portLaneSelects[ laneIndex ] = 0x1
      else:
         print 'Unsupported Speed'

      for dpPort in self.dpPorts:
	 dpPort.configureSpeed( lane=lane, speedStr=speedStr )
  
class SwitchBoard():
   def __init__( self ):
      self.fp = []
      self.datapaths = []
      for index in range(1, 65):
         self.fp.append(FrontPanel(index))

      self.switchChip = SwitchChip( 64 )
      
      for index in range(64):
        self.datapaths.append(SimpleDatapath( 
           [self.fp[index], self.switchChip.macPort[index]] ))

if __name__ == '__main__':
   parser = argparse.ArgumentParser( description="A traffic test" )
   parser.add_argument("-p", "--ports", help="select ports traffic test",
      type=str)
   parser.add_argument("-s", "--speed", help="select speed",
      type=str)
   p = parser.parse_args()
   portargs = []
   
   s = p.ports
   if len(s) > 1:
      lp = s.find(',')
      while (lp != -1):
         innerS = s[:lp]
         lp1 = innerS.find('..') 
         if lp1 != -1:
           portargs.append((innerS[:lp1], innerS[lp1+2:]))
         else:
           portargs.append(innerS)
         s = s[lp+1:]
         lp = s.find(',')

      lp = s.find('..')
      #print s
      if lp != -1:
         portargs.append((s[:lp],s[lp+2:]))
      else:
         portargs.append(s)
   else:
      portargs.append(s)

   print portargs
   board = SwitchBoard()
   for portpair in portargs:
      if len(portpair) == 2:
         firstPort, secondPort = portpair
         lp = firstPort.find('/')
         if lp == -1:
            port1 = int(firstPort)
            print port1
         else:
            port1 = int(firstPort[:lp]) - 1
            lane1 = int(firstPort[lp+1:])
            #print port1, lane1
         lp = secondPort.find('/')
         if lp == -1:
            port2 = int(secondPort) - 1
            print port2
         else:
            port2 = int(secondPort[:lp]) - 1
            lane2 = int(secondPort[lp+1:])
            #print port2, lane2
         portIndex = port1
         while portIndex <= port2:
            for laneIndex in range(4):
               board.datapaths[portIndex].configureSpeed( speedStr=p.speed, 
                  lane=laneIndex)
            portIndex = portIndex + 1
      else:
         lp = portpair.find('/')
         if lp == -1:
            portIndex = int(portpair) - 1
            board.datapaths[portIndex].configureSpeed( speedStr=p.speed, 
               lane=0)
         else:
            portIndex = int(portpair[:lp]) - 1
            laneIndex = int(portpair[lp+1:])
            board.datapaths[portIndex].configureSpeed( speedStr=p.speed, 
               lane=laneIndex)

