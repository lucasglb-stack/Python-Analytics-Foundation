"""
Topic: Python Loops (For/While)
Purpose: Automating energy asset monitoring and financial report formatting.
"""

# --- Section 1: For Loops with Numerical Ranges ---
# Simulating a 12-month budget forecast review
print("--- Monthly Budget Review ---")
for month_index in range(1, 13):
    # Using f-strings with padding for clean reporting
    print(f"Analyzing Fiscal Month: {month_index:02d}") #using 02d for 2 digits, like 01 to 12


# --- Section 2: Iterating with Conditionals (Replacing Guess Game) ---
# Scenario: Monitoring energy spot prices. 
# We loop through a series of price points until a budget threshold is exceeded.
price_threshold = 150.00  # R$/MWh or USD/MWh
spot_prices = [120.5, 135.2, 148.0, 160.5, 142.0]

print("\n--- Market Price Alert System ---")
for price in spot_prices:
    if price > price_threshold:
        print(f"ALERT: Spot price {price} exceeds threshold {price_threshold}!")
        # In a real scenario, we could trigger a 'break' or a notification here
    else:
        print(f"Market price stable: {price}")


# --- Section 3: Data Unpacking (The "Senior" Way) ---
# Scenario: Managing a portfolio of Energy Assets (Power Plants)
# Structure: (Asset Name, Capacity MW, Operational Status)
energy_assets = [
    ('Solar Plant Alpha', 50.5, 'Active'), 
    ('Wind Farm Beta', 120.0, 'Maintenance'), 
    ('Hydro Delta', 450.8, 'Active')
]

print("\n--- Energy Asset Portfolio Report ---")

# Best Practice (Option 3): Direct Unpacking in the Loop
# This is the most readable and "Pythonic" approach for international teams
for name, capacity, status in energy_assets:
    print(f"Asset: {name:18} | Capacity: {capacity:>6} MW | Status: {status}")

print("\nReport Generation Complete.")

# --- Section 4: Data Unpacking (The "Senior" Way) ---

