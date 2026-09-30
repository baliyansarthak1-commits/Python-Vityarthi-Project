# Cash-drawer limit, alert messages and the alert check
CASH_LIMIT = 2000
ALERT_MSG = "ALERT: Cash limit reached! Deposit cash to bank."
SAFE_MSG = "Cash in counter is within safe limit."


def cash_alert(total):
    """Return ALERT_MSG if total has reached CASH_LIMIT, otherwise SAFE_MSG."""
    if total >= CASH_LIMIT:
        return ALERT_MSG
    return SAFE_MSG
