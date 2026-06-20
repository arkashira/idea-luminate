import json
from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    name: str
    description: str
    market_demand: int

def validate_idea(idea: Idea) -> bool:
    """Validate an idea based on market demand"""
    return idea.market_demand > 0

def provide_feedback(idea: Idea) -> str:
    """Provide feedback on idea feasibility"""
    if validate_idea(idea):
        return f"Idea '{idea.name}' is feasible with a market demand of {idea.market_demand}"
    else:
        return f"Idea '{idea.name}' is not feasible due to low market demand"

def load_ideas_from_json(json_data: str) -> List[Idea]:
    """Load ideas from a JSON string"""
    data = json.loads(json_data)
    return [Idea(name=idea['name'], description=idea['description'], market_demand=idea['market_demand']) for idea in data]

def main():
    json_data = '[{"name": "Idea 1", "description": "Description 1", "market_demand": 10}, {"name": "Idea 2", "description": "Description 2", "market_demand": 0}]'
    ideas = load_ideas_from_json(json_data)
    for idea in ideas:
        print(provide_feedback(idea))

if __name__ == "__main__":
    main()
