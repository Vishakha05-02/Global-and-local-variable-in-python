# global variable

a = 10

def global_local():

    # local variable
     a = 15
     print('variable inside the function', a)

global_local()



print('variable outside the function',a)
