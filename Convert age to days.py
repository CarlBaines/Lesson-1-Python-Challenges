def calc_age():
    leapyr = input('Is it a leap year? ')

    if leapyr == 'Y' or leapyr == 'y':

        ageinyrs = int(input('What is your age in years '))
        while ageinyrs < 0:
            ageinyrs = int(input('What is your age in years '))

        ageindays = (ageinyrs*366)

        print('Your age in days is ' + str(ageindays))

        return ageindays

    if leapyr == 'N' or leapyr == 'n':

        ageinyrs = int(input('What is your age in years '))
        while ageinyrs < 0:
            ageinyrs = int(input('What is your age in years '))

        ageindays = (ageinyrs*365)

        print('Your age in days is ' + str(ageindays))

        return ageindays

calc_age()