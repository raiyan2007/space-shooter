def build_pyramid(p_size):
    for a in range(1, p_size + 1):
        for b in range(0, (p_size - a)):
            print(" ", end="")
        for x in range(0, a):
            print("* ", end="")
        print("")

    for m in range(1, (p_size)):
        for n in range(0, m):
            print(" ", end="")
        for p in range(0, (p_size - m)):
            print("* ", end="")
        print("")
p_size = int(input("enter a number please\n"))
out = False

while p_size > 0 and not(out):
    build_pyramid(p_size)
    build_pyramid(p_size+2)
    p_size = int(input("enter a number please\n"))

    if p_size < 0:
        out = True















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































