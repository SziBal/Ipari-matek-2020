def flea_jump(start_x, start_y, input_string):
    dest_x, dest_y = 0,0
    ### CODE START
    dest_x=start_x
    dest_y=start_y
    for x in range (len(input_string)):
        if input_string[x]=='E':
            dest_x+=1
        if input_string[x]=='D':
            dest_x-=1
        if input_string[x]=='K':
            dest_y+=1
        if input_string[x]=='N':
            dest_y-=1
    print(dest_x, dest_y)
    ### CODE END
    return dest_x, dest_y
