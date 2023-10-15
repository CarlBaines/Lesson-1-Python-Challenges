def powerCalc():
    voltage = int(input("Please enter the total voltage of the appliance ")) #inputs.
    current = int(input("Please enter the total current of the appliance "))

    pwr = (voltage*current) #power equation

    print(str(pwr) + 'W') #adds Watts unit on the end.

powerCalc()