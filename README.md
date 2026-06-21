# Validation Score Model

This project calculates a validation score for an idea based on its trend, Reddit volume, and sentiment.
The score is a combination of these factors, weighted to produce a score between 0 and 100.

## Usage

To use this project, create an instance of the `Idea` class and pass it to the `validate_idea` function.
The function returns a dictionary containing the validation score and a brief explanation of the contributing factors.

## Testing

To run the tests, use the `pytest` command.
The tests cover the happy path and edge cases, including zero and maximum values for the input factors.
