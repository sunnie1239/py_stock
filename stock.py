def three_days(data):

    result    = []
    yesterday = data[0]
    cnt_up    = 0
    cnt_down  = 0

    for d in data:
        if d - yesterday > 0: # 漲
            cnt_up += 1
            cnt_down = 0
        elif d - yesterday < 0: # 跌
            cnt_up = 0
            cnt_down += 1
        else: # 持平
            cnt_up = 0
            cnt_down = 0

        yesterday = d    

        if cnt_up >= 3 and cnt_down == 0:
            result.append(1) # 連三漲
        elif cnt_down >= 3 and cnt_up == 0:
            result.append(-1) # 連三跌
        else:
            result.append(0) # 其他

    return result           


def main():
    data = [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368]
    result = three_days(data)
    print(result)


main()    