nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]

Iterator = iter(nums)

while True:
    try:
        numbers = next(Iterator)
        print(numbers)
    except:
        StopIteration
        break