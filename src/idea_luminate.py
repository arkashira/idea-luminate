import argparse
import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class FeedbackPoint:
    key: str
    value: str

def validate_idea(idea: str) -> Dict[str, List[str]]:
    """
    Analyzes the viability of an idea based on market trends and user needs.
    Returns a dictionary with feedback points.
    """
    if not idea.strip():
        return {"feedback": ["Idea is empty. Please provide a description."]}
    
    # Normalize the idea text
    normalized = idea.lower().strip()
    
    # Check for keywords related to open source/community
    if "open source" in normalized or "contribute" in normalized or "community" in normalized:
        feedback = [
            "Market Relevance: Your idea aligns with validated open-source contributions (e.g., the Mastodon example).",
            "User Need: Addresses the need for community-driven solutions, which has proven demand.",
            "Viability: High potential for community adoption and long-term sustainability."
        ]
    # Check for keywords related to support/hiring
    elif "support" in normalized or "hiring" in normalized or "customer service" in normalized:
        feedback = [
            "Market Relevance: Aligns with validated user support solutions (e.g., PANROTAS passenger support).",
            "User Need: Addresses a critical pain point in service industries.",
            "Viability: High demand for robust support systems, as seen in existing validated products."
        ]
    # Check for keywords related to testing/quality
    elif "testing" in normalized or "quality" in normalized or "coverage" in normalized:
        feedback = [
            "Market Relevance: Matches the validated QA test-coverage gap analytics product.",
            "User Need: Addresses the need for automated quality assurance in software development.",
            "Viability: Strong demand from development teams for improved testing workflows."
        ]
    else:
        feedback = [
            "Market Relevance: Idea is not clearly aligned with existing validated needs.",
            "User Need: May not address a widely recognized pain point.",
            "Viability: Consider refining the idea to focus on a validated user need."
        ]
    
    return {"feedback": feedback}

def main():
    """
    Parses command-line arguments and provides feedback on an idea.
    """
    parser = argparse.ArgumentParser(description="Idea validation tool.")
    parser.add_argument("idea", help="Your idea description")
    args = parser.parse_args()
    
    feedback = validate_idea(args.idea)
    print(json.dumps(feedback, indent=2))
