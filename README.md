# TBD Demo

A demonstration project for Trunk-Based Development (TBD) practices using FastAPI. This project showcases a simple web application with proper testing and development workflows.

## Project Overview

This project implements a basic web application using FastAPI and Jinja2 templates to demonstrate Trunk-Based Development practices. It includes:

- A simple homepage endpoint
- HTML template rendering
- Unit tests
- Type checking
- Development scripts

## Setup

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Development

### Git Hooks Configuration

This project uses Git hooks to ensure code quality. The pre-commit hook runs type checking and unit tests before each commit.

To set up the hooks:

```bash
git config core.hooksPath .githooks
```

The pre-commit hook will:
- Run type checking with mypy
- Execute unit tests with pytest
- Prevent commits if any checks fail

### Starting the Application

Run the development server:
```bash
./scripts/start.sh
```

The application will be available at http://localhost:8000

### Running Tests

Execute the test suite:
```bash
./scripts/test.sh
```

### Type Checking

Run static type checking:
```bash
./scripts/check_type.sh
```

## Project Structure

```
├── main.py              # FastAPI application entry point
├── test_main.py         # Unit tests
├── requirements.txt     # Project dependencies
├── templates/           # HTML templates
│   └── index.html      # Main page template
└── scripts/            # Development scripts
    ├── start.sh        # Script to start the application
    ├── test.sh         # Script to run tests
    └── check_type.sh   # Script to run type checking
```

## Development Workflow

This project follows Trunk-Based Development practices:

1. Make small, incremental changes
2. Write tests for new features
3. Ensure all tests pass before committing
4. Use type hints and run type checking
5. Keep the main branch stable

## Testing

The project includes several types of tests:

- Endpoint testing
- Template rendering tests
- Content verification tests

Tests are written using pytest and FastAPI's TestClient.

## License

This project is open-source and available under the MIT License.