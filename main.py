def quick_sort(lst, l, r):
  if r < l + 2:
    return 0

  i = l

  for j in range(l + 1, r):
    if lst[j] < lst[l]:
      i += 1
      lst[i], lst[j] = lst[j], lst[i]

  lst[l], lst[i] = lst[i], lst[l]

  quick_sort(lst, l, i)
  quick_sort(lst, i + 1, r)

with open('QuickSort.txt', 'r') as f:
  lines = f.readlines()

lst = [int(line.strip()) for line in lines]
quick_sort(lst, 0, len(lst))
print(lst)
