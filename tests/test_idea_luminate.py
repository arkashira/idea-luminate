from idea_luminate import Idea, validate_idea, provide_feedback, load_ideas_from_json

def test_validate_idea():
    idea = Idea(name="Test Idea", description="Test Description", market_demand=10)
    assert validate_idea(idea) == True

def test_validate_idea_zero_demand():
    idea = Idea(name="Test Idea", description="Test Description", market_demand=0)
    assert validate_idea(idea) == False

def test_provide_feedback():
    idea = Idea(name="Test Idea", description="Test Description", market_demand=10)
    assert provide_feedback(idea) == "Idea 'Test Idea' is feasible with a market demand of 10"

def test_provide_feedback_zero_demand():
    idea = Idea(name="Test Idea", description="Test Description", market_demand=0)
    assert provide_feedback(idea) == "Idea 'Test Idea' is not feasible due to low market demand"

def test_load_ideas_from_json():
    json_data = '[{"name": "Idea 1", "description": "Description 1", "market_demand": 10}, {"name": "Idea 2", "description": "Description 2", "market_demand": 0}]'
    ideas = load_ideas_from_json(json_data)
    assert len(ideas) == 2
    assert ideas[0].name == "Idea 1"
    assert ideas[1].name == "Idea 2"
