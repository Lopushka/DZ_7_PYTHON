def print_operation_table(operation, num_rows=6, num_columns=6):
    for rows in range(1, num_rows + 1):
        for columns in range(1, num_columns+1):
            print(operation(rows, columns), end='\t')
        print()


print(print_operation_table(lambda x,y: x**y,4,4))
