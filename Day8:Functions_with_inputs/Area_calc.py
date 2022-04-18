import  math

def area_calc(height, width, cover):
    area = height * width
    n_cans = area / cover
    final_can = math.ceil(n_cans)
    print(f"You will need {final_can} paint cans")


test_h = int(input("Enter the test height:"))
test_w = int(input("Enter the test width:"))
coverage = 5

area_calc(height=test_h, width=test_w, cover=coverage)
