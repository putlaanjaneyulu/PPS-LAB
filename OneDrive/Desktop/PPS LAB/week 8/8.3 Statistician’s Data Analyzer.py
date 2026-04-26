def mean(data):
    return sum(data) / len(data)
def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:  # Odd number of elements
        return sorted_data[mid]
    else:  # Even number of elements
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
def mode(data):
    frequency = {}
    for num in data:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_count = max(frequency.values())
    for key in frequency:
        if frequency[key] == max_count:
            return key
n = int(input())
data = list(map(int, input().split()))
mean_value = mean(data)
median_value = median(data)
mode_value = mode(data)
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
