# Infrastructure Overview
This application is built using FastAPI, a modern web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Data Models
- **Item**: A simple model with `id` (int) and `name` (str).

## API Design
- **GET /api/greet**: Returns a JSON response with a greeting message.
- **GET /api/items**: Returns a JSON response with a list of items.

## Key Decisions
- FastAPI was chosen for its speed and ease of use.
- Jinja2 is used for rendering HTML templates.