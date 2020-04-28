import time

def three_days(data):

    result    = []
    yesterday = data[0]
    cnt_up    = 0
    cnt_down  = 0

    for d in data:
        if d - yesterday > 0:
            cnt_up += 1
            cnt_down = 0
        elif d - yesterday < 0: 
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


def three_days2(data): # 此作法執行效率較慢
    
    result = []

    for i in range(len(data)):
        if i < 3:
            result.append(0)
        else: 
            if data[i-3] < data[i-2] < data[i-1] < data[i]:
                result.append(1) # 連三漲
            elif data[i-3] > data[i-2] > data[i-1] > data[i]:
                result.append(-1) # 連三跌
            else:
                result.append(0) # 其他

    return result 

def main():
    data = [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368] * 1000000
    start = time.time()
    result = three_days(data)
    end = time.time()
    # print(result)
    print('Spent ', end-start, 'seconds')


main()    