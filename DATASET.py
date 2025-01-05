def dataKu(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = dataKu(dataset, target)
print(f'Target ditemukan di indeks: {result}' if result != -1 else 'Target tidak ditemukan.')

print("====================================================")
print("Egi Nayla Sofyan \n")
print("NIM : 2411100996")
