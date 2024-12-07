#Highridge Company Payment Slips
import random
# Step 1: list of random names
names_list = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", 
    "Ivan", "Jenna", "Kevin", "Laura", "Michael", "Nina", "Oscar", "Paula", 
    "Quinn", "Rachel", "Steve", "Tina", "Uma", "Victor", "Wendy", "Xander", 
    "Yvonne", "Zack", "idris","Tunde", "Momodu", "James", "Drinkwater"
]
def custom_random_uniform(min_rate, max_rate, step):
    """Generates a random value between min_rate and max_rate with a given step."""
    # Calculate the range of possible steps
    num_steps = int((max_rate - min_rate) / step) + 1
    # Choose a random step and calculate the value
    random_step = random.randint(0, num_steps - 1)
    return min_rate + (random_step * step)

for _ in range(5):  # Generate 5 random values for testing
    print(custom_random_uniform(80, 120, 5))  # Random value between 80 and 120 with step size of 5

# Step 2: Create a list of 400 workers dynamically
num_workers = 400
workers = [f"Worker_{i+1}" for i in range(num_workers)]

# Step 3: Assign random attributes for workers
worker_details = {
    worker: {
        "name": random.choice(names_list),  # Assign a random name
        "gender": random.choice(["Male", "Female"]),
        "hourly_rate": custom_random_uniform(80, 120, 5),  # Hourly rate between $80 and $120
        "hours_worked": random.randint(40, 60)  # Hours worked between 40 and 60
    }
    for worker in workers
}

# Step 4: Calculate weekly payments and determine employee level
for worker, details in worker_details.items():
    # Calculate weekly payment
    details["weekly_payment"] = round(details["hourly_rate"] * details["hours_worked"], 2)
    
    # Determine employee level based on conditions
    salary = details["weekly_payment"]
    gender = details["gender"]
    
    if 10000 < salary < 20000:
        details["employee_level"] = "A1"
    elif 7500 < salary < 30000 and gender == "Female":
        details["employee_level"] = "A5-F"
    else:
        details["employee_level"] = "Standard"

# Step 5: Generate payment slips
print("Highridge Construction Company - Weekly Payment Slips")
print("=" * 50)
for worker, details in worker_details.items():
    try:
        print(
            f"{worker} | Name: {details['name']} | Gender: {details['gender']} | "
                f"Hourly Rate: ${details['hourly_rate']:.2f} | Hours Worked: {details['hours_worked']} | "
                f"Weekly Payment: ${details['weekly_payment']:.2f} | Employee Level: {details['employee_level']}"
        )
    except KeyError as e:
        print(f"Missing data for {worker}: {e}")
    except Exception as e:
        print(f"Unexpected error while printing payment slip for {worker}: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Unexpected error in the program: {e}")