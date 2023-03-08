import turtle
from turtle import*
color('pink', 'magenta')
begin_fill()
while True:
    forward(400) # fd (200) = move forward, bk() = move backward
    left(170)    # lt(170) = rotate left, rt() = rotate right
    if abs(pos()) < 1:
        break
end_fill()
done()
