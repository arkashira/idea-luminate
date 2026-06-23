# REQUIREMENTS.md
## Introduction
The idea-luminate project aims to create a database of pre-validated software ideas. This document outlines the functional and non-functional requirements for the project.

## Functional Requirements
1. **FR-1: Idea Database Creation**: The system shall allow users to create an instance of the `IdeaDatabase` class.
2. **FR-2: Idea Addition**: The system shall provide an `add_idea` method to add new ideas to the database.
3. **FR-3: Idea Search**: The system shall provide a `search` method to search for ideas in the database based on relevant criteria (e.g., keywords, categories).
4. **FR-4: Idea Retrieval**: The system shall provide a `get_idea` method to retrieve an idea by its unique ID.
5. **FR-5: Idea Bookmarking**: The system shall provide a `bookmark_idea` method to bookmark an idea for a specific user.
6. **FR-6: Bookmark Retrieval**: The system shall provide a `get_bookmarks` method to retrieve a list of bookmarked ideas for a specific user.

## Non-Functional Requirements
### Performance
1. **PER-1: Response Time**: The system shall respond to user requests (e.g., search, retrieval) within 500 milliseconds.
2. **PER-2: Data Storage**: The system shall be able to store a minimum of 10,000 ideas in the database.

### Security
1. **SEC-1: Authentication**: The system shall implement user authentication to ensure only authorized users can access and modify the database.
2. **SEC-2: Data Encryption**: The system shall encrypt sensitive data (e.g., user credentials, idea descriptions) to prevent unauthorized access.

### Reliability
1. **REL-1: Uptime**: The system shall maintain an uptime of at least 99.9% to ensure users can access the database at all times.
2. **REL-2: Error Handling**: The system shall implement robust error handling to handle unexpected errors and exceptions.

## Constraints
1. **CON-1: Technology Stack**: The system shall be built using Python and utilize the pytest framework for testing.
2. **CON-2: Database Schema**: The system shall use a predefined database schema to store ideas and user bookmarks.

## Assumptions
1. **ASM-1: User Input**: Users will provide valid and relevant input when adding ideas or searching the database.
2. **ASM-2: Network Connectivity**: Users will have a stable internet connection to access the system.

## Acceptance Criteria
The system shall meet all functional and non-functional requirements outlined in this document. The system shall be tested using pytest to ensure it meets the required standards.
