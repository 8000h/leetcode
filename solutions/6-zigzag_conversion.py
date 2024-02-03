def convert(s, numRows):
    # Cheking number of rows, if its 1 returning same as zigzag pattern will not change anything if we have 1 row
    if numRows == 1 or numRows >= len(s):
        return s

    # Create an array of strings for each line
    zigZag = ['' for _ in range(numRows)]

    # Initialize index for array of strings zigZag
    index, step = 0, 1

    # Traverse through given string
    for char in s:
        # Append current character to current row
        zigZag[index] += char

        # If last row is reached, change direction to 'up'
        if index == 0:
            step = 1
        # If 1st row is reached, change direction to 'down'
        elif index == numRows - 1:
            step = -1

        # Move to next row using step value
        index += step

    return ''.join(zigZag)