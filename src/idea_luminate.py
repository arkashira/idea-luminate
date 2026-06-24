import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Idea:
    problem: str
    target_user: str
    pain_severity: str
    existing_solutions: str
    unique_angle: str

class IdeaLuminate:
    def __init__(self):
        self.steps = [
            "Problem",
            "Target User",
            "Pain Severity",
            "Existing Solutions",
            "Unique Angle"
        ]
        self.current_step = 0
        self.idea = Idea("", "", "", "", "")

    def validate_input(self, input_str: str) -> bool:
        return input_str.strip() != "" and len(input_str) <= 200

    def ask_question(self, question: str) -> str:
        while True:
            user_input = input(question)
            if self.validate_input(user_input):
                return user_input
            print("Invalid input. Please enter a non-empty string with a maximum of 200 characters.")

    def run_wizard(self) -> Idea:
        for i, step in enumerate(self.steps):
            self.current_step = i
            if step == "Problem":
                self.idea.problem = self.ask_question("What is the problem you're trying to solve? ")
            elif step == "Target User":
                self.idea.target_user = self.ask_question("Who is the target user for this solution? ")
            elif step == "Pain Severity":
                self.idea.pain_severity = self.ask_question("How severe is the pain point for the target user? ")
            elif step == "Existing Solutions":
                self.idea.existing_solutions = self.ask_question("What existing solutions are there for this problem? ")
            elif step == "Unique Angle":
                self.idea.unique_angle = self.ask_question("What's the unique angle for your solution? ")
            print(f"Step {i+1} of {len(self.steps)} completed.")
        return self.idea

    def display_summary(self, idea: Idea) -> None:
        print("Summary:")
        print(f"Problem: {idea.problem}")
        print(f"Target User: {idea.target_user}")
        print(f"Pain Severity: {idea.pain_severity}")
        print(f"Existing Solutions: {idea.existing_solutions}")
        print(f"Unique Angle: {idea.unique_angle}")

def main() -> None:
    idea_luminate = IdeaLuminate()
    idea = idea_luminate.run_wizard()
    idea_luminate.display_summary(idea)

if __name__ == "__main__":
    main()
