from turtle import*

for angle in range(0, 360, 15):
    setheading(angle)
    forward(200)
    write(str(angle) + '°')
    backward(200)

for angle in range(20):
    undo()
done()
