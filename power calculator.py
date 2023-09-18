def powerCalc():
    voltage = int(input("Please enter the total voltage of the appliance "))
    current = int(input("Please enter the total current of the appliance "))

    pwr = (voltage*current)

    print(str(pwr) + 'W')

powerCalc()