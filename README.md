# COM103 Midterm Exam - Dorm Room Chore Tracker

## 📌 Description
This program is a **Dorm Room Chore Tracker** that helps manage and monitor chores assigned to roommates.

It allows the user (room monitor) to:
- Enter and validate their name
- Enter and validate a room number
- View a predefined list of chores with frequencies
- Assign chores to roommates
- Track whether each chore is completed or not
- Generate a weekly chore report

## ✅ Input Validation Features
The program ensures:
- Names contain only letters and spaces
- Each name part has at least 2 characters
- Room number contains both letters and numbers
- No invalid characters are allowed
- Chore number input is between 0–5
- Status must be exactly "done" or "not done"

## 🔄 Program Flow
1. User enters room monitor name (validated)
2. User enters room number (validated)
3. Program displays available chores
4. User assigns up to 4 chores
5. For each chore:
   - Choose chore number (or skip)
   - Enter roommate name
   - Enter status (done / not done)
6. Program calculates completion rate
7. Program displays a formatted weekly report

## ▶️ How to Run
1. Make sure Python 3 is installed
2. Open terminal or command prompt
3. Navigate to the project folder
4. Run:

## 🛠️ Features
- Uses lists to store chore data
- Uses loops (while and for) for processing
- Manual input validation without built-in functions
- Clean formatted output report
- Calculates completion percentage and room status

## 📊 Room Status Logic
- 100% → SPOTLESS!
- 50% or more → ALMOST THERE!
- Below 50% → NEEDS WORK!

## 👤 Author 
Ali, Khalif G.