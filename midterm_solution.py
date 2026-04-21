# DORM ROOM CHORE TRACKER

# Parallel lists for chores and frequencies
chore_names = ["Sweeping / Mopping", "Dishwashing", "Taking Out Trash", "Cleaning Bathroom", "Buying Groceries"]
chore_frequencies = ["Daily", "After meals", "Every other day", "Weekly", "Weekly"]

# Get room monitor name with validation
monitor_name = ""
while monitor_name == "":
    monitor_name = input("Room monitor name: ")
    
    # Check if empty
    if monitor_name == "":
        print("Invalid: Please enter a name (cannot be empty)")
        continue
    
    # Trim whitespace
    monitor_name = monitor_name
    
    # Check if empty or all spaces
    if monitor_name == "":
        print("Invalid: Please enter a name (cannot be empty or spaces only)")
        monitor_name = ""
        continue
    
    # Check for invalid characters
    has_invalid = False
    for char in monitor_name:
        is_letter = (char >= "a" and char <= "z") or (char >= "A" and char <= "Z")
        is_space = (char == " ")
        if not is_letter and not is_space:
            has_invalid = True
    
    if has_invalid:
        print("Invalid: Name should contain only letters and spaces (no numbers or symbols)")
        monitor_name = ""
        continue
    
    # Split and validate full name parts
    name_parts = monitor_name

    # Allow at least one name (first name only is OK)
    if len(name_parts) < 1:
        print("Invalid: Please enter at least a first name")
        monitor_name = ""
        continue
    
    # Check that each part of the name has at least 2 letters
    valid_parts = all(len(part) >= 2 for part in name_parts)
    if not valid_parts:
        print("Invalid: Each part of the name must be at least 2 letters")
        monitor_name = ""
        continue


# Get room number with validation (must have both letters and numbers)
room_number = ""
while room_number == "":
    room_number = input("Room number: ")
    
    # Check if empty
    if room_number == "":
        print("Invalid: Please enter a room number (cannot be empty)")
        continue
    
    # Check if starts with 0 followed by number
    if len(room_number) >= 2:
        if room_number[0] == "0":
            second_char = room_number[1]
            if second_char >= "0" and second_char <= "9":
                print("Invalid: Room number cannot start with 0 followed by another number (like 01)")
                room_number = ""
                continue
    
    # Count letters and numbers
    has_letter = False
    has_number = False
    has_invalid = False
    
    k = 0
    while k < len(room_number):
        char = room_number[k]
        if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
            has_letter = True
        elif char >= "0" and char <= "9":
            has_number = True
        elif char == "-":
            pass
        else:
            has_invalid = True
        k = k + 1
    
    if has_invalid:
        print("Invalid: Room number contains invalid characters (only letters, numbers, and dash allowed)")
        room_number = ""
    elif not has_letter and has_number:
        print("Invalid: Room number cannot be numbers only (must include letters)")
        room_number = ""
    elif has_letter and not has_number:
        print("Invalid: Room number cannot be letters only (must include numbers)")
        room_number = ""
    elif not has_letter and not has_number:
        print("Invalid: Room number must contain both letters and numbers")
        room_number = ""

print("")
print("=" * 50)
print("       DORM ROOM -- CHORE LIST")
print("=" * 50)

# Display chore list using for loop
for idx in range(5):
    chore_num = idx + 1
    name = chore_names[idx]
    freq = chore_frequencies[idx]
    print(f"  {chore_num}. {name:20} [{freq}]")

print("=" * 50)
print("")

# Lists to store assigned chores
assigned_chore_numbers = []
assigned_roommates = []
assigned_statuses = []

# Track completed and assigned counts
completed_count = 0
assigned_count = 0

