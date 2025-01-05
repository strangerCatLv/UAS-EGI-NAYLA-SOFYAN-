def merge_sort(orders):
    if len(orders) > 1:
        mid = len(orders) // 2
        left = orders[:mid]
        right = orders[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i]['time'] <= right[j]['time']:
                orders[k] = left[i]
                i += 1
            else:
                orders[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orders[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orders[k] = right[j]
            j += 1
            k += 1

orders = [
    {"id": 10, "pickup": "Paket", "destination": "Bogor", "time": "2025-01-05 10:59:00"},
    {"id": 2, "pickup": "Kulkas", "destination": "Jakarta", "time": "2025-01-05 08:00:00"},
    {"id": 34, "pickup": "Lemari", "destination": "Pamulang", "time": "2025-01-05 09:30:00"}
]
merge_sort(orders)
print(orders)


print("====================================================")
print("Egi Nayla Sofyan \n")
print("NIM : 2411100996")
