#  def add(a,b):
#     add(2,5)
# recursion 

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(5))