list1 = list(map(int, input("Input array pertama: ").split()))
list2 = list(map(int, input("Input array kedua: ").split()))

print(f"\nArray Pertama: {list1}")
print(f"Array Kedua: {list2}")

sama = set(list1).intersection(list2)

print(f"\nTerdapat {len(sama)} duplikasi {sama}")