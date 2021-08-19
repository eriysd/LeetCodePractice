# best O(nlogn), average O(nlogn), worst O(n^2)

def quickSort(s: list, lower, upper):
    if lower < upper:
        pivot = s[upper]
        left = lower - 1
        right = lower

        while right < upper:
            if s[right] < pivot:
                left += 1
                s[left], s[right] = s[right], s[left]
            right += 1

        s[left + 1], s[upper] = s[upper], s[left + 1]

        quickSort(s, lower, left)
        quickSort(s, left + 2, right)


s = [5, 7, 1, 3, 9, 0]
quickSort(s, 0, len(s)-1)
print(s)
