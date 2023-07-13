# time limit exceeded 321/322 testcases passed
def trap(self, height: List[int]) -> int:
        i, res = 0, 0
        while i < len(height):
            if i == 0:
                while i < len(height) and height[i] == 0:
                    i += 1

            if i >= len(height):
                break

            if len(height[:i]) == 0:
                left_side = 0
            else:
                left_side = max(height[:i])

            if len(height[i:]) == 0:
                right_side = 0
            else:
                right_side = max(height[i:])

            trapped = min(left_side, right_side) - height[i]
            if trapped > 0:
                res += trapped

            i += 1

        return res

# time limit exceeded 321/322 testcases passed
def trap1(self, height: List[int]) -> int:
    # Algo min(l, r) - height[i]
    max_left = [0] * len(height)
    m_l = 0
    max_right = [0] * len(height)
    m_r = 0
    min_lr = [0] * len(height)
    m_lr = 0

    j = len(height) - 1
    for i in range(len(height)):
        if i == 0:
            continue

        m_l = max(height[0:i])
        max_left[i] = m_l

        m_r = max(height[len(height)-i:len(height)])
        max_right[len(height)-i-1] = m_r

    for i in range(len(height)):
        m_lr = min(max_left[i], max_right[i])
        min_lr[i] = m_lr

    water = 0
    for i in range(len(height)):
        x = min_lr[i] - height[i]
        if x > 0:
            water += x
        print(f'water: {water}, x: {x}, min_lr[i]: {min_lr[i]}, height[i]: {height[i]}')

    return water

def trap3(self, height: List[int]) -> int:
    # Algo min(l, r) - height[i]
    max_l, max_r, water = 0, 0, 0
    i, j = 0, len(height) - 1

    while i <= j:
        if max_l <= max_r:
            max_l = max(max_l, height[i])   
            print(f'max_l: {max_l}')
            print(f'height[i]: {height[i]}')
            if max_l - height[i] > 0:
                water += max_l - height[i]
                print(f'left water: {water}')
            
            i +=1
        else:
            max_r = max(max_r, height[j])
            print(f'max_r: {max_r}')

            if max_r - height[j] > 0:
                water += max_r - height[j]
                print(f'right water: {water}')

            j -= 1
    
    return water