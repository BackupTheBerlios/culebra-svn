import sys

class StdOut(sys.stdout):
    
    def __init__(self):
        
        sys.stdout.__init__(self)
        
    def write(self, out):
        
        print "Out:",
        print out
        
        
if __name__ == "__main__":
    
    sys.stdout = StdOut()
    
    print "hola"