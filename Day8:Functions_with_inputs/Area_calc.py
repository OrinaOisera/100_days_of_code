import  math

def area_calc(height, width):
    a = height * width
    n_cans = a / 5
    fina_can = math.ceil(n_cans)
    print(f"You will need {fina_can} paint cans")


test_h = int(input("Enter the test height:"))
test_w = int(input("Enter the test width:"))


area_calc(height=test_h, width=test_w)
