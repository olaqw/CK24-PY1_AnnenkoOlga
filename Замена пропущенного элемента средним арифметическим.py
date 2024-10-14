numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_of_numbers = sum(numbers[:4])+sum(numbers[5:])
numbers[4] = round(sum_of_numbers / len(numbers), 2)

print("Измененный список:", numbers)
