X=int(input())
Y=int(input())
Z=int(input())
max=0
COST=int(input())
if (X+Y+Z)>COST:
    if (X+Y>X+Z and X+Y>Y+Z):
        max=X+Y
        print('Alisa and Bob')
    if (X+Z>X+Y and X+Z>Y+Z):
        max=X+Z
        print('Alisa and Charley')
    if (Y+Z>X+Y and Y+Z>X+Z):
        max=Y+Z
        print('Bob and Charley')
else:
    print('error: cost>x+y+z')
print(max)
