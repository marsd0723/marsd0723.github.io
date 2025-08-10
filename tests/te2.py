import time

SIZE = 16
arr = [0] * SIZE
sum_ = 0

start = time.time()

for i in range(10000000):
    sum_ += i
    arr[i % SIZE] = (arr[i % SIZE] + (sum_ & 0xFF)) % 100

end = time.time()

arr_sum = sum(arr)

print("Sum:", sum_)
print("Array checksum:", arr_sum)
print("Time:", end - start, "seconds")
