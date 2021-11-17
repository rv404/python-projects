from timeit import repeat

def linear_time():
    SETUP_CODE = '''
from search_types import linearSearch
from random import randint'''
    TEST_CODE = '''
list = [x for x in range(10000)]
find = randint(0, 10000)
linearSearch(list, find)'''
    times = repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=1000)
    x1,x2,x3 = times
    ave_time = (x1 + x2 + x3)/3000
    print(f'Result: Average time for linear search was {ave_time:3.2e} seconds.')
    
def binary_time():
    SETUP_CODE = '''
from search_types import binarySearch
from random import randint'''
    TEST_CODE = '''
list = [x for x in range(10000)]
find = randint(0, 10000)
binarySearch(list, find, 0 , 9999)'''
    times = repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=1000)
    x1,x2,x3 = times
    ave_time = (x1 + x2 + x3)/3000
    print(f'Result: Average time for binary search was {ave_time:3.2e} seconds.')
   
if __name__ == '__main__':
    linear_time()
    binary_time()
    
