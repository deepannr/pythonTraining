'''
Created on May 13, 2019

@author: ab75812
'''


def myFunction(string):
    print("Function Call ", string)
    toInput = input("Enter String : ")
    print('Function', toInput)
    return toInput

def Main():
    print("Main Function")
    returnedValue = myFunction("Hello")
    print("Called from myFunction ", returnedValue)

    
if __name__ == "__main__":
    Main()