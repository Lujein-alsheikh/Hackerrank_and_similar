if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    # print(arr)
    arr.sort()
    # print(arr)
    max_num = max(arr)
    arr = [x for x in arr if x != max_num]
    # print(arr)
    print(arr[len(arr)-1])