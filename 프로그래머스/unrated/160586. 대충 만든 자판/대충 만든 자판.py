def solution(keymap, targets):
    answer = []
    key_dict = {}
    print(keymap)
    
    for i in keymap:
        for index, j in enumerate(i):
            if key_dict.get(j) == None:
                key_dict.update({j : index})
            else:
                key_dict.update({j : min(key_dict.get(j), index)})
        
    for i in targets:
        tmp_value = 0
        for j in i:
            if key_dict.get(j) == None:
                tmp_value = -1
            else:
                if tmp_value != -1:
                    tmp_value += key_dict.get(j) + 1
        answer.append(tmp_value)
        

    return answer