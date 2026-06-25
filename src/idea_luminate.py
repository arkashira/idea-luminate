import json
from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    name: str
    search_volume: int
    competition: int
    willingness_to_pay: int

class IdeaLuminate:
    def __init__(self):
        self.ideas = []

    def add_idea(self, idea: Idea):
        self.ideas.append(idea)

    def get_ideas(self):
        return self.ideas

    def sort_ideas_by_search_volume(self):
        return sorted(self.ideas, key=lambda x: x.search_volume)

    def sort_ideas_by_competition(self):
        return sorted(self.ideas, key=lambda x: x.competition)

    def sort_ideas_by_willingness_to_pay(self):
        return sorted(self.ideas, key=lambda x: x.willingness_to_pay)

    def get_validation_metrics(self, idea_name: str):
        for idea in self.ideas:
            if idea.name == idea_name:
                return {
                    "search_volume": idea.search_volume,
                    "competition": idea.competition,
                    "willingness_to_pay": idea.willingness_to_pay
                }
        return None
