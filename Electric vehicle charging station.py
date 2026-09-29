# Electric-vehicle-charging-station
import time

print("===================================")
print("     ELECTRIC VEHICLE CHARGER")
print("===================================")

# Input vehicle information
battery_capacity = float(input("Enter battery capacity (kWh): "))
current_charge = float(input("Enter current battery charge (%): "))
charging_power = float(input("Enter charger power (kW): "))

# Calculate remaining energy
remaining_percentage = 100 - current_charge
energy_required = battery_capacity * remaining_percentage / 100

# Calculate charging time
charging_time_hours = energy_required / charging_power

print("\n-----------------------------------")
print("Charging Information")
print("-----------------------------------")
print(f"Battery Capacity : {battery_capacity:.2f} kWh")
print(f"Current Charge   : {current_charge:.1f}%")
print(f"Charger Power    : {charging_power:.2f} kW")
print(f"Energy Required  : {energy_required:.2f} kWh")
print(f"Estimated Time   : {charging_time_hours:.2f} hours")

# Start charging
start = input("\nStart charging? (yes/no): ").lower()

if start == "yes":
    print("\nCharging started...")

    charge = current_charge

    while charge < 100:
        time.sleep(1)

        # Simulate charging
        charge += (charging_power / battery_capacity) * 2

        if charge > 100:
            charge = 100

        print(f"Battery Level: {charge:.1f}%")

    print("\n===================================")
    print("Charging completed!")
    print("Please disconnect the vehicle.")
    print("===================================")

else:
    print("\nCharging cancelled.")
