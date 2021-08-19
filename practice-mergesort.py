# best O(nlogn), average O(nlogn), worst O(nlogn)

def mergeSort(s: list):
    if len(s) > 1:
        middle = len(s)//2
        left = s[:middle]
        right = s[middle:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                s[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                s[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            s[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            s[k] = right[j]
            j += 1
            k += 1


s = [5, 7, 1, 3, 9, 0]
mergeSort(s)
print(s)
