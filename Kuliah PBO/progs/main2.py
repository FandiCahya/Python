from sys import path
path.append('E:\Python\Kuliah PBO\packages')

import extra.iota
print(extra.iota.FunI())
print('='*20)


from extra.iota import FunI
print(FunI())
print('='*20)



from sys import path
path.append('E:\Python\Kuliah PBO\packages')

import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())
print('='*20)

from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())
print('='*20)



from sys import path

path.append('..∖∖packages∖∖extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())








