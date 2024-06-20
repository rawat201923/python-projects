username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()



x = 99
# def func2(y):
#     z=x+y
#     return z

# result = func2(2)
# print(result)



# def func3():
#     global x 
#     x = 12 

# func3()
# print(x)



#### closures

# def f1():
#     x=88
#     def f2():
#         print(x)
#     f2()
# myresult = f1()
# print(myresult())


def chaicode(num):
    def actual(x):
        return x** num
    return actual

# def chaicode(2):
#     def actual(x):
#         return x**2
#     return actual


f = chaicode(2)
g= chaicode(3)

print(f(3))
print(g(3))