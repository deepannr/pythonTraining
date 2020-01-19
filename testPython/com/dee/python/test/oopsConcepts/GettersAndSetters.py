class GettersAndSetters(object):
    def __init__(self, courseName):
        self.courseName = courseName
        
    def setCourseName(self, courseName):
        self.courseName = courseName.upper()
    
    def getCourseName(self):
        return self.courseName
    

obj = GettersAndSetters("Design")
print(obj.getCourseName())

obj.setCourseName("courseName")
print(obj.getCourseName())