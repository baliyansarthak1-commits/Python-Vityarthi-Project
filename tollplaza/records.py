# Stores all issued toll receipts (kept in memory for one shift)
receipts = []


def add_receipt(plate, v_type, amount):
    """Save one receipt as a dictionary."""
    receipts.append({"plate": plate, "type": v_type, "amt": amount})


def get_total_cash():
    """Return the total amount collected so far."""
    total = 0
    for r in receipts:
        total = total + r["amt"]
    return total
