class ClassA(object):
    static_var = 1
    
    def __init__(self):
        print "Initializing A"
        self.instance_var = 2
        self.my_method() # this is new
        
    def my_method(self):
        print "Do Something"
        
class ClassB(ClassA):
    def __init__(self):
        print "Initializing B"


        super(ClassB,self).__init__()

        
    def my_method(self):
        print "Do Something Else"





def main():
    
    b = ClassB()    
    print "b.static_var =",b.static_var
    
    print "b.instance_var =",b.instance_var    
    
    
    
if __name__ == "__main__":
    main()