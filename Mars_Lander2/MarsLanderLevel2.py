import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
LAND=[]
N = int(input()) # the number of points used to draw the surface of Mars.
print("N: "+str(N), file=sys.stderr)
for i in range(N):
    # LAND_X: X coordinate of a surface point. (0 to 6999)
    # LAND_Y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    LAND_X, LAND_Y = [int(i) for i in input().split()]
    LAND.append({'X':LAND_X,'Y':LAND_Y})
    print("LAND: "+str(LAND[i]), file=sys.stderr)
    if (i > 0) and (LAND[i-1]['Y'] == LAND[i]['Y']):
        LANDAREAI={'X':LAND[i-1]['X'],'Y':LAND[i-1]['Y']}
        LANDAREAF={'X':LAND[i]['X'],'Y':LAND[i-1]['Y']}
        
print("LANDAREA: "+str(LANDAREAI), file=sys.stderr)
print("LANDAREA: "+str(LANDAREAF), file=sys.stderr)
        
        

# game loop
while 1:
    # HS: the horizontal speed (in m/s), can be negative.
    # VS: the vertical speed (in m/s), can be negative.
    # F: the quantity of remaining fuel in liters.
    # R: the rotation angle in degrees (-90 to 90).
    # P: the thrust power (0 to 4).
    X, Y, HS, VS, F, R, P = [int(i) for i in input().split()]
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    #pico
    pico = 0
    for i in range(N):
        if ((LAND[i]['X'] > X and LAND[i]['X'] < LANDAREAI['X']) and (LAND[i]['Y'] > pico)):
            pico = LAND[i]['Y']
        
    
    if (Y >= 2900):
        print("0 2")
    elif (LANDAREAI['Y']>Y or pico+300 > Y):
        print("0 4")
    elif (HS < -15):
            print("-45 4")
    elif (HS > 15):
            print("45 4")
    elif (VS < -30):
        print("0 4")
    elif (X < LANDAREAI['X']):
        print("X: "+str(X), file=sys.stderr)
        print("XA: "+str(LANDAREAI['X']), file=sys.stderr)
        print("-45 4")
    elif (X > LANDAREAF['X']):
        print("-X: "+str(X), file=sys.stderr)
        print("XA: "+str(LANDAREAF['X']), file=sys.stderr)
        print("45 4")
    else:
        print("0 1")

    
    #print("-20 3") # R P. R is the desired rotation angle. P is the desired thrust power.
