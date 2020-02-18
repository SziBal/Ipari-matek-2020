def max_pooling(input_table):
    output_table = []
    ### CODE START
    for x in range (9):
        for y in range (9):
            input_table[x][y]=max(input_table[x][y],input_table[x+1][y],input_table[x][y+1],input_table[x+1][y+1])
        del input_table[x][-1]
    del input_table[-1]
    output_table=input_table
    print(output_table)
    ### CODE END
    return output_table