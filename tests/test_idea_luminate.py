import pytest
from idea_luminate import Idea, IdeaDatabase, load_ideas_from_json

def test_add_idea():
    db = IdeaDatabase()
    idea = Idea(1, 'Test Idea', 'Tech', 'Python', 'Validated', 10, 100)
    db.add_idea(idea)
    assert len(db.ideas) == 1

def test_search():
    db = IdeaDatabase()
    idea1 = Idea(1, 'Test Idea', 'Tech', 'Python', 'Validated', 10, 100)
    idea2 = Idea(2, 'Another Idea', 'Finance', 'Java', 'Not Validated', 5, 50)
    db.add_idea(idea1)
    db.add_idea(idea2)
    results = db.search('Test')
    assert len(results) == 1
    assert results[0].title == 'Test Idea'

def test_get_idea():
    db = IdeaDatabase()
    idea = Idea(1, 'Test Idea', 'Tech', 'Python', 'Validated', 10, 100)
    db.add_idea(idea)
    retrieved_idea = db.get_idea(1)
    assert retrieved_idea.title == 'Test Idea'

def test_bookmark_idea():
    db = IdeaDatabase()
    idea = Idea(1, 'Test Idea', 'Tech', 'Python', 'Validated', 10, 100)
    db.add_idea(idea)
    db.bookmark_idea(1, 1)
    bookmarks = db.get_bookmarks(1)
    assert len(bookmarks) == 1
    assert bookmarks[0].title == 'Test Idea'

def test_load_ideas_from_json():
    data = {
        'ideas': [
            {'id': 1, 'title': 'Test Idea', 'industry': 'Tech', 'tech_stack': 'Python', 'validation_status': 'Validated', 'early_adopters': 10, 'revenue_signals': 100},
            {'id': 2, 'title': 'Another Idea', 'industry': 'Finance', 'tech_stack': 'Java', 'validation_status': 'Not Validated', 'early_adopters': 5, 'revenue_signals': 50}
        ]
    }
    ideas = load_ideas_from_json(data)
    assert len(ideas) == 2
    assert ideas[0].title == 'Test Idea'
    assert ideas[1].title == 'Another Idea'
