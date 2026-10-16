# =========================================================
# VICTORIA UNIVERSITY KAMPALA
# PYTHON FOR DATA SCIENCE - COURSE WORK 1
# Student: KAMWADA MUSA HIIRE
# Reg No: VU-BAD-2607-2558-DAY
# File: Musa.py - Contains everything
# =========================================================

# ---------------- ONE: IF ELSE & NESTED CONDITIONS ----------------
print("--- TASK 1: CONDITIONALS ---")
age = 20
licence = True

# Simple if-else
if age >= 18:
    print("Adult: Eligible to vote")
else:
    print("Child: Not eligible")

# Nested if with and
if age >= 18:
    if licence == True:
        print("Eligible to drive")
    else:
        print("Age OK but no licence")
else:
    print("Underage, not eligible")

# Edge case check
if age < 0 or age > 120:
    print("Invalid age")
else:
    print(f"Valid age: {age}")

# Grade classification nested if
score = 82
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 75:
    print("Distinction")
elif score >= 60:
    print("Credit")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

# ---------------- ONE: LOOPS (FOR, WHILE) & ITERATION ----------------
print("\n--- TASK 2: LOOPS ---")

# For loop with iteration over list
ages = [12, 18, 25, 16, 30]
for i, a in enumerate(ages, 1):
    print(f"{i}. Age {a}")

# For loop with break
for a in ages:
    if a == 16:
        print("Found 16, stopping loop")
        break
    print(f"Checking age {a}")

# While loop
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Launch!")

# Iteration over tuple
subjects = ('Python', 'Pandas', 'SQL', 'Statistics')
for sub in subjects:
    print(f"Subject: {sub}")

# ---------------- TWO: FUNCTIONS & MODULAR PROGRAMMING ----------------
print("\n--- TASK 3: FUNCTIONS ---")

def add_numbers(a, b):
    """Adds two numbers - modular programming"""
    return a + b

def is_even(n):
    """Check if even"""
    return n % 2 == 0

def check_age_group(age):
    """Returns age group using nested if - modular"""
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

# Test functions
print(f"add_numbers(5,3) = {add_numbers(5,3)}")
print(f"is_even(18) = {is_even(18)}")

# Function that uses loop internally (modular)
def predict_grades(scores):
    for s in scores:
        print(f"Score {s} -> {check_age_group(s)}")

test_scores = [12, 18, 25, 16, 30]
for age_val in test_scores:
    print(f"Age {age_val} is {check_age_group(age_val)}")

# ---------------- TWO: RECURSION ----------------
print("\n--- TASK 4: RECURSION ---")

def factorial_recursive(n):
    """Recursion example: factorial"""
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(f"factorial_recursive(5) = {factorial_recursive(5)}") # 120

def factorial_loop(n):
    """Same using loop for comparison"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(f"factorial_loop(5) = {factorial_loop(5)}")

# ---------------- TWO: LAMBDA FUNCTIONS ----------------
print("\n--- TASK 5: LAMBDA ---")

# Simple lambda
x = lambda a: a * 2
print(f"lambda a*2 with 5 = {x(5)}")

# Lambda with filter - get adults
ages = [12, 18, 25, 16, 30]
adults = list(filter(lambda a: a >= 18, ages))
print(f"Adults (filter >=18): {adults}")

# Lambda with map - get birth years
birth_years = list(map(lambda a: 2026 - a, ages))
print(f"Birth years (map 2026-age): {birth_years}")

# Lambda with sorted
sorted_ages = sorted(ages, key=lambda a: a)
print(f"Sorted ages: {sorted_ages}")

# ---------------- EXTRA: LISTS, TUPLES, SETS, DICTIONARIES ----------------
print("\n--- TASK 6: LISTS, TUPLES, SETS, DICTS ---")

# LISTS - mutable, ordered
my_list = [12, 18, 25, 16, 30]
print(f"Original list: {my_list}")
my_list.append(22)
print(f"After append(22): {my_list}")
my_list.remove(16)
print(f"After remove(16): {my_list}")
# List comprehension
adult_list = [a for a in my_list if a >= 18]
print(f"List comp adults: {adult_list}")

# TUPLES - immutable, ordered
age_tuple = (18, 20, 22)
print(f"Tuple: {age_tuple}")
print(f"Tuple[0] = {age_tuple[0]}")
# Tuples cannot be changed - age_tuple[0]=99 will error

# SETS - unique, unordered, no duplicates
unique_ages = {18, 20, 18, 25, 20}
print(f"Set (duplicates removed): {unique_ages}")
unique_ages.add(30)
print(f"After add(30): {unique_ages}")

# DICTIONARIES - key-value pairs
age_dict = {'Musa': 22, 'John': 18, 'Sara': 16}
print(f"Dict: {age_dict}")
print(f"age_dict['Musa'] = {age_dict['Musa']}")

# Iteration over dict
for name, age_val in age_dict.items():
    print(f"{name} is {age_val} years -> {check_age_group(age_val)}")

# Dict comprehension
adult_dict = {k:v for k,v in age_dict.items() if v >= 18}
print(f"Dict comp adults: {adult_dict}")

print("\n--- END OF PROGRAM ---")
print("All concepts practiced successfully!")
