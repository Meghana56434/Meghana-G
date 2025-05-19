def generate_series_modified(a: int):
    count = a if a % 2 != 0 else a - 1
    series = []
    for i in range(count):
        series.append(2 * i + 1)
    return series

a = int(input("Enter a number: "))
print(generate_series_modified(a))
