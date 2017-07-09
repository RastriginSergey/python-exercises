# -*- coding: utf-8 -*-

# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n, m):
    for i in range(1, n):
        if n * i == m:
            return True
    return False


# print(is_multiple(10, 13))


# R-1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators

def is_even(k):
    for even in range(0, k + 1, 2):
        if k == even:
            return True
    return False


# print(is_even(22))

# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    min, max = 0, 0
    for numb in data:
        if numb > max:
            max = numb
        if numb < min:
            min = numb
    return min, max


# print(minmax((1,2,3,4,5,22,-5)));


# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sq_sum(n):
    if n < 0:
        raise ValueError('Number should be greater than zero')

    sum = 0
    for i in range(1, n):
        sum += i * i
    return sum


# print(sq_sum(30))


# R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.
def sq_sum_builtIn(n):
    return sum([i * i for i in range(1, n)])


# print(sq_sum_builtIn(30))


# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sq_odd_sum(n):
    if n < 0:
        raise ValueError('Number should be greater that zero')
    sum = 0
    for i in range(1, n, 2):
        sum += i * i
    return sum


# print sq_odd_sum(4)

# R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.

def sq_odd_sumBuiltIn(n):
    if n < 0:
        raise ValueError('Number should be greater that zero')
    return sum([i * i for i in range(1, n, 2)])


# print sq_odd_sumBuiltIn(4)

# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

# It can work only if -n >= k < 0 because if index will be greater than
# negative length of iterable, it will raise IndexError
someString = 'abcder'
negIndex = -len(someString)
print someString[0] == someString[negIndex]

# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

# assert(range(50, 90, 10) == [50, 60, 70, 80]), "Assertion error"


# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

# assert (range(8, -9, -2) == [8, 6, 4, 2, 0, -2, -4, -6, -8]), 'Assertion error'


# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

assert ([1 * 2 ** i for i in range(0, 9)] == [1, 2, 4, 8, 16, 32, 64, 128, 256]), 'Assertion error'

# R-1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes
# a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.

from random import randrange


def choice(data):
    if len(data) == 0:
        raise ValueError('Function accepts only non-empty iterable')

    randomIndex = randrange(0, len(data))
    return data[randomIndex]

# print choice([1,2,3,4])
