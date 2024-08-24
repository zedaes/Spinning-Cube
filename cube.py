import math
import os
import time

a, b, c = 0, 0, 0

cubeWidth = 20
width, height = 160, 44
zBuffer = [0] * (width * height)
buffer = [' '] * (width * height)
backgroundAsciiCode = ' '
distanceFromCam = 100
horizontalOffset = 0
k1 = 40

incrementSpeed = 0.6

def calculateX(i, j, k):
    return (
        j * math.sin(a) * math.sin(b) * math.cos(c) - 
        k * math.cos(a) * math.sin(b) * math.cos(c) + 
        j * math.cos(a) * math.sin(c) + 
        k * math.sin(a) * math.sin(c) + 
        i * math.cos(b) * math.cos(c)
    )

def calculateY(i, j, k):
    return (
        j * math.cos(a) * math.cos(c) + 
        k * math.sin(a) * math.cos(c) - 
        j * math.sin(a) * math.sin(b) * math.sin(c) + 
        k * math.cos(a) * math.sin(b) * math.sin(c) - 
        i * math.cos(b) * math.sin(c)
    )

def calculateZ(i, j, k):
    return (
        k * math.cos(a) * math.cos(b) - 
        j * math.sin(a) * math.cos(b) + 
        i * math.sin(b)
    )

def calculateForSurface(cubeX, cubeY, cubeZ, ch):
    global x, y, z, ooz, xp, yp, idx
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1 / z

    xp = int(width / 2 + horizontalOffset + k1 * ooz * x * 2)
    yp = int(height / 2 + k1 * ooz * y)

    idx = xp + yp * width
    if 0 <= idx < width * height:
        if ooz > zBuffer[idx]:
            zBuffer[idx] = ooz
            buffer[idx] = ch

while True:
    buffer = [' '] * (width * height)
    zBuffer = [0] * (width * height)
    #this code displays 3 cubes
    cubeWidth = 20
    horizontalOffset = -2 * cubeWidth

    for cubeX in [i * incrementSpeed for i in range(-int(cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed))]:
        for cubeY in [i * incrementSpeed for i in range(-int(cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed))]:
            calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
            calculateForSurface(cubeWidth, cubeY, cubeX, '$')
            calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
            calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
            calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
            calculateForSurface(cubeX, cubeWidth, cubeY, '+')

    cubeWidth = 10
    horizontalOffset = 1 * cubeWidth

    for cubeX in [i * incrementSpeed for i in range(-int(cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed))]:
        for cubeY in [i * incrementSpeed for i in range(-int(cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed))]:
            calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
            calculateForSurface(cubeWidth, cubeY, cubeX, '$')
            calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
            calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
            calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
            calculateForSurface(cubeX, cubeWidth, cubeY, '+')

    cubeWidth = 5
    horizontalOffset = 8 * cubeWidth

    for cubeX in [i * incrementSpeed for i in range(-int(cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed))]:
        for cubeY in [i * incrementSpeed for i in range(-int(cubeWidth / incrementSpeed), int(cubeWidth / incrementSpeed))]:
            calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
            calculateForSurface(cubeWidth, cubeY, cubeX, '$')
            calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
            calculateForSurface(-cubeX, cubeY, cubeWidth, '#')
            calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
            calculateForSurface(cubeX, cubeWidth, cubeY, '+')

    os.system('cls' if os.name == 'nt' else 'clear')
    for k in range(width * height):
        print(buffer[k], end='')
        if (k + 1) % width == 0:
            print()

    a += 0.05
    b += 0.05
    c += 0.01

    time.sleep(0.016)
