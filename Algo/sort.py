class sort:
    def BubbleSort(self, data):
        for i in range (len(data)):
            for j in range (len(data)-1):
                if data[j] > data[j+1]:
                   data[j], data[j+1] = data[j+1], data[j]

    def SelectionSort(self, data):
            for i in range(len(data)-1):
                min = i
                for j in range(i + 1, len(data)):
                    if data[j] < data[min]:
                        min = j
                data[i], data[min] = data[min], data[i]

    def InsertionSort(self, data):
             n = len(data)
             for i in range(1, n):
                 key = data[i]
                 j = i - 1
                 while (j >= 0 and key < data[j]):
                    data[j + 1] = data[j]
                    j -= 1
                 data[j + 1] = key

data = [10,17,4,1]
sort = sort()
sort.InsertionSort(data)
print(data)