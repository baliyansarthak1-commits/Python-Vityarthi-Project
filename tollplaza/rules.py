# Rules for toll exemption (emergency / VIP vehicles)

def is_exempt(plate):
    """Return True if the plate contains AMB (ambulance) or VIP.
    The plate is converted to capital letters first, so 'ka01amb99' also works."""
    plate = plate.upper()
    if "AMB" in plate or "VIP" in plate:
        return True
    return False
