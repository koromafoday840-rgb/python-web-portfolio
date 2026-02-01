#for number in range(10, 0, -1):
 # print(number)
#count_sum = 0
#for number in range(2, 21, 2):
#  count_sum += number
 # print(count_sum)

#for number in range (10, 0, -1):
  
 # print(number)


#for i in (1, 2 ,3 ,4 ,5):
#
#names = 'Foday', 'John', 'Marie' 
#scores = 90,76,89,45

#for name in names:
 # for score in scores:
# Python Web Portfolio
def validate_user_data(age_text, payment_received):
    """
    Demonstrates type safety by converting string input to integers.
    This pattern is used to handle real-world input safely.
    """
    # Typecasting string to int for calculation
    current_age = int(age_text)
    next_year_age = current_age + 1
    
    return f"Next year you will be {next_year_age}."

# Proving Case Sensitivity Logic
price = 100
Tax = 0.05
# total = price + tax  <-- This would fail (NameError)
total = price + (price * Tax)
print(f"The calculated total with tax is: {total}")