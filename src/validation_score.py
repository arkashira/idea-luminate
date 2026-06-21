import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Idea:
    trend: float
    reddit_volume: int
    sentiment: float

def calculate_validation_score(idea: Idea) -> int:
    """
    Calculate the validation score for an idea.

    The score combines normalized trend, Reddit volume, and sentiment from product-review snippets.
    """
    trend_weight = 0.4
    reddit_volume_weight = 0.3
    sentiment_weight = 0.3

    trend_score = idea.trend / 100
    reddit_volume_score = idea.reddit_volume / 1000
    sentiment_score = idea.sentiment / 5

    validation_score = (trend_score * trend_weight +
                        reddit_volume_score * reddit_volume_weight +
                        sentiment_score * sentiment_weight) * 100

    return int(validation_score)

def get_explanation(idea: Idea) -> str:
    """
    Get a brief explanation of the contributing factors for the validation score.
    """
    explanation = f"Trend: {idea.trend}, Reddit Volume: {idea.reddit_volume}, Sentiment: {idea.sentiment}"
    return explanation

def validate_idea(idea: Idea) -> Dict:
    """
    Validate an idea and return the validation score and explanation.
    """
    validation_score = calculate_validation_score(idea)
    explanation = get_explanation(idea)

    return {"validation_score": validation_score, "explanation": explanation}
