def main():
    data_s = input().split()
    data = [int(x) for x in data_s]

    right_idx = [i for i in range(1, len(data))]
    right_idx.append(0)

    data_in = int(input())

    for i in range(len(right_idx)):
        if right_idx[i] == 0:
            data.append(data_in)
            right_idx[i] == len(data) - 1
            right_idx.append(0)
            break
        
        if data[right_idx[i]] > data_in:
            data.append(data_in)
            temp = right_idx[i]
            right_idx[i] = len(data) - 1
            right_idx.append(temp)
            break
    
    print(data[0], end=" ")
    cur = right_idx[0]
    while cur != 0:
        print(data[cur], end=" ")
        cur = right_idx[cur]
    # for idx in right_idx:
    #     if idx != 0:
    #         print(data[idx], end=" ")


if __name__ == "__main__":
    main()