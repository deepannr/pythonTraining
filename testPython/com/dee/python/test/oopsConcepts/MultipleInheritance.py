class First(object):
    def __init__(self):
        #super(First, self).__init__()
        print("First Class")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("Second Class")
        
class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print("Third Class")
        
        
Third()