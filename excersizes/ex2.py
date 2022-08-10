def generate_arm_strong(num_test):
    for num in range(0, num_test + 1):
        test = num
        total_sum = 0
        while test > 0:
            digit = test % 10
            total_sum = total_sum + digit ** 3
            test = test // 10

        if total_sum == num:
            yield num


number = int(input("Enter test number: "))
iterator = generate_arm_strong(number)

for item in iterator:
    if item == number:
        print(f"{number} is armstrong")
        break
else:
    print(f"{number} is not armstrong")