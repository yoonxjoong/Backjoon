def solution(s, skip, index):
    answer = ''
    alphabet = alphabet = [chr(ord('a') + i) for i in range(26)]  # 소문자 알파벳
    characters_to_remove = list(skip)  # 제거하려는 문자 리스트

    # 리스트 컴프리헨션을 사용하여 characters_to_remove에 포함되지 않은 문자만 남김
    alphabet = [char for char in alphabet if char not in characters_to_remove]
    
    for character_to_find in s:
        tmp_index = alphabet.index(character_to_find)
        
        new_index = tmp_index + index   

        if new_index < len(alphabet):
            character_at_new_index = alphabet[new_index]
            # print(f"The character at index {new_index} is '{character_at_new_index}'")
            answer = answer + character_at_new_index
        else:
            new_index = new_index % len(alphabet)
            character_at_new_index = alphabet[new_index]
            # print(f"The character at index {new_index} is '{character_at_new_index}'")
            answer = answer + character_at_new_index

    return answer