# Convert degree Farenheit in degree Celsius

tempInFarenheit = 0
tempInCelsius = 0

# 1. Ask the temperature in Farenheit
tempInFarenheit = input("Enter the temperature in Farenheit:")

# 1b. Make sure the computer got it right
print("The temperature you entered is: ", tempInFarenheit)

# 2. Make the conversion
tempInCelsius = (float(tempInFarenheit) - 32) * .5556

# 3. Tell the user what is the temperature in Celsius
print("The temperature in Celsius is: ", tempInCelsius)
 