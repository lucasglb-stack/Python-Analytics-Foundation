"""
08_functions_and_standard_libs.py
A comprehensive guide to Python functions, parameters, the None keyword, 
module imports, and standard libraries applied to energy sector scenarios.
"""

# ==========================================
# 1. BUILT-IN & CUSTOM FUNCTIONS
# ==========================================

# Simple function to step up voltage
def step_up_voltage(v):
    return v + 2.0

result = step_up_voltage(3.0)
print(f"Adjusted Voltage: {result} kV")  # Output: 5.0 kV
print(f"Negative adjustment: {step_up_voltage(-2.9):.1f} kV")  # Output: -0.9 kV

# Function to calculate the sweep area of a wind turbine
def calculate_turbine_area(blade_radius):
    import math # Importing inside a function is possible, though usually done at the top
    return math.pi * (blade_radius ** 2)

area = calculate_turbine_area(50)
print(f"Turbine area: {area:.2f} sqm")  


# Function to concatenate strings (e.g., creating asset IDs)
def combine_asset_data(part1, part2):
    return part1 + part2

print(combine_asset_data("SUB_", "A45"))  # Output: SUB_A45
print(combine_asset_data(10, 20))         # Output: 30 (Polymorphism in Python)


# ==========================================
# 2. PARAMETERS AND ARGUMENTS
# ==========================================

def calculate_efficiency(output_mwh, input_mwh):
    if input_mwh == 0:
        return "Error: Cannot divide by zero (Input energy is 0)"
    return output_mwh / input_mwh

print(calculate_efficiency(10, 2))      # Output: 5.0
print(calculate_efficiency(output_mwh=10, input_mwh=2)) # Keyword arguments
print(calculate_efficiency(10, 0))      # Output: Error message

# Default Parameters
def tag_status(asset_name, status=" [OPERATIONAL]"):
    return asset_name + status

print(tag_status("Turbine 01", " [MAINTENANCE]"))
print(tag_status("Turbine 02")) # Uses default status


def calculate_total_load(zone_a=0, zone_b=0, zone_c=0, zone_d=0):
    return zone_a + zone_b + zone_c + zone_d

print(f"Total Load: {calculate_total_load(zone_c=34)} MW")  # Output: 34 MW


# ==========================================
# 3. THE 'NONE' VALUE
# ==========================================

def log_system_startup():
    print("System starting up...")

# A function without a return statement returns None
return_value = log_system_startup()
print(return_value)  # Output: None

# None is often used to handle missing data gracefully
energy_prices = {
    "solar": 45.5,
    "wind": 38.0,
    "hydro": 30.2
}

print(energy_prices.get("nuclear"))  # Output: None
print(type(None))                    # Output: <class 'NoneType'>

# In-place methods usually return None
active_substations = [1, 2, 3, 4, 5]
return_value = active_substations.append(6)
print(return_value)  # Output: None
print(active_substations)  # Output: [1, 2, 3, 4, 5, 6]

# Unlike string methods, which return a new object
status_text = "offline"
return_text = status_text.upper()
print(return_text)  # Output: OFFLINE


# ==========================================
# 4. MODULE IMPORTS (Examples)
# ==========================================
# Note: These are commented out to prevent ModuleNotFoundError when running this script.
# Assuming you have a file named 'financial_module.py' with a variable 'tax_rate' and function 'calc_tax()'

# Method 1: Standard import
# import financial_module
# print(financial_module.calc_tax())
# print(financial_module.tax_rate)

# Method 2: Importing specific parts
# from financial_module import calc_tax, tax_rate

# Method 3: Importing everything (Not recommended - pollutes namespace)
# from financial_module import *

# Method 4: Using an alias for the module
# import financial_module as fm
# print(fm.calc_tax())

# Method 5: Using aliases for functions and variables
# from financial_module import calc_tax as ct, tax_rate as tr


# ==========================================
# 5. PYTHON STANDARD LIBRARIES
# ==========================================

import math
print(f"Pi: {math.pi}")
print(f"Base-2 Logarithm of 16: {math.log(16, 2)}")  # Output: 4.0


import datetime
now = datetime.datetime.now()
print(f"Current Date and Time: {now}")

market_deregulation_date = datetime.datetime(2000, 1, 1)
time_difference = now - market_deregulation_date

print(f"Days since market deregulation: {time_difference.days} days")


import random
print("Random daily demand fluctuation (MW):")
for _ in range(3):
    print(random.randint(-10, 10))  

assets = ["Substation Alpha", "Substation Beta", "Wind Farm Charlie"]
print(f"Random asset selected for inspection: {random.choice(assets)}")


import os
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}") 
# print(os.listdir(current_directory)) # Lists files and folders in the current directory


import time
print("Initiating sensor reboot countdown...")
start_time = time.time()

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)  # Pauses execution for 1 second

end_time = time.time()
execution_time = end_time - start_time
print(f"Reboot complete. Execution time: {execution_time:.2f} seconds")