# Toll Booth Management System

## Overview
A Python console application that acts like the software inside a highway toll booth. It calculates toll for cars, buses and trucks (single or return trip), lets ambulance (`AMB`) and `VIP` vehicles pass free, counts vehicles, stores every receipt and warns the operator when the cash drawer crosses a safe limit.

Built for the **VITyarthi – Build Your Own Project** submission (B.Tech CSE, Python course).

## Features
- **Rate card** – shows single and return toll for Car, Bus and Truck.
- **Ticketing** – issues a ticket with the exact toll (return = single + Rs. 50).
- **Free pass for emergency/VIP vehicles** – plates containing `AMB` or `VIP` are charged Rs. 0 (not case-sensitive).
- **Live vehicle count** – number of paid Cars, Buses and Trucks.
- **Receipts** – list of all tickets with total cash collected.
- **Cash-limit alert** – warns when cash reaches Rs. 2000.
- **Input validation** – wrong vehicle type, wrong trip type, empty plate and wrong menu number all show a message instead of crashing.

## Technologies / Tools Used
- Python 3.8 or higher (standard library only – no external packages)
- `unittest` (built-in) for testing
- Git and GitHub for version control
- VS Code / IDLE as editor

## Project Structure
| File | Purpose |
|------|---------|
| `main.py` | Menu and program flow (run this file) |
| `pricing.py` | Toll rates and toll calculation |
| `rules.py` | AMB / VIP exemption check |
| `booth.py` | Vehicle counting |
| `records.py` | Receipts and total cash |
| `reports.py` | Cash limit, alert messages and alert check |
| `test_toll.py` | Unit tests |
| `statement.md` | Problem statement, scope, users |

## Steps to Install & Run
1. Install Python 3 from [python.org](https://www.python.org/downloads/) (tick "Add Python to PATH" on Windows). Check with `python --version`.
2. Download the project (`git clone <your-repo-link>` or *Code → Download ZIP* and extract it).
3. No dependencies to install – nothing to `pip install`.
4. Open a terminal **inside the project folder** and run:

```
python main.py
```
(use `python3 main.py` on macOS/Linux)

### How to Use
| Menu choice | What it does |
|-------------|--------------|
| 1 | Show rate card |
| 2 | Issue ticket (asks plate, vehicle type, trip type) |
| 3 | Show vehicle counts |
| 4 | Show receipts and total cash |
| 5 | Check cash-limit alert |
| 6 | End shift and exit |

### Sample Session
```
Choice: 2
Plate No: MH12AB1234
Type (Car/Bus/Truck): Car
Trip (Single/Return): Return
Toll to pay: Rs. 150
```

## Configuration
- Change toll rates or the return surcharge in `pricing.py` (`rates`, `RETURN_SURCHARGE`).
- Change exempt plate keywords in `rules.py`.
- Change the cash limit in `reports.py` (`CASH_LIMIT`, default 2000).

## Instructions for Testing
Run all unit tests from the project folder:

```
python -m unittest test_toll -v
```
Expected result: `Ran 14 tests ... OK`.

The tests cover pricing, exemption rules, vehicle counting, receipt totals and the cash-limit alert. Menu behaviour (invalid inputs) can be tested manually by running `python main.py` and typing wrong values such as `AutoRickshaw` as vehicle type or `9` as menu choice.

## Screenshots
Add your screenshots in a `screenshots/` folder and keep these lines:

![Rate card](screenshots/rates.png)
![Ticket issue](screenshots/ticket.png)
![Counts and receipts](screenshots/receipts.png)
![Cash alert](screenshots/alert.png)

## Known Limitations
Data is stored in memory only (lost when the program closes); exemption is based on plate text only; one booth only.

## Author
Sarthak Baliyan – 26BCE10721 – B.Tech CSE Core, VIT Bhopal
