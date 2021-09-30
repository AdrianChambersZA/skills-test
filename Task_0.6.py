def maximum(*numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

maximum(1, 22, 3, 2)