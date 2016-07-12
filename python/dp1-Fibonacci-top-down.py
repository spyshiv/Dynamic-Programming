# Python program for Memoized (top down) version of nth Fibonacci number
 
# function to calcualte nth Fibonacci number
def fib(n, lookup):
 
    # Base case
    if n == 0 or n == 1 :
        lookup[n] = n
 
    # If the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup) 
 
    # return the value corresponding to that value of n
    return lookup[n]
# end of function
 
#-----Driver program to test the above function----
n = 34
# Declaration of lookup table
# Handles till n = 100 
lookup = [None]*(101)
print "Fibonacci Number is ", fib(n, lookup)