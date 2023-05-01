def check_triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        print("Triangle can be formed !")
    else:
        print("Triangle cannot be formed.")


x = int(input("Enter First Side of a Triangle : "))
y = int(input("Enter Second Side of a Triangle : "))
z = int(input("Enter Third Side of a Triangle : "))
check_triangle(x, y, z) 


    