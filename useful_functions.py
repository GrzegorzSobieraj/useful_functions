def calculate_pit(income):
    """Get income and return tax due."""
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


def right_triangle_hypotenuse(leg_a, leg_b):
    """Get lenghts of both legs of right triangle and return lenght of hypotenuse."""
    if type(leg_a) not in (int, float) or type(leg_b) not in (int, float):
        raise TypeError
    if leg_a <= 0 or leg_b <= 0:
        raise ValueError
    return (leg_a ** 2 + leg_b ** 2) ** 0.5
    
