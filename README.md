# 🧮 Calculator — Python Project

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)
![DaysOfCode](https://img.shields.io/badge/90DaysOfCode-Python%20Challenge-9cf)

---

A clean, modular, and beginner-friendly **command-line calculator** built using Python.  
This project is part of my **#90DaysOfCode** challenge, focusing on improving logic building, modular design, and user interaction in Python.

---

## 🚀 Features

- ✅ Perform basic arithmetic operations: **add**, **subtract**, **multiply**, and **divide**  
- ✅ Chain multiple calculations in a single run  
- ✅ Option to **restart** or **quit** anytime  
- ✅ Handles **invalid operations** and **division by zero** gracefully  
- ✅ Simple and clean ASCII art interface for better user experience  

---

## 🧠 What I Learned

- Creating modular and reusable functions in Python  
- Using **dictionaries** to map symbols to function logic  
- Handling **loops** and **conditional branching** for interactive programs  
- Implementing **input validation** and basic **error handling**  
- Designing a clean **CLI (Command-Line Interface)**  

---

## 💻 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/faizhsnnn/Calculator.git
cd Calculator
```
### 2️⃣ Run the Program
```bash
python calculator.py
```
---

## 🧩 Example Run

```bash
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                            

What is the first number?: 10  
Pick an operation: +  
What is the next number?: 5  
10.0 + 5.0 = 15.0  
Type 'y' to continue with 15.0, or 'n' to start a new calculation, or 'q' to quit:
```
---

## 🧾 File Structure

```bash
Calculator/
│
├── calculator.py      # Main Python program
├── ascii.py           # ASCII art logo for the calculator
└── README.md          # Project documentation
```
---

# ✨ Code Highlights

```bash
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply, 
    "/" : divide,
}

if operation_symbol not in operations:
```
---

# 🔮 Future Improvements

- ✅Add power, modulo, and square root operations
- ✅Build a GUI version using Tkinter or PyQt
- ✅Implement unit tests for automated validation
- ✅Add calculation history tracking
---

# 👨‍💻 Author

- Faiz Hasan
🎓 BCA Final Year @ Graphic Era University
🚀 #90DaysOfCode Python Learner
🐍 Passionate about Clean Code & Problem Solving
---


If you found this project useful or inspiring, please consider starring ⭐ the repository — it helps support my coding journey and motivates me to build more open-source projects!

🖋️ "Code is like math — elegant when simple, powerful when precise."
    print("Invalid operation! Try again.")
    continue
```
---

