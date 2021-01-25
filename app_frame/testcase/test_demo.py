#演示装饰器
def b(run):
    def pan(*args,**kwargs):
        print("before")
        run(*args,**kwargs)
        print("end")
    return pan


@b
def a():
    print("a")

def test_dome():
    a()