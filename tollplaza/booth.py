# Keeps a live count of PAID vehicles passing through the lane
counts = {"Car": 0, "Bus": 0, "Truck": 0}


def show_counts():
    """Print the count of each vehicle type."""
    for v in counts:
        print(v, ":", counts[v])


def update_count(v):
    """Add 1 to the count of vehicle type v (ignored if v is not a valid type)."""
    if v in counts:
        counts[v] = counts[v] + 1
