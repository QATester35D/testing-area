# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return "List is empty"
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return int(average)

numbers = [10, 20, 30, 40, 50]
print("The average is ", calculate_average(numbers))
