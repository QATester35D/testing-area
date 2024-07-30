# Function to find the maximum number in a list
def find_max(numbers):
    if len(numbers) == 0:
        return "List is empty"
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [5, 3, 8, 2, 7]
print("The maximum number is: ", find_max(numbers))
