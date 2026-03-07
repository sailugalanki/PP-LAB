
feet = float(input("Enter length in feet: "))

l1 = ["inches", "yards", "miles", "millimetres", "centimetres", "meters", "kilometres"]

l2 = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]

print("Choose conversion:")
for i in range(len(l1)):
    print(i+1, "->", l1[i])

choice = int(input("Enter your choice (1-7): "))


result = feet * l2[choice-1]


print("Length from feet to", l1[choice-1], "=", result)
