# iclvs_core.py
# Intelligent Contextual Legal Verification System (ICLVS)
# Demonstrative core logic — for academic and evidentiary use

import re
import hashlib
from datetime import datetime

def verify_clause(text: str, jurisdiction: str) -> dict:
    """Contextual verification prototype."""
    rules = {
        "Florida": {"must": ["Florida", "Miami"], "avoid": ["outside Florida"]},
        "New York": {"must": ["New York"], "avoid": ["outside New York"]},
        "California": {"must": ["California"], "avoid": ["outside California"]}
    }
    rule = rules.get(jurisdiction, {"must": [], "avoid": []})
    score = 50
    for term in rule["must"]:
        if re.search(term, text, re.I):
            score += 15
    for term in rule["avoid"]:
        if re.search(term, text, re.I):
            score -= 25
    score = max(0, min(100, score))
    digest = hashlib.sha256((text + jurisdiction).encode()).hexdigest()
    return {
        "jurisdiction": jurisdiction,
        "score": score,
        "timestamp": datetime.now().isoformat(),
        "hash": digest
    }

if __name__ == "__main__":
    clause = input("Enter clause: ")
    result = verify_clause(clause, "Florida")
    print(result)
