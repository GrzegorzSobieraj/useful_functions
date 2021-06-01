def right_triangle_hypotenuse(leg_a, leg_b):
    """Get lenghts of both legs of right triangle and return lenght of hypotenuse."""
    if type(leg_a) not in (int, float) or type(leg_b) not in (int, float):
        raise TypeError
    if leg_a <= 0 or leg_b <= 0:
        raise ValueError
    return (leg_a ** 2 + leg_b ** 2) ** 0.5
    
