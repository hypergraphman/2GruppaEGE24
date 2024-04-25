from turtle import *

speed(0)
cell = 20
for _ in range(2):
    fd(cell * 13)
    rt(90)
    fd(cell * 20)
    rt(90)
pu()
fd(cell * 8)
rt(90)
bk(cell * 3)
lt(90)
pd()
for _ in range(2):
    fd(cell * 16)
    rt(90)
    fd(cell * 8)
    rt(90)
pu()
for x in range(0, 20):
    for y in range(4, -21, - 1):
        goto(cell * x, cell * y)
        dot(3, 'Red')
done()