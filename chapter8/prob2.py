# write a function that converts Fahrenheit to Celsius. The formula is: C = 5 * (F - 32) / 9
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter the temprature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")