from idea_luminate import Idea, IdeaLuminate

def test_add_idea():
    idea_luminate = IdeaLuminate()
    idea = Idea("Test Idea", 100, 50, 20)
    idea_luminate.add_idea(idea)
    assert len(idea_luminate.get_ideas()) == 1

def test_get_ideas():
    idea_luminate = IdeaLuminate()
    idea1 = Idea("Test Idea 1", 100, 50, 20)
    idea2 = Idea("Test Idea 2", 200, 60, 30)
    idea_luminate.add_idea(idea1)
    idea_luminate.add_idea(idea2)
    ideas = idea_luminate.get_ideas()
    assert len(ideas) == 2
    assert ideas[0].name == "Test Idea 1"
    assert ideas[1].name == "Test Idea 2"

def test_sort_ideas_by_search_volume():
    idea_luminate = IdeaLuminate()
    idea1 = Idea("Test Idea 1", 100, 50, 20)
    idea2 = Idea("Test Idea 2", 200, 60, 30)
    idea_luminate.add_idea(idea1)
    idea_luminate.add_idea(idea2)
    sorted_ideas = idea_luminate.sort_ideas_by_search_volume()
    assert sorted_ideas[0].name == "Test Idea 1"
    assert sorted_ideas[1].name == "Test Idea 2"

def test_sort_ideas_by_competition():
    idea_luminate = IdeaLuminate()
    idea1 = Idea("Test Idea 1", 100, 50, 20)
    idea2 = Idea("Test Idea 2", 200, 60, 30)
    idea_luminate.add_idea(idea1)
    idea_luminate.add_idea(idea2)
    sorted_ideas = idea_luminate.sort_ideas_by_competition()
    assert sorted_ideas[0].name == "Test Idea 1"
    assert sorted_ideas[1].name == "Test Idea 2"

def test_sort_ideas_by_willingness_to_pay():
    idea_luminate = IdeaLuminate()
    idea1 = Idea("Test Idea 1", 100, 50, 20)
    idea2 = Idea("Test Idea 2", 200, 60, 30)
    idea_luminate.add_idea(idea1)
    idea_luminate.add_idea(idea2)
    sorted_ideas = idea_luminate.sort_ideas_by_willingness_to_pay()
    assert sorted_ideas[0].name == "Test Idea 1"
    assert sorted_ideas[1].name == "Test Idea 2"

def test_get_validation_metrics():
    idea_luminate = IdeaLuminate()
    idea = Idea("Test Idea", 100, 50, 20)
    idea_luminate.add_idea(idea)
    metrics = idea_luminate.get_validation_metrics("Test Idea")
    assert metrics == {
        "search_volume": 100,
        "competition": 50,
        "willingness_to_pay": 20
    }

def test_get_validation_metrics_non_existent_idea():
    idea_luminate = IdeaLuminate()
    metrics = idea_luminate.get_validation_metrics("Non Existent Idea")
    assert metrics is None
