def reverse(x):
    # if number negativ, store negative sign, convert number to positive
    if x < 0:
        sign = -1
        x = x * -1
    else:
        sign = 1
    # convert number to string, reverse string, convert back to integer
    reversed_x = int(str(x)[::-1])
    # apply original sign to reversed number
    result = reversed_x * sign
    # check if reversed number is within 32-bit integer range
    if result > 2**31-1 or result < -2**31:
        return 0
    else:
        return result
    