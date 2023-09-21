from sys import path

# path.append('...\\modules')
path.append('E:\\Python\\Kuliah PBO\\modules')

# print(module.counter)
import module

from module import suml, prodl,nyelok

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
print(suml([ 3,1,3]))
print(nyelok())
