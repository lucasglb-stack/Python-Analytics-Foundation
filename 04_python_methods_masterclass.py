"""
PYTHON CORE METHODS MASTERCLASS
Focus: Energy Sector & Financial Data Wrangling
Author: [Your Name]
"""

# =================================================================
# SECTION 1: DICTIONARY METHODS (Data Mapping & Safety)
# =================================================================

# Asset Inventory: Power Plants and their Capacity (MW)
assets = {
    'Alpha_Wind_Farm': 150.5,
    'Beta_Solar_Array': 88.0,
    'Gamma_Hydro_Plant': 225.3,
}

# Accessing data safely
# .get() avoids KeyError if the asset is missing
print(f"Capacity of Unknown: {assets.get('Delta_Plant', 'Not Registered')}")

# .setdefault() ensures a key exists with a default value
assets.setdefault('Epsilon_Thermal', 0.0)

# .update() merges new data into the existing dictionary
new_readings = {'Alpha_Wind_Farm': 160.0, 'Zeta_Biomass': 45.0}
assets.update(new_readings)

# Iterating with .items() (Unpacking)
print("\n--- Current Inventory ---")
for name, capacity in assets.items():
    print(f"Asset: {name:20} | Capacity: {capacity} MW")


# =================================================================
# SECTION 2: STRING METHODS (Data Sanitization & Formatting)
# =================================================================

# Simulating a "dirty" log entry from a CSV file
raw_log = "  2026_02_24 ; WIND_TURBINE_01 ; ACTIVE \n"

# Method Chaining: Clean, Split, and Standardize
cleaned_data = raw_log.strip().split(';')
print(f"Sanitized Data: {cleaned_data}")

# Validating File Formats
filename = "Financial_Report_Q1.PDF"
if filename.lower().endswith('.pdf'):
    print("Document format is valid.")

# Search and Count within Strings
description = "System status: Operational. All sensors operational."
print(f"Frequency of 'operational': {description.lower().count('operational')}")

# Replacing Characters
path = "C:/Users/Reports/Draft_V1"
final_path = path.replace("Draft_V1", "Final_Production")
print(f"New Path: {final_path}")

# =================================================================
# SECTION 3: NUMBER METHODS (Financial Precision)
# =================================================================

# Financial calculation precision
billing_amount = 4500.75

# .as_integer_ratio() returns the exact fraction representation
# Useful for high-precision economic modeling
print(f"Fractional Ratio: {billing_amount.as_integer_ratio()}") 

# .is_integer() checks if there is any decimal remainder
payment_received = 5000.0
print(f"Is full integer? {payment_received.is_integer()}") # True


# =================================================================
# SECTION 4: UTILITY - THE METHOD EXPLORER
# =================================================================
# Purpose: To inspect objects and list only usable (public) methods.

def explore_methods(obj):
    """
    Filters out internal Python attributes and returns 
    only the public methods of an object.
    """
    # We use a 'List Comprehension' to filter the dir() list
    # Logic: Keep the item ONLY if it does NOT start with '_'
    public_methods = [method for method in dir(obj) if not method.startswith('_')]
    
    print(f"\n--- Exploring Object Type: {type(obj).__name__} ---")
    print(f"Total Public Methods Found: {len(public_methods)}")
    print("-" * 40)
    
    # Printing the methods in a clean, organized way
    for i, method in enumerate(public_methods, 1):
        print(f"{i:02d}. {method}")

# --- Practical Example (Using a Dictionary) ---
energy_data = {'Plant_ID': 101, 'Status': 'Active'}
explore_methods(energy_data)

# --- Practical Example (Using a String) ---
report_name = "monthly_generation_report"
explore_methods(report_name)