from datetime import datetime
from idea_luminate import Idea, IdeaLuminate, Update
import json
import pytest

def test_add_idea():
    idea_luminate = IdeaLuminate()
    idea = Idea(1, "Test Idea", 50)
    idea_luminate.add_idea(idea)
    assert len(idea_luminate.ideas) == 1

def test_get_update():
    idea_luminate = IdeaLuminate()
    idea = Idea(1, "Test Idea", 50)
    idea_luminate.add_idea(idea)
    idea_luminate.add_market_trend("Trend 1")
    idea_luminate.add_user_need("Need 1")
    update = idea_luminate.get_update(1)
    assert isinstance(update, Update)
    assert update.idea.id == 1
    assert update.market_trends == ["Trend 1"]
    assert update.user_needs == ["Need 1"]

def test_send_update():
    idea_luminate = IdeaLuminate()
    idea = Idea(1, "Test Idea", 50)
    idea_luminate.add_idea(idea)
    idea_luminate.add_market_trend("Trend 1")
    idea_luminate.add_user_need("Need 1")
    update = idea_luminate.send_update(1)
    update_json = json.loads(update)
    assert update_json["idea"]["id"] == 1
    assert update_json["idea"]["name"] == "Test Idea"
    assert update_json["idea"]["progress"] == 50
    assert update_json["market_trends"] == ["Trend 1"]
    assert update_json["user_needs"] == ["Need 1"]

def test_schedule_update():
    idea_luminate = IdeaLuminate()
    idea = Idea(1, "Test Idea", 50)
    idea_luminate.add_idea(idea)
    scheduled_date = idea_luminate.schedule_update(1)
    assert isinstance(scheduled_date, datetime)

def test_get_update_idea_not_found():
    idea_luminate = IdeaLuminate()
    with pytest.raises(ValueError):
        idea_luminate.get_update(1)

def test_schedule_update_idea_not_found():
    idea_luminate = IdeaLuminate()
    with pytest.raises(ValueError):
        idea_luminate.schedule_update(1)
