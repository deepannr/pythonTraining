x = 90
print('--- If, Elif, Else ----')
if (x < 60):
    print('Less than 60')
elif (x > 80):
    print('Greater than 80')
    print('Distinction')
else:
    print('Fail')

print('\n--- Another Example ----')    
x = 60
if(x > 60):
    print('Greater than 60')
    if(x == 60):
        print('Equal to 60')

print('\n--- Works on Indentation ----')
if(x > 60):
    print('Greater than 60')
if(x == 60):
    print('Equal to 60')
