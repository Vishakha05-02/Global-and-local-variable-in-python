# global variable

a = 10

def global_local():
    global a        # tell to python that we want to use global variable

    a = 15
    print('variable inside the function', a)

global_local()

print('variable outside the function', a)
