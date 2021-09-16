def help():
    """easter egg"""
    for x in range(1,10):
        print(f"{x} is fun".format(x))
def table(num):
    """write table of any number"""
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}".format(num,i,num*i))
def error():
    """give error enjoy getting error"""
    raise TypeError(" : it just prank")
def prime_fun(number):
    """try it"""
    for num in range(2,number):
        if number%num == 0:
            print("its a prime number")
        else:
            print("its is not a prime number")
        