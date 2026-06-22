import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Idea:
    id: int
    title: str
    industry: str
    tech_stack: str
    validation_status: str
    early_adopters: int
    revenue_signals: int

class IdeaDatabase:
    def __init__(self):
        self.ideas = []
        self.bookmarks = {}

    def add_idea(self, idea: Idea):
        self.ideas.append(idea)

    def search(self, query: str) -> List[Idea]:
        return [idea for idea in self.ideas if query.lower() in idea.title.lower() or query.lower() in idea.industry.lower() or query.lower() in idea.tech_stack.lower()]

    def get_idea(self, id: int) -> Idea:
        for idea in self.ideas:
            if idea.id == id:
                return idea
        return None

    def bookmark_idea(self, user_id: int, idea_id: int):
        if user_id not in self.bookmarks:
            self.bookmarks[user_id] = []
        self.bookmarks[user_id].append(idea_id)

    def get_bookmarks(self, user_id: int) -> List[Idea]:
        bookmarks = self.bookmarks.get(user_id, [])
        return [idea for idea in self.ideas if idea.id in bookmarks]

def load_ideas_from_json(data: Dict) -> List[Idea]:
    ideas = []
    for idea_data in data['ideas']:
        idea = Idea(
            id=idea_data['id'],
            title=idea_data['title'],
            industry=idea_data['industry'],
            tech_stack=idea_data['tech_stack'],
            validation_status=idea_data['validation_status'],
            early_adopters=idea_data['early_adopters'],
            revenue_signals=idea_data['revenue_signals']
        )
        ideas.append(idea)
    return ideas
