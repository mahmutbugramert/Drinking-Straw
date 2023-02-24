
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
if straw_pos % 2 == 0:
    q = 2*glass_size-straw_pos+4
else:
    q = 2 * glass_size - straw_pos + 3
# by using if-else statement above, I found glass number, which is q/2, using glass_size and straw_pos
for d in range(int(q/2)):
# this for loop iterates glass number
    for j in range(straw_pos):
        for k in range(j):
            print(" ", end="")
        for s in range(1):
            print("o", end="")
        print()
# these 3 for loops draws straw outside of glass for every glass
    for b in range(glass_size):
# this loop iterates inside of glass
        for m1 in range(b):
            print(" ", end="")
        for g1 in range(1):
            print("\\", end="")
# these 2 for loops draw left sides of the glasses
        if b >= d:
# this if determines whether loop will draw asteriks or straw
            for y in range(2*(glass_size - b)):
                print("*", end="")
# this one draws asterikses
        else:
            for r1 in range(straw_pos - 1):
                print(" ", end="")
            for y1 in range(1):
                print("o", end="")
            for k1 in range(2 * (glass_size - b) - straw_pos):
                print(" ", end="")
# these ones draw straw
        for u1 in range(1):
            print("/", end="")
# this draws right sides of glasses
        print()
    for p in range(glass_size):
        print(" ", end="")
    for f in range(1):
        print("--", end="")
    print()
# these loops for drawing hyphens at the bottom of glasses
    for h in range(glass_size):
        for p in range(glass_size):
            print(" ", end="")
        for z in range(2):
            print("|", end="")
        print()
# these loops for drawing stems of glasses

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


