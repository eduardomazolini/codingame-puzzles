import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MESSAGE = input()
print("MESSAGE: "+str(MESSAGE), file=sys.stderr)
OrdMessage = [ord(x) for x in MESSAGE]
print("OrdMessage: "+str(OrdMessage), file=sys.stderr)
answer = ""
seq = ""
for i in OrdMessage:
    print("i: "+str(i), file=sys.stderr)
    for b in range(1,8):
        bit = ((i << b) & 128) >> 7
        if (str(bit)!=seq):
            answer += " 0 " if bit==1 else " 00 "
            seq=str(bit)
        answer += "0"
        print("byte: "+str(b)+" "+str(((i << b) & 128) >> 7), file=sys.stderr)
        
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(answer.strip())
