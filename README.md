# FastAPI Simple Web App

## Description
A simple web application built using FastAPI that demonstrates basic API endpoints and serves HTML templates.

## What's Built
- Two API endpoints: one for fetching a greeting and another for fetching a list of items.
- An HTML template that displays a greeting message.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-simple-web-app.git
   cd fastapi-simple-web-app
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn jinja2
   ```
3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
4. Open your browser and navigate to `http://127.0.0.1:8000`.

## API Documentation
- `GET /api/greet`: Returns a greeting message.
- `GET /api/items`: Returns a list of items.

## Environment Variables
No environment variables are required for this application.