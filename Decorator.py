def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("thanks for using this function")
    return mfx
@greet
def hello():
    print("Hello world")
#@greet
def sum(a,b):
    print(a+b)
hello()
greet(sum)(1,2)
