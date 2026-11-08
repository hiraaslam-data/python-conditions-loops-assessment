# Python Conditions & Loops Assessment

## Project Overview
This repository contains two console-based Python applications built for a programming assessment. Each one solves a realistic business problem while demonstrating a core Python topic:

| Application | File | Topic |
|-------------|------|-------|
| Student Scholarship Eligibility System | `student_scholarship_system.py` | Conditional statements (`if`, `elif`, `else`) |
| Smart Pharmacy Inventory & Sales Management System | `pharmacy_inventory_system.py` | Loop structures (`for`, `range()`, counters, accumulators) |

## Project Structure
```
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

---

## Application 1: Student Scholarship Eligibility System

### Description
This program decides whether a student qualifies for a university scholarship and prints a complete evaluation report.

**Input collected:** student name, academic marks (%), attendance (%), monthly family income (Rs.)

**Input validation:**
- Name must contain letters and spaces only.
- Marks and attendance must be numbers between 0 and 100.
- Income must be a number that is not negative.
- Invalid values are rejected and the user is asked again.

**Eligibility criteria (all three must be met):**
- Academic marks of at least 80%
- Attendance of at least 85%
- Monthly family income of Rs. 50,000 or less

**Scholarship result:**
- Marks of 90% or above: **Full Scholarship**
- Marks from 80% up to below 90%: **Partial Scholarship**
- Any criterion not met: **Not Eligible**, with every reason listed

---

## Application 2: Smart Pharmacy Inventory & Sales Management System

### Description
This program processes daily medicine sales for a pharmacy and generates a final sales report.

**What it does:**
1. Asks how many different medicines need to be processed.
2. Uses a `for` loop to process each medicine.
3. Collects medicine name, available stock, price per unit, and quantity sold (all validated).
4. Rejects the sale if the quantity sold is more than the available stock.
5. Calculates the sales amount and the remaining stock for each successful sale.
6. Shows a low-stock warning if remaining stock is below 10 units.
7. Adds each sale to a revenue accumulator.
8. Counts how many medicines need restocking.
9. Prints a final report with total medicines processed, total revenue, and medicines requiring restocking.

---

## Python Concepts and Techniques Used
- Variables and constants (`MIN_MARKS`, `LOW_STOCK_LIMIT`, etc.)
- `input()` and `print()` with f-string formatting
- Arithmetic operators (`*`, `-`, `+=`)
- Comparison and logical operators (`<`, `>=`, `and`, `not`)
- Conditional statements: `if`, `elif`, `else`
- `for` loop with `range()`
- `while True` loops for repeated input validation
- Exception handling with `try` / `except ValueError`
- Counters and accumulators (revenue total, restock count, sale counts)
- Functions to reuse validation code
- Lists and string methods (`strip()`, `isalpha()`, `replace()`, `join()`)
- Comments and meaningful variable names

---

## How to Run

### Requirements
- Python 3.8 or later installed on your computer

### Steps
1. Clone the repository (or download the files):
   ```bash
   git clone https://github.com/hiraaslam-data/python-conditions-loops-assessment.git
   cd python-conditions-loops-assessment
   ```
2. Run the scholarship program:
   ```bash
   python student_scholarship_system.py
   ```
3. Run the pharmacy program:
   ```bash
   python pharmacy_inventory_system.py
   ```

On some systems, use `python3` or `py` instead of `python`.

You can also open each file in VS Code and press the **Run (▶)** button.

---

## Sample Execution

### Task 1: Student Scholarship Eligibility System

**Example 1: Full Scholarship**
```
==================================================
   STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM
==================================================
Enter student name: Ayesha Khan
Enter academic marks (%): 92
Enter attendance percentage (%): 90
Enter monthly family income (Rs.): 40000

==================================================
        SCHOLARSHIP EVALUATION REPORT
==================================================
Student Name      : Ayesha Khan
Academic Marks    : 92.00%  (min 80%)
Attendance        : 90.00%  (min 85%)
Monthly Income    : Rs. 40,000.00  (max Rs. 50,000)
--------------------------------------------------
Eligibility       : ELIGIBLE
Result            : Full Scholarship
==================================================
```

**Example 2: Not Eligible (multiple reasons)**
```
Enter student name: Ali Raza
Enter academic marks (%): 75
Enter attendance percentage (%): 85
Enter monthly family income (Rs.): 60000

==================================================
        SCHOLARSHIP EVALUATION REPORT
==================================================
Student Name      : Ali Raza
Academic Marks    : 75.00%  (min 80%)
Attendance        : 85.00%  (min 85%)
Monthly Income    : Rs. 60,000.00  (max Rs. 50,000)
--------------------------------------------------
Eligibility       : NOT ELIGIBLE
Result            : Not Eligible
Reason(s):
  - Marks are below the required 80%.
  - Monthly family income exceeds Rs. 50,000.
==================================================
```

### Task 2: Smart Pharmacy Inventory & Sales Management System

```
=======================================================
   SMART PHARMACY INVENTORY & SALES MANAGEMENT
=======================================================
How many different medicines to process? 3

--- Medicine 1 of 3 ---
Medicine name: Panadol
Available stock: 50
Price per unit (Rs.): 20
Quantity sold: 45
Sale amount     : Rs. 900.00
Remaining stock : 5
WARNING: Low stock for Panadol (5 left)!

--- Medicine 2 of 3 ---
Medicine name: Brufen
Available stock: 30
Price per unit (Rs.): 15
Quantity sold: 40
Sale rejected: only 30 unit(s) of Brufen in stock.

--- Medicine 3 of 3 ---
Medicine name: Disprin
Available stock: 12
Price per unit (Rs.): 5
Quantity sold: 2
Sale amount     : Rs. 10.00
Remaining stock : 10

=======================================================
                 FINAL SALES REPORT
=======================================================
Total medicines processed      : 3
Successful sales               : 2
Rejected sales (low stock)     : 1
Total revenue                  : Rs. 910.00
Medicines requiring restocking : 1
Restock list                   : Panadol
=======================================================
```

---

## Testing Scenarios
**Scholarship system**
- Full scholarship (marks 90 or above) and partial scholarship (marks 80 to 89)
- Boundary values: marks 80 and 90, attendance 85, income 50,000
- Each criterion failing on its own, and multiple failures together
- Invalid input: empty name, name with numbers, text instead of numbers, marks above 100, negative income

**Pharmacy system**
- Normal sale with enough stock
- Quantity sold greater than available stock (sale rejected)
- Remaining stock of exactly 10 (no warning) and below 10 (warning)
- Zero quantity sold
- Invalid input: text instead of numbers, negative values, zero price, empty medicine name

---

## Author
Hira Aslam
GitHub: [hiraaslam-data](https://github.com/hiraaslam-data)
