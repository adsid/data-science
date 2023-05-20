temperature = 32

if temperature > 85:
    print(f"It is a hot day because it is {temperature} degrees")
elif temperature > 70 and temperature <= 85:
    print(f"It is a pleasant day because it is {temperature} degrees")
elif temperature > 55 and temperature <= 70:
    print(f"It is cold because it is {temperature} degrees")
elif temperature==32:
    print(f"Wooooo Water will freeze today because it is {temperature} degrees")
else:
    print(f"It is a cold day because it is {temperature} degrees")