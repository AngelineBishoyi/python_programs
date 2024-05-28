import monk
def donkey_f(self):
    print('Still not getting')
monk.A.func= donkey_f
obj=monk.A()
obj.func()