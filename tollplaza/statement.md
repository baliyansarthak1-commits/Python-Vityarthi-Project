# Problem Statement: Highway Toll Plaza System

## 1. Problem Statement
At highway toll plazas, managing vehicles manually with paper receipts or mental calculations causes several real-world problems:
* **Calculation mistakes:** Cashiers must quickly work out different rates for cars, buses and trucks plus the extra charge for return journeys. In rush hour this leads to billing errors and slow lines.
* **No quick vehicle counting:** Shift supervisors find it hard to know how many trucks or cars passed through their booth.
* **Delays for emergency vehicles:** Ambulances and VIP convoys can get stuck or be charged by mistake because their plates are not flagged automatically.
* **Cash drawer risk:** If cash piles up unnoticed in the drawer it becomes a security risk. Staff need a clear reminder to move money to the office safe.

## 2. Project Goal
Build a simple, reliable command-line tool in Python that handles toll collection quickly and accurately.

## 3. Scope of the Project
**In scope**
* One toll booth / one lane, one shift per program run
* Three vehicle types: Car, Bus, Truck
* Two trip types: Single and Return
* Free pass for plates containing `AMB` or `VIP`
* Vehicle counting, receipt storage (in memory) and a cash-limit alert (Rs. 2000)
* Keyboard-driven menu with input validation

**Out of scope (future work)**
* FASTag / UPI / online payment
* Number-plate camera recognition
* Permanent storage (files or database)
* Multiple booths, operator login, graphical interface

## 4. Target Users
* **Toll Booth Operators:** check rates, enter vehicle details, issue tickets and take payments.
* **Shift In-Charge / Supervisors:** check shift totals, traffic counts and make sure cash is not overflowing in the counter.

## 5. High-Level Features
1. Rate card showing single and return toll for each vehicle type
2. Instant ticket generation with exact toll amount
3. Automatic free pass for emergency (`AMB`) and official (`VIP`) vehicles
4. Live count of vehicles by type
5. Receipt log with total cash collected
6. Cash-limit alert to prompt deposit to the office safe
7. Input validation for vehicle type, trip type, plate and menu choice

## 6. System Structure
The project is divided into 6 modules plus a test file:
1. `booth.py` – tracks vehicle counts.
2. `pricing.py` – stores rates and calculates single vs. return price.
3. `records.py` – stores receipts and totals the cash.
4. `rules.py` – checks plates for ambulance / VIP exemption.
5. `reports.py` – holds the cash limit, alert messages and alert check.
6. `main.py` – runs the menu and coordinates all actions.
7. `test_toll.py` – unit tests.
