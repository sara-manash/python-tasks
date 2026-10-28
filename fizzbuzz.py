#1 eded daxil edin
eded = int (input("1 eded daxil et:"))
#eded 3 ya 5 bolmesini yoxlayiriq
if eded % 3 == 0 and eded % 5 == 0:
    print("FizzBuzz")
elif eded % 3 == 0:
    print("Fizz")
elif eded % 5 == 0:
    print("Buzz")
elif eded % 3!=0 and eded %5!=0:
    print("eded")