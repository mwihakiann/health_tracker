# Daily Health Habit Tracker

def get_health_data():
    print("\nEnter today's health data:")
    water_intake = input("How many glasses of water did you drink today? ")
    steps_walked = input("How many steps did you walk today? ")
    sleep_hours = input("How many hours did you sleep last night? ")
    
    return water_intake, steps_walked, sleep_hours

def display_health_summary(water, steps, sleep):
    print("\n--- Health Summary for Today ---")
    print(f"Water Intake: {water} glasses")
    print(f"Steps Walked: {steps} steps")
    print(f"Sleep Hours: {sleep} hours")
    
    if int(water) < 8:
        print("Tip: Drink more water! Aim for 8 glasses a day.")
    if int(steps) < 10000:
        print("Tip: Try to walk at least 10,000 steps daily.")
    if int(sleep) < 8:
        print("Tip: Aim for 7-9 hours of sleep each night.")

def main():
    print("Welcome to the Daily Health Habit Tracker!")
    
    # Get health data from the user
    water_intake, steps_walked, sleep_hours = get_health_data()
    
    # Display the health summary
    display_health_summary(water_intake, steps_walked, sleep_hours)

if __name__ == "__main__":
    main()
