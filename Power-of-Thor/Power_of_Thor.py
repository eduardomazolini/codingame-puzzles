import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in input().split()]

MX = 0
MY = 0
X = ''
Y = ''
step = 0

if LX > TX:
    MX = LX - TX
    X = 'E'

if TX > LX:
    MX = TX - LX
    X = 'W'
    
if LY > TY:
    MY = LY - TY
    Y = 'S'

if TY > LY:
    MY = TY - LY
    Y = 'N'


    
# game loop
while 1:
    E = int(input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    step = step + 1
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(E,file=sys.stderr)
    move = ''
    if (step <= MY):
        move = Y
    if (step <= MX):
        move = move + X
        
    print(move,file=sys.stderr)
    
    print(move) # A single line providing the move to be made: N NE E SE S SW W or NW
