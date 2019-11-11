import math
import copy 
class Track():
   
    def __init__(self):
        self.values = None
        self.ans = None
        self.children = []

    def __CreateChild(self, d_val):
        for i in range(d_val):
            self.children.append( Track() ) 
                
    def CreateDimension(self, dim):
        if len(dim) == 0:
            self.ans = math.inf
        else:
            d_val = dim.pop(0)
            self.__CreateChild( d_val )
            i = 0
            for t in self.children:
                t.values = i
                t.CreateDimension(copy.copy( dim ) )
                i+=1

    def GetValue(self, div ):
        if len ( self.children ) == 0:
            return self.ans
        else:
            val = div.pop(0)
            for t in self.children:
                if t.values == val:
                    return t.GetValue(copy.copy(div))

    def SetValue(self, div, val):
        if len ( self.children ) == 0:
            self.ans = val
        else:
            tempVal = div.pop(0)
            for t in self.children:
                if t.values == tempVal:
                    t.SetValue(copy.copy(div), val )

        
        
dimension = [2,2,3]
t = Track()
t.CreateDimension(dimension)


for i in dim[0]:
    for j in dim[1]:
        for k in dim[2]:
            print( t.GetValue[i,j,k] )

apple = 0
for i in dim[0]:
    for j in dim[1]:
        for k in dim[2]:
            t.SetValue[i,j,k] =apple
            apple+=1

for i in dim[0]:
    for j in dim[1]:
        for k in dim[2]:
            print( t.GetValue[i,j,k] )
            


'''



        if self.values == None:

            return ans

        ans += "Level " + str(level)
        ans += " : "
        i = 0
        while i <  len(self.values) - 1:
            ans += str( self.values[i] ) + ", "
            i+=1
        ans += str( self.values[i] )
        ans += "\n"
            
        level+=1
        for j in range(level):
            ans += "| "
            
        ans = self.children.Print(ans,level)
        return ans
'''
