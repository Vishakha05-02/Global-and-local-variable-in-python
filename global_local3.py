# global variable

a = 10

def global_local():
     a = 15

     print('variable inside the function', a)

     globals()['a'] = 20

global_local()

print('variable outside the function',a)
