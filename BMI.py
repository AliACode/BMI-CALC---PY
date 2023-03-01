
heightIN = float(input('Please enter your height in Inches: '))
weightLB = float(input('Please enter your weight in Pounds: '))


def BMI (heightIN, weightLB):
    bmi = weightLB/(heightIN**2) * 703

    if bmi >= 19 and bmi <= 24:
       return 'NORMAL', bmi

    elif bmi >= 25 and bmi <= 29:
        return 'OVERWEIGHT', bmi

    elif bmi >= 30 and bmi <= 39:
        return 'OBESE', bmi

    elif bmi > 39:
        return 'MORBIDLY OBESE', bmi

    elif bmi < 19:
        return 'UNDERWEIGHT', bmi
        

quote, bmi = BMI(heightIN, weightLB)
print('your bmi is: {} and you are: {}' .format(bmi, quote))
