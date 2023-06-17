def solution(players, callings):
    index_dict = {idx: player for idx, player in enumerate(players)}
    value_dict = {player: idx for idx, player in enumerate(players)}

    for calling in callings:
        index = value_dict[calling]
    
        tmp_index = index_dict[index - 1]
        tmp_value = index_dict[index - 1]
        index_dict[index - 1] = calling
        index_dict[index] = tmp_index
        
        value_dict[calling] -= 1
        value_dict[tmp_value] += 1
        
      
    
    return list(index_dict.values())
