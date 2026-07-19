# Smart Device Management System

## Introduction
This project is a Mini Project for **EL 162 / 234 – Object Oriented Programming**, submitted by Richard Akwensy.
It simulates a software system used by a technology company to manage smart devices in a smart home.

## Project Summary
The system manages different types of smart devices, each sharing common information (name, device ID, power status) while also having their own unique features. The program demonstrates the following OOP concepts:

- Variables and data types
- Input and output
- Conditional statements
- Loops
- Functions
- Classes and objects
- Constructors (`__init__`)
- Methods
- Inheritance
- Encapsulation
- Getters and setters (`@property`)
- Use of `super()`

### Classes
- **SmartDevice** (Parent Class) – has private attributes `__device_id` and `__power_status`, a public attribute `name`, and methods `turn_on()`, `turn_off()`, and `display_info()`.
- **SecurityCamera** (Child Class) – adds `recording_status`, `start_recording()`, and `stop_recording()`.
- **SmartLight** (Child Class) – adds `brightness` (validated between 0–100), `increase_brightness()`, and `decrease_brightness()`.
- **TemperatureSensor** (Child Class) – adds `temperature` and `read_temperature()`.

All child classes inherit from `SmartDevice` and use `super()` to initialize inherited attributes. The device ID and power status are encapsulated (private) and can only be accessed or changed through getters/setters.

## How to Run the Program
1. Make sure you have **Python 3** installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program with:

```bash
python3 smart_device_management_system.py
```

5. Use the on-screen menu to interact with the devices:

```
1. Display Device Information
2. Turn Device On
3. Turn Device Off
4. Read Temperature
5. Adjust Brightness
6. Start Recording
7. Exit
```

## Author
- `Name:` AFFUL CHRISTABEL
- `Course:` EL 162 / 234 – Object Oriented Programming
- `Instructor:` Dr. Matthew Cobbinah (mcobbinah@umat.edu.gh)
# Smart-Device-Management-System-