# Chore entry loop - runs exactly 4 times using while loop
chore_entry = 1
while chore_entry <= 4:
    print(f"--- CHORE {chore_entry} ---")
    
    # Get chore number with validation
    chore_num_input = ""
    chore_num = -1
    
    while chore_num == -1:
        chore_num_input = input("Chore number (0 to skip): ")
        
        # Check if empty
        if chore_num_input == "":
            print("Invalid: Please enter a number between 0 and 5")
            continue
        
        # Check if valid number
        is_valid_number = True
        m = 0
        while m < len(chore_num_input):
            char = chore_num_input[m]
            if char < "0" or char > "9":
                is_valid_number = False
            m = m + 1
        
        if not is_valid_number:
            print("Invalid: Please enter a number only (0 to skip, 1-5 for chores)")
            continue
        
        # Convert to integer
        temp_num = 0
        n = 0
        while n < len(chore_num_input):
            temp_num = temp_num * 10 + (ord(chore_num_input[n]) - ord("0"))
            n = n + 1
        
        # Ensure no leading zeros (e.g., "01")
        if len(chore_num_input) > 1 and chore_num_input[0] == "0":
            print("Invalid: Please enter a valid chore number (no leading zeros like 01)")
            continue
        
        # Ensure it's one of the allowed options: 0–5
        if not (0 <= temp_num <= 5):
            print("Invalid: Please enter a number between 0 and 5 only")
            continue
        
        chore_num = temp_num
    
    # If skip (0), move to next entry
    if chore_num == 0:
        print("")
        chore_entry = chore_entry + 1
        continue
    
    # Get roommate name with validation
    roommate_name = ""
    while roommate_name == "":
        roommate_name = input("Roommate name: ")
        
        # Check if empty
        if roommate_name == "":
            print("Invalid: Please enter a name (cannot be empty)")
            continue
        
        # Check for invalid characters
        has_invalid = False
        p = 0
        while p < len(roommate_name):
            char = roommate_name[p]
            is_letter = (char >= "a" and char <= "z") or (char >= "A" and char <= "Z")
            is_space = char == " "
            if not is_letter and not is_space:
                has_invalid = True
            p = p + 1
        
        if has_invalid:
            print("Invalid: Name should only contain letters and spaces (no numbers or symbols)")
            roommate_name = ""
    
    # Get status with validation
    status = ""
    while status == "":
        status = input("Status (done/not done): ")
        
        # Check if empty
        if status == "":
            print("Invalid: Please enter 'done' or 'not done'")
            continue
        
        if status != "done" and status != "not done":
            print("Invalid: Please enter exactly 'done' or 'not done'")
            status = ""
    
    # Store the assignment
    assigned_chore_numbers.append(chore_num)
    assigned_roommates.append(roommate_name)
    assigned_statuses.append(status)
    assigned_count = assigned_count + 1
    
    if status == "done":
        completed_count = completed_count + 1
    
    print("")
    chore_entry = chore_entry + 1

# Calculate completion rate
if assigned_count > 0:
    completion_rate = (completed_count * 100) // assigned_count
else:
    completion_rate = 0

# Determine room status
if completion_rate == 100:
    room_status = "SPOTLESS!"
elif completion_rate >= 50:
    room_status = "ALMOST THERE!"
else:
    room_status = "NEEDS WORK!"

# Print Weekly Chore Report
print("")
print("=" * 50)
print("      ROOM " + room_number + " -- WEEKLY CHORE REPORT")
print("=" * 50)
print(f"Room Monitor : {monitor_name}")
print("-" * 50)

# Print assigned chores using for loop
report_num = 1
for idx in range(assigned_count):
    chore_idx = assigned_chore_numbers[idx] - 1
    chore_name = chore_names[chore_idx]
    frequency = chore_frequencies[chore_idx]
    roommate = assigned_roommates[idx]
    status = assigned_statuses[idx]
    
    print("")
    print(f"[{report_num}] {chore_name:20} [{frequency}]")
    print(f"    Roommate : {roommate}")
    print(f"    Status   : {status}")
    
    report_num = report_num + 1

print("")
print("-" * 50)
print(f"Completed      : {completed_count} out of {assigned_count} assigned")
print(f"Completion Rate: {completion_rate}%")
print(f"Room Status    : {room_status}")
print("=" * 50)
