import pytest
from validation_score import Idea, validate_idea

def test_calculate_validation_score():
    idea = Idea(trend=50, reddit_volume=500, sentiment=3)
    validation_score = validate_idea(idea)["validation_score"]
    assert 0 <= validation_score <= 100

def test_get_explanation():
    idea = Idea(trend=50, reddit_volume=500, sentiment=3)
    explanation = validate_idea(idea)["explanation"]
    assert "Trend: 50" in explanation
    assert "Reddit Volume: 500" in explanation
    assert "Sentiment: 3" in explanation

def test_validate_idea():
    idea = Idea(trend=50, reddit_volume=500, sentiment=3)
    result = validate_idea(idea)
    assert "validation_score" in result
    assert "explanation" in result

def test_edge_case_zero_values():
    idea = Idea(trend=0, reddit_volume=0, sentiment=0)
    validation_score = validate_idea(idea)["validation_score"]
    assert validation_score == 0

def test_edge_case_max_values():
    idea = Idea(trend=100, reddit_volume=1000, sentiment=5)
    validation_score = validate_idea(idea)["validation_score"]
    assert validation_score == 100
