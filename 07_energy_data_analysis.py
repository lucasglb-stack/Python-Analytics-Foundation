
# Energy Data Analysis: List Comprehensions and Dictionary Updates

def analyze_energy_consumption():
    """
    Demonstrates list comprehensions and dictionary updates 
    using daily energy consumption data.
    """
    print("--- Energy Consumption Analysis (kWh) ---")
    
    # 1. Daily energy consumption readings in kWh for a week
    daily_kwh = [12.5, 8.0, 15.2, 22.1, 19.5, 9.3, 14.8]
    print(f"Original weekly readings (kWh): {daily_kwh}")
    
    # Filtering days with high consumption (greater than 15 kWh)
    high_consumption_days = [kwh for kwh in daily_kwh if kwh > 15]
    print(f"High consumption readings (>15 kWh): {high_consumption_days}")

    # 2. Applying operations: Calculating daily cost
    # Assuming a flat rate of $0.15 per kWh
    tariff_rate = 0.15
    daily_cost = [round(kwh * tariff_rate, 2) for kwh in daily_kwh]
    print(f"Estimated daily cost (USD): {daily_cost}")

    print("\n--- Power Plant Status Update Example ---")
    
    # 3. Managing and updating dictionaries for plant status
    plant_status = {
        "Hydroelectric Plant A": "Operational",
        "Wind Farm B": "Under Maintenance",
        "Solar Park C": "Operational",
        "Substation D": "Offline"
    }
    
    print(f"Before update: Substation D -> {plant_status['Substation D']}")
    
    # Updating the status using .update() method after a repair
    plant_status.update({"Substation D": "Operational"})
    
    print(f"After repair: Substation D -> {plant_status['Substation D']}")


if __name__ == "__main__":
    analyze_energy_consumption()