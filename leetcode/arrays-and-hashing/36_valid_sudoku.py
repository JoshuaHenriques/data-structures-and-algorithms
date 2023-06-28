def isValidSudoku(self, board: List[List[str]]) -> bool:
    hashmap = defaultdict(list)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ".":
                hashmap[board[i][j]].append([i,j])

    for v in hashmap.values():
        if len(v) == 1:
            continue

        for i in range(len(v)):
            for j in range(i+1, len(v)):
                print(f'v[i]: {v[i]}')
                print(f'v[j]: {v[j]}')
                if v[i][0] == v[j][0]:
                    return False
                elif v[i][1] == v[j][1]:
                    return False
                elif 0 <= v[i][0] < 3 and 0 <= v[j][0] < 3:
                    if 0 <= v[i][1] < 3 and 0 <= v[j][1] < 3:
                        return False
                    elif 3 <= v[i][1] < 6 and 3 <= v[j][1] < 6:
                        return False
                    elif 6 <= v[i][1] <= 8 and 6 <= v[j][1] <= 8:
                        return False  
                elif 3 <= v[i][0] < 6 and 3 <= v[j][0] < 6:
                    if 0 <= v[i][1] < 3 and 0 <= v[j][1] < 3:
                        return False
                    elif 3 <= v[i][1] < 6 and 3 <= v[j][1] < 6:
                        return False
                    elif 6 <= v[i][1] <= 8 and 6 <= v[j][1] <= 8:
                        return False 
                elif 6 <= v[i][0] <= 8 and 6 <= v[j][0] <= 8:
                    if 0 <= v[i][1] < 3 and 0 <= v[j][1] < 3:
                        return False
                    elif 3 <= v[i][1] < 6 and 3 <= v[j][1] < 6:
                        return False
                    elif 6 <= v[i][1] <= 8 and 6 <= v[j][1] <= 8:
                        return False 
    return True