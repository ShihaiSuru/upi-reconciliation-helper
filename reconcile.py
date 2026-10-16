#!/usr/bin/env python3
"""Simple UPI reconciliation helper."""

def reconcile(bank_txns, upi_txns):
    matched = []
    unmatched = []
    for b in bank_txns:
        found = False
        for u in upi_txns:
            if abs(b["amount"] - u["amount"]) < 1 and b["date"] == u["date"]:
                matched.append((b, u))
                found = True
                break
        if not found:
            unmatched.append(b)
    return matched, unmatched

if __name__ == "__main__":
    bank = [{"date": "2026-10-16", "amount": 1500}]
    upi = [{"date": "2026-10-16", "amount": 1500}]
    m, u = reconcile(bank, upi)
    print(f"Matched: {len(m)}, Unmatched: {len(u)}")
