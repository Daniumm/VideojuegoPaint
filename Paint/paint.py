"""
Juego: Paint

Programador 1: Daniel Alejandro Martinez Rosete
Programador 2: Andrés  Martínez Sánchez 

Fecha:09/05/22

"""


from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def drawCircle(start, end):
    #Se hace algo parecido al cuadrado pero con el lado y el ángulo ajustado 36 veces 
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(36):
        forward((end.x - start.x)/8)
        left(10)

    end_fill()


def rectangle(start, end):
    #Aqui se usa la misma lógica que el cuadrado pero se dibujan los lados normales y luego los lados pequeños a la mitad 2 veces
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.x - start.x)/2)
        left(90)
    

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range (3):
        forward(end.x - start.x)
        left(120)
        
    end_fill()
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#Agregar color nuevo 
onkey(lambda: color('aqua'), 'A')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', drawCircle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

