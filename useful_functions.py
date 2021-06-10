def area_of_triangle(side_a, side_b, side_c):
    """Calculate are aof triangle."""
    if not is_triangle(side_a, side_b, side_c):
        raise Exception
    semiperimeter = (side_a + side_b + side_c) / 2
    
    return (semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) * (semiperimeter - side_c)) ** 0.5


def bmi(weight, height):
    """Calculate BMI Body Mass Index."""
    if (type(weight), type(height)) != float:
        raise TypeError
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 500:
        raise ValueError

    return weight / height ** 2


def calculate_pit(income):
    """Get income and return Polish due tax."""
    if type(income) not in (int, float):
        raise TypeError
    relief = 0

    if income <= 85_528:
        if income <= 8_000:
            relief = 1_360
        elif income <= 13_000:
            relief = 834.88 * (income - 8_000) / 5_000
        else:
            relief = 525.12
        tax = income * 0.17 - relief
    else:
        if income <= 127_000:
            relief = 525.12 * (income - 85_528) / 41_472
        tax = (income - 85_528) * 0.32 + 14_539.76 - relief

    if tax < 0:
        tax = 0

    return round(tax, 2)


def fibonacci_number(number):
    """Return Fibonacci number."""
    if type(number) != int:
        raise TypeError
    if number < 1:
        raise ValueError
    if number < 3:
        return 1

    return fibonacci_number(number - 1) + fibonacci_number(number - 2)


def ft_and_inch_to_m(foot=0.0, inch=0.0):
    """Convert feets and inches to meters."""
    if type(foot), type(inch) not in (float, int):
        raise TypeError
    if foot < 0 or inch < 0:
        raise ValueError
    
    return ft_to_m(foot) + inch_to_m(inch)


def ft_to_m(foot):
    """Convert feets to meters."""
    if type(foot) not in (float, int):
        raise TypeError
    if foot < 0:
        raise ValueError
    
    return foot * 0.3048


def inch_to_m(inch):
    """Convert inches to meters."""
    if type(inch) not in (float, int):
        raise TypeError
    if inch < 0:
        raise ValueError
    
    return inch * 0.0254


def lb_to_kg(lb):
    """Convert pounds to kilograms."""
    if type(lb) not in (float, int):
        raise TypeError
    if lb < 0:
        raise ValueError
    
    return lb * 0.45359237


def is_prime(number):
    """Check if given number is a prime number."""
    if type(number) != int:
        raise TypeError
    if number <= 1:
        return False
    if number == 2:
        return True
    if not number % 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if not number % i:
            return False
    
    return True


def is_right_triangle(leg_a, leg_b, leg_c):
    if not is_triangle(leg_a, leg_b, leg_c):
        raise Exception
    if leg_a > leg_b and leg_a > leg_c:
        hypotenuse = side_a
        return hypotenuse ** 2 == leg_b ** 2 + leg_c ** 2
    elif leg_b > leg_a and leg_b > leg_c:
        hypotenuse = side_b
        return hypotenuse ** 2 == leg_a ** 2 + leg_c ** 2
    else:
        hypotenuse = side_c
        return hypotenuse ** 2 == leg_a ** 2 + leg_b ** 2


def is_triangle(side_a, side_b, side_c):
    """Check if sides of given lenghts form a triangle."""
    if type(side_a) not in (int, float) or type(side_b) not in (int, float) or type(side_c) not in (int, float):
        raise TypeError
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError
    
    return side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a


def l_100km_to_mpg(liters_per_100km):
    """Convert l/100km (liters per 100 km) to mpg (miles per US gallon)."""
    if type(liters_per_100km) != float:
        raise TypeError
    if liters_per_100km <= 0:
        raise ValueError
    
    return 3.785411784 * 100 / (1.609344 * liters_per_100km)


def miles_gallon_to_liters_100km(miles_per_gallon):
    """Convert mpg (miles per US gallon) to l/100km (liters per 100 km)."""
    if type(miles_per_gallon) != float:
        raise TypeError
    if miles_per_gallon <= 0:
        raise ValueError
    
    return 100*3.785411784/(1.609344 * miles_per_gallon)


def right_triangle_hypotenuse(leg_a, leg_b):
    """Get lenghts of both legs of right triangle and return lenght of the hypotenuse."""
    if type(leg_a) not in (int, float) or type(leg_b) not in (int, float):
        raise TypeError
    if leg_a <= 0 or leg_b <= 0:
        raise ValueError
    
    return (leg_a ** 2 + leg_b ** 2) ** 0.5
