st_number = int(input("please enter the starting number: "))
end_number = int(input("please enter the ending number: "))
# convert inputs to int before arithmetic; ensure the upper bound adds 1 to the integer value
sum_range = sum(range(st_number, end_number + 1))
print(f"the sum of number from {st_number} to {end_number} is: {sum_range}")