"""
Topic: Data Aggregation and Sequence Comparison
Purpose: Manual implementation of sum, average, and peak detection for energy monitoring.
"""

# --- Section 1: Manual Aggregation (Generation Analysis) ---
# Scenario: Calculating total and average energy generation (MWh) without built-in functions.
daily_generation_mwh = range(10, 100, 10)  # Simulated hourly generation
total_mwh = 0

for value in daily_generation_mwh:
    total_mwh += value

# Calculating average manually
count_readings = len(daily_generation_mwh)
average_generation = total_mwh / count_readings

print("--- Energy Generation Report ---")
print(f"Total Daily Generation: {total_mwh} MWh")
print(f"Average Generation: {average_generation:.2f} MWh/h\n")


# --- Section 2: Peak Detection (Grid Load Monitoring) ---
# Scenario: Finding the peak load reading in a sequence without max().
load_readings = [145.2, 167.8, 210.5, 189.0, 205.4, 155.1]
peak_load = load_readings[0]

for reading in load_readings:
    if reading > peak_load:
        peak_load = reading

print("--- Grid Load Analysis ---")
print(f"Peak Load Detected: {peak_load} MW\n")


# --- Section 3: Technical Term Filtering ---
# Scenario: Filtering technical keywords for report formatting (Min 5 characters).
sector_keywords = ('energy', 'MWh', 'generation', 'USD', 'power', 'grid')

print("--- High-Level Sector Keywords ---")
for word in sector_keywords:
    if len(word) >= 5:
        print(f"Keyword: {word}")


# --- Section 4: System Reconciliation (Comparing Asset Lists) ---
# Scenario: Checking for common Asset IDs across two different regional databases.
regional_grid_A = ['TX-990', 'FL-120', 'CA-550', 'NY-880']
regional_grid_B = ['WA-330', 'CA-550', 'OR-110', 'TX-990']

print("\n--- Asset Reconciliation ---")
common_assets_found = 0

for asset in regional_grid_A:
    if asset in regional_grid_B:
        print(f"Match Found: Asset {asset} is registered in both grids.")
        common_assets_found += 1

print(f"Total matching assets: {common_assets_found}")


# --- Section 5: Audit Flag (Efficiency Check) ---
# Scenario: Quick check to see if there is ANY overlap between systems.
system_audit_A = ('SmartMeter_01', 'SmartMeter_05', 'SmartMeter_09')
system_audit_B = ('SmartMeter_02', 'SmartMeter_05', 'SmartMeter_10')

has_overlap = False
for meter in system_audit_A:
    if meter in system_audit_B:
        has_overlap = True
        break # Optimized: stops as soon as the first match is found

if has_overlap:
    print("\n[AUDIT] Warning: Duplicate meter IDs detected across systems.")
else:
    print("\n[AUDIT] Success: No overlapping meter IDs found.")