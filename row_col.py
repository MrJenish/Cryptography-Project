def get_row_col_indices(zigzag_value):
    """
    Calculates the row and column indices corresponding to a given value in a zigzag scan
    
    Parameters:
        zigzag_value (int): The value to find the row and column indices of
    
    Returns:
        row_index (int): The row index of the value in the zigzag scan
        col_index (int): The column index of the value in the zigzag scan
    """
    row_index = 0
    for i in range(-11, 12):
        power_of_two = 2 ** i
        if power_of_two == abs(zigzag_value):
            row_index = i + 1
            break
        elif power_of_two > abs(zigzag_value) and abs(zigzag_value) > 0:
            row_index = i
            break
    
    if zigzag_value > 0:
        col_index = ((2 ** row_index) - 1) - ((2 ** (row_index - 1)) - 1) + (zigzag_value - ((2 ** (row_index - 1)) - 1))
    elif zigzag_value < 0:
        col_index = ((2 ** row_index) - 1) - abs(zigzag_value) + 1
    else:
        col_index = 1
        
    col_index -= 1
    
    return row_index, col_index