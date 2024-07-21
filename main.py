def quick_sort(lst: List[int], l: int, r: int) -> None:
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
