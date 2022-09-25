def raise_to_degrees(number, max_degree):
    i = 0
    while True:
        result = number**i
        yield result

        if result > 100**20:
            return
        i += 1

res = raise_to_degrees(123456, 500 )
print(res)

for _ in res:
    print(_)