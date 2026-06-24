import pytest
from unittest.mock import patch
from io import StringIO
from idea_luminate import IdeaLuminate, Idea

@pytest.fixture
def idea_luminate():
    return IdeaLuminate()

def test_validate_input_valid(idea_luminate):
    assert idea_luminate.validate_input("Hello World") == True

def test_validate_input_empty(idea_luminate):
    assert idea_luminate.validate_input("") == False

def test_validate_input_too_long(idea_luminate):
    assert idea_luminate.validate_input("a" * 201) == False

def test_ask_question_valid(idea_luminate):
    with patch("builtins.input", return_value="Hello World"):
        assert idea_luminate.ask_question("What is your name? ") == "Hello World"

def test_ask_question_invalid(idea_luminate):
    with patch("builtins.input", side_effect=["", "Hello World"]):
        assert idea_luminate.ask_question("What is your name? ") == "Hello World"

def test_run_wizard(idea_luminate):
    with patch("builtins.input", side_effect=["Problem", "Target User", "Pain Severity", "Existing Solutions", "Unique Angle"]):
        idea = idea_luminate.run_wizard()
        assert isinstance(idea, Idea)
        assert idea.problem == "Problem"
        assert idea.target_user == "Target User"
        assert idea.pain_severity == "Pain Severity"
        assert idea.existing_solutions == "Existing Solutions"
        assert idea.unique_angle == "Unique Angle"

def test_display_summary(idea_luminate):
    idea = Idea("Problem", "Target User", "Pain Severity", "Existing Solutions", "Unique Angle")
    with patch("sys.stdout", new=StringIO()) as fake_stdout:
        idea_luminate.display_summary(idea)
        assert fake_stdout.getvalue() == "Summary:\nProblem: Problem\nTarget User: Target User\nPain Severity: Pain Severity\nExisting Solutions: Existing Solutions\nUnique Angle: Unique Angle\n"
