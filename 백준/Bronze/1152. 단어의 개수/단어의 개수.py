str_list = list(input())

if len(str_list) < 2 and str_list[0] == " ":
    print(0)
    
else:
    if str_list[0] == " ":
      del str_list[0]

    if str_list[-1] == " ":
      del str_list[-1]


    print(str_list.count(" ") + 1)