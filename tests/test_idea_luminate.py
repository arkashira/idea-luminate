import pytest
from src.idea_luminate import validate_idea

def test_validate_idea_open_source():
    idea = "I want to create an open-source project to help indie hackers contribute to the community."
    result = validate_idea(idea)
    assert result["feedback"][0] == "Market Relevance: Your idea aligns with validated open-source contributions (e.g., the Mastodon example)."
    assert result["feedback"][1] == "User Need: Addresses the need for community-driven solutions, which has proven demand."
    assert result["feedback"][2] == "Viability: High potential for community adoption and long-term sustainability."

def test_validate_idea_support():
    idea = "Develop a support system for a service like PANROTAS to improve customer interactions."
    result = validate_idea(idea)
    assert result["feedback"][0] == "Market Relevance: Aligns with validated user support solutions (e.g., PANROTAS passenger support)."
    assert result["feedback"][1] == "User Need: Addresses a critical pain point in service industries."
    assert result["feedback"][2] == "Viability: High demand for robust support systems, as seen in existing validated products."

def test_validate_idea_testing():
    idea = "Create a tool to analyze test coverage gaps in production code."
    result = validate_idea(idea)
    assert result["feedback"][0] == "Market Relevance: Matches the validated QA test-coverage gap analytics product."
    assert result["feedback"][1] == "User Need: Addresses the need for automated quality assurance in software development."
    assert result["feedback"][2] == "Viability: Strong demand from development teams for improved testing workflows."

def test_validate_idea_empty():
    idea = ""
    result = validate_idea(idea)
    assert result["feedback"][0] == "Idea is empty. Please provide a description."

def test_validate_idea_no_keywords():
    idea = "I want to build a social media app."
    result = validate_idea(idea)
    assert result["feedback"][0] == "Market Relevance: Idea is not clearly aligned with existing validated needs."
    assert result["feedback"][1] == "User Need: May not address a widely recognized pain point."
    assert result["feedback"][2] == "Viability: Consider refining the idea to focus on a validated user need."
