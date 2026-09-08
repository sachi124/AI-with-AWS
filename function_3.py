# The basics
def greet_user(name):
    return f"Hello, {name}!"

name = "Sachin Bista"
print(greet_user(name))

# The intermediate
# Default arg and type hinting
# 'discount' set 0 if not provided
def calculate_total(price: float, discount: float=0.0) -> float:
    return price - (price * discount)

print(calculate_total(100.0))
print(calculate_total(100.0, 0.15))

# Arbitrary Arguements
# When we don't know how many input?, use *args (tuples) and **kwags (dict)
def build_pizza(size: str, *toppings, **details):
    print(f"Size: {size}")
    print(f"Toppings: {toppings}")
    print(f"Delivery Details: {details}")

pizza = build_pizza('large', 'Pepperoni', 'Mushrooms', 'Olives', address= "Chabahil Kathmandu", rush=True)
print(pizza)

# The rule of ordering: Where does **kwags go?
def correct_func(a, b, **kwags):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Kwargs: {kwags}")

Sachin = correct_func(1,2, c = 14, d = 22)
print(Sachin)

# 2. Unpacking Elements
def add_three(a, b, c):
    return a + b + c

my_tuple = (1, 2)
my_dict = {'c': 22}

# *(1,2) explode the tuple into 1, 2
# **('sachin': 22) explode dict into {'sachin': 22}
result = add_three(*my_tuple, **my_dict)
print(result)

# Creating forced Keywords Arguments
def calculate_avg(*number, strict_mode):
    total = sum(number)
    if strict_mode:
        print("Running in strict verification mode...")
    return total / len(number)

result = calculate_avg(10, 20, 30, 40, 50, strict_mode=True)
print(result)


# 4. Overlapping Arguements: The Double Binding Trap
def configure_system(status, timeout):
    return f"System status: {status}, Timeout: {timeout}"

extra_settings = {"status": "Inactive", "timeout": 100}
# print(extra_settings)

# 5. Perfect forwarding (the decorator pattern)
# you combine define packing and call unpacking
def complex_math_operation(x, y, multiplier):
    return (x + y) * multiplier

def logging_wrapper(func, *args, **kwargs):
    # 1. *args and **kwargs PACK everything sent into a tuple and dict
    print(f"Intercepted poitional items: {args}")
    print(f"Intercepted keyword items: {kwargs}")

    # 2. We use * and ** again to UNPACK them perfectly into the target function
    result = func(*args, **kwargs)
    print(f"✅ Execution finished. Result: {result}")
    return result

# let's wrap our math function
logging_wrapper(complex_math_operation, 5, 10, multiplier=2)



