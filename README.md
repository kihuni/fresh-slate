# Fresh Slate API

This is the API documentation for the Fresh Slate project. The API allows you to manage goals, milestones, daily progress, and productivity patterns.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/fresh-slate.git
    cd fresh-slate

    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv .venv
    source .venv/bin/activate

    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt

    ```

4. Apply the migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate

    ```

5. Create a superuser:
    ```
    python manage.py createsuperuser

    ```

6. Run the development server:
    ```

    python manage.py runserver
    
    ```

## API Endpoints

### Goals

- **List all goals**: `GET /goals/`
- **Create a new goal**: `POST /goals/`
- **Retrieve a goal**: `GET /goals/{id}/`
- **Update a goal**: `PUT /goals/{id}/`
- **Delete a goal**: `DELETE /goals/{id}/`

### Milestones

- **List all milestones**: `GET /milestones/`
- **Create a new milestone**: `POST /milestones/`
- **Retrieve a milestone**: `GET /milestones/{id}/`
- **Update a milestone**: `PUT /milestones/{id}/`
- **Delete a milestone**: `DELETE /milestones/{id}/`

### Daily Progress

- **List all daily progress**: `GET /daily-progress/`
- **Create a new daily progress**: `POST /daily-progress/`
- **Retrieve a daily progress**: `GET /daily-progress/{id}/`
- **Update a daily progress**: `PUT /daily-progress/{id}/`
- **Delete a daily progress**: `DELETE /daily-progress/{id}/`

### Productivity Patterns

- **List all productivity patterns**: `GET /productivity-patterns/`
- **Create a new productivity pattern**: `POST /productivity-patterns/`
- **Retrieve a productivity pattern**: `GET /productivity-patterns/{id}/`
- **Update a productivity pattern**: `PUT /productivity-patterns/{id}/`
- **Delete a productivity pattern**: `DELETE /productivity-patterns/{id}/`

## API Documentation

The API documentation is available at the following URLs:

- **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Running Tests

To run the tests, use the following command:

```
python manage.py test

```
