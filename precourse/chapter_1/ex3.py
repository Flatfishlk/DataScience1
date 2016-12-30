def fizzbuzz(num, fizz, buzz):
    if num % fizz == 0 and num % buzz == 0:
        print "FizzBuzz"
    if num % fizz == 0 and num % buzz != 0:
        print "Fizz"
    if num % fizz != 0 and num % buzz == 0:
        print "Buzz"
    else:
        print ""

fizzbuzz(10,2,5)
fizzbuzz(10,2,4)
fizzbuzz(10,4,5)
fizzbuzz(10,3,7)
