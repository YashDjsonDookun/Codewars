def solution(number):
    three = [] # Stores multiples of 3
    five = [] # Stores multiples of 5
    #Find multiples of 3
    for i in range(number):
        three.append(i*3)
    #Find multiples of 5
    for i in range(number):
        five.append(i*5)
    #Combine all multiples
    numbers = three + five
    #Remove duplicates if any by converting list into dictionary
    numbers = list(dict.fromkeys(numbers))
    sum_of_all_multiples_below_number = 0
    # Adds all the multiples (that are less than number) from the dictionary
    for i in range(len(numbers) - 1):
        if (numbers[i] < number):
            sum_of_all_multiples_below_number = sum_of_all_multiples_below_number + numbers[i]
    return sum_of_all_multiples_below_number
#example, let number = 23
print(solution(23))


# Best Answer:
'''
    def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
'''