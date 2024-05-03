def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("This triangle exists.")
    else:
        print("This triangle does not exist.")

check_triangle(69, 420, 404)
