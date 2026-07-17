# Assignment: Vehicle Rental Management System

## Objective

Build a **Vehicle Rental Management System** using **Inheritance** in Python.

The system should demonstrate code reusability by creating a common parent class and multiple child classes.

---

# Problem Statement

A vehicle rental company rents different types of vehicles such as:

- Cars
- Bikes
- Trucks

Although every vehicle has some common properties, each vehicle type also has its own unique features.

Instead of writing duplicate code for every vehicle, use **Inheritance**.

---

# Requirements

## Step 1: Create a Parent Class

Create a class named **Vehicle**.

### Attributes

- vehicle_id
- brand
- model
- rent_per_day
- availability (Available / Not Available)

### Methods

- display_details()
- rent_vehicle()
- return_vehicle()

---

## Step 2: Create a Car Class

Create a class named **Car** that inherits from **Vehicle**.

### Additional Attribute

- number_of_doors

### Additional Method

- start_ac()

---

## Step 3: Create a Bike Class

Create a class named **Bike** that inherits from **Vehicle**.

### Additional Attribute

- helmet_included (Yes/No)

### Additional Method

- wheelie_mode()

---

## Step 4: Create a Truck Class

Create a class named **Truck** that inherits from **Vehicle**.

### Additional Attribute

- load_capacity

### Additional Method

- load_cargo()

---

# Functional Requirements

Your program should:

- Create at least one Car object.
- Create at least one Bike object.
- Create at least one Truck object.
- Display the details of every vehicle.
- Rent a vehicle.
- Return a vehicle.
- Call each child-specific method.

---

# Sample Output

```
========== CAR ==========
Vehicle ID : V101
Brand      : Toyota
Model      : Fortuner
Rent/Day   : ₹3500
Availability : Available

Air Conditioner Started

Vehicle rented successfully.

Vehicle returned successfully.

==========================

========== BIKE ==========
Vehicle ID : V201
Brand      : Royal Enfield
Model      : Classic 350
Rent/Day   : ₹900
Availability : Available

Wheelie Mode Activated

Vehicle rented successfully.

==========================

========== TRUCK ==========
Vehicle ID : V301
Brand      : Tata
Model      : Signa
Rent/Day   : ₹6500
Availability : Available

Loading Cargo...

Vehicle rented successfully.
```

---

# Constraints

- Use **Inheritance**.
- Use the **super()** function to initialize parent class attributes.
- Do not duplicate common code in child classes.
- Child classes should only contain their own unique attributes and methods.
- Use constructors (`__init__`) appropriately.

---
