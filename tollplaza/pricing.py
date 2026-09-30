# Toll rates for vehicle categories (single journey, in Rs.)
rates = {"Car": 100, "Bus": 200, "Truck": 300}

# Extra amount charged for a return journey (kept in ONE place only)
RETURN_SURCHARGE = 50


def get_toll(v, trip):
    """Return the toll for vehicle type v and trip ("Single" or "Return").
    Unknown vehicle types return 0."""
    if v not in rates:
        return 0
    if trip == "Return":
        return rates[v] + RETURN_SURCHARGE
    return rates[v]
