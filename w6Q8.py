def zip_lists(list1, list2):
    zipped_list = [row1 + row2 for row1, row2 in zip(list1, list2)]
    return zipped_list

def main():
    m = int(input())
    n = int(input())
    list1 = []
    for _ in range(m):
        inner_list = []
        for _ in range(n):
            inner_list.append(int(input()))
        list1.append(inner_list)
    list2 = []
    for _ in range(m):
        inner_list = []
        for _ in range(n):
            inner_list.append(int(input()))
        list2.append(inner_list)
    zipped_list = zip_lists(list1, list2)
    print(zipped_list)

if __name__ == "__main__":
    main()     
