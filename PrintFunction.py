if __name__ == '__main__':
    n = int(input())
    list1 = []
    for i in range(1 , n+1):
        list1.append(i)
        
    print(''.join(map(str, list1)))  