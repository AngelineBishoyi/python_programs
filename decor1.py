def decorator(func):
    def inner_func():
        func()
        print('How you doing')
    return inner_func
@decorator
def greet():
    print('Hello')
greet()
def dosome():
    print('Im doing code')
dosome()