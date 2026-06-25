import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Idea:
    id: int
    name: str
    progress: int

@dataclass
class Update:
    idea: Idea
    market_trends: List[str]
    user_needs: List[str]

class IdeaLuminate:
    def __init__(self):
        self.ideas = []
        self.market_trends = []
        self.user_needs = []

    def add_idea(self, idea: Idea):
        self.ideas.append(idea)

    def add_market_trend(self, trend: str):
        self.market_trends.append(trend)

    def add_user_need(self, need: str):
        self.user_needs.append(need)

    def get_update(self, idea_id: int) -> Update:
        idea = next((i for i in self.ideas if i.id == idea_id), None)
        if idea is None:
            raise ValueError("Idea not found")
        return Update(idea, self.market_trends, self.user_needs)

    def send_update(self, idea_id: int) -> str:
        update = self.get_update(idea_id)
        return json.dumps({
            "idea": {
                "id": update.idea.id,
                "name": update.idea.name,
                "progress": update.idea.progress
            },
            "market_trends": update.market_trends,
            "user_needs": update.user_needs
        })

    def schedule_update(self, idea_id: int, interval: int = 7) -> datetime:
        idea = next((i for i in self.ideas if i.id == idea_id), None)
        if idea is None:
            raise ValueError("Idea not found")
        return datetime.now() + timedelta(days=interval)
