import random

pincode_short_digit_1 = random.randint(0, 9)
pincode_short_digit_2 = random.randint(0, 9)
pincode_short_digit_3 = random.randint(0, 9)

pincode_long_digit_1 = random.randint(1, 6)
pincode_long_digit_2 = random.randint(1, 6)
pincode_long_digit_3 = random.randint(1, 6)
pincode_long_digit_4 = random.randint(1, 6)

print(pincode_short_digit_1, pincode_short_digit_2, pincode_short_digit_3)
print(pincode_long_digit_1, pincode_long_digit_2, pincode_long_digit_3, pincode_long_digit_4)
