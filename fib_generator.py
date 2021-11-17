# Infinite Fibonacci sequence generator
# 1, 1, 2, 3, 5...
def fib_generator():
    a = 0
    b = 1
    while True:
        a, b = b, (a+b)
        yield a

"""
# Create the generator object
gen_obj = fib_generator()

# use loop and next() to iterate over the object
i=1
while i < 10:
	print(next(gen_obj))
	i+=1
"""