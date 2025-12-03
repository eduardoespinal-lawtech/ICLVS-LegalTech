# iclvs_core.py
# Intelligent Contextual Legal Verification System (ICLVS)
# Core logic — academic and evidentiary prototype

import re
import hashlib
from datetime import datetime
from typing import Dict, List

RULES: Dict[str, Dict[str, List[str]]] = {
    "Florida": {"must": ["Florida", "Miami"], "avoid": ["outside Florida"]},
    "New York": {"must": ["New York", "NYC"], "avoid": ["outside New York"]},
    "California": {"must": ["California", "Los Angeles"], "avoid": ["outside California"]}
}

def verify_clause(text: str, jurisdiction: str) -> dict:
    """
    Verifica una cláusula legal según reglas básicas de jurisdicción.
    
    Args:
        text (str): Texto de la cláusula.
        jurisdiction (str): Jurisdicción a validar.
    
    Returns:
        dict: Resultado con score, hash y metadatos.
    """
    rule = RULES.get(jurisdiction, {"must": [], "avoid": []})
    score = 50  # base neutral
    
    # Reglas positivas
    score += sum(15 for term in rule["must"] if re.search(term, text, re.I))
    
    # Reglas negativas
    score -= sum(25 for term in rule["avoid"] if re.search(term, text, re.I))
    
    # Normalización
    score = max(0, min(100, score))
    
    digest = hashlib.sha256(f"{text}{jurisdiction}".encode()).hexdigest()
    
    return {
        "jurisdiction": jurisdiction,
        "score": score,
        "timestamp": datetime.now().isoformat(),
        "hash": digest,
        "matched_terms": {
            "must": [t for t in rule["must"] if re.search(t, text, re.I)],
            "avoid": [t for t in rule["avoid"] if re.search(t, text, re.I)]
        }
    }

if __name__ == "__main__":
    clause = input("Enter clause: ")
    jurisdiction = input("Enter jurisdiction (Florida/New York/California): ")
    result = verify_clause(clause, jurisdiction)
    print(result)
