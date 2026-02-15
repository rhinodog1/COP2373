"""
spam_detector.py

Spam Score Detector
- Prompts the user to enter an email message
- Scans for 30 common spam words/phrases
- Adds 1 point per occurrence (multiple occurrences count multiple points)
- Displays spam score, likelihood rating, and the terms that triggered the score

Author: Joseph Scott
"""

import re
from typing import List, Dict, Tuple


def get_spam_terms() -> List[str]:
    """
    Returns a list of 30 common spam words/phrases.
    """
    return [
        "act now",
        "limited time",
        "offer expires",
        "last chance",
        "urgent",
        "risk-free",
        "guaranteed",
        "no cost",
        "free",
        "free money",
        "cash bonus",
        "make money",
        "earn $$$",
        "get paid",
        "work from home",
        "no credit check",
        "cheap loan",
        "credit repair",
        "winner",
        "you have won",
        "claim your prize",
        "congratulations",
        "click here",
        "verify your account",
        "password",
        "suspended",
        "final notice",
        "unsubscribe",
        "wire transfer",
        "bitcoin",
    ]


def read_multiline_message() -> str:
    """
    Reads a multi-line email message from the user.
    Stops when the user enters a blank line.
    """
    print("Paste/type the email message below.")
    print("When you're done, press Enter on a blank line.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    return "\n".join(lines)


def analyze_message(message: str, terms: List[str]) -> Tuple[int, Dict[str, int]]:
    """
    Scan the message for each term (case-insensitive).
    Adds 1 point per occurrence.
    Returns (score, hits_dict).
    """
    normalized = message.lower()
    hits: Dict[str, int] = {}

    for term in terms:
        if " " in term:
            # Phrase
            pattern = re.escape(term.lower())
            count = len(re.findall(pattern, normalized))
        else:
            # Single word (whole word match)
            pattern = r"\b" + re.escape(term.lower()) + r"\b"
            count = len(re.findall(pattern, normalized))

        if count > 0:
            hits[term] = count

    score = sum(hits.values())
    return score, hits


def rate_likelihood(score: int) -> str:
    """
    Convert spam score into likelihood label.
    """
    if score <= 2:
        return "Unlikely spam"
    elif score <= 6:
        return "Possibly spam"
    elif score <= 12:
        return "Likely spam"
    else:
        return "Very likely spam"


def main():
    terms = get_spam_terms()
    message = read_multiline_message()

    if not message.strip():
        print("\nNo message entered. Exiting.")
        return

    score, hits = analyze_message(message, terms)
    likelihood = rate_likelihood(score)

    print("\n--- Spam Scan Results ---")
    print(f"Spam score: {score}")
    print(f"Likelihood: {likelihood}")

    if hits:
        print("\nTriggered terms (term: occurrences):")
        for term, count in hits.items():
            print(f"- {term}: {count}")
    else:
        print("\nNo spam terms found.")


if __name__ == "__main__":
    main()
