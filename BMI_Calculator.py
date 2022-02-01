height = float(input("Enter your height in m:"))
weight = int(input("Enter your height in Kg:"))

body_mass_index = weight / (height**2)

bmi_final = round(body_mass_index, 1)
print(bmi_final)

if bmi_final > 18.5:
    if bmi_final < 25:
        print(f"Your bmi is {bmi_final} and you normal weight")
    elif bmi_final < 30:
         print(f"Your bmi is {bmi_final} and You are overweight")
    elif bmi_final < 35:
        print(f"Your bmi is {bmi_final} You are Obese")
    else:
         print("You are  clinicaly obese")
else:
  print(f" Your bmi is {bmi_final} and You are underweight")


