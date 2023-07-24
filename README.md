# Create FastAPI App

Create FastAPI App is a command-line tool that allows you to quickly set up a new FastAPI project with a predefined
directory structure and configurations. Inspired by `create-react-app` for React projects, this tool aims to simplify
the initial setup process and get you up and running with FastAPI in no time.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Rapid Setup**: Create a new FastAPI project effortlessly without worrying about the initial project structure and
  configurations.
- **Ready-to-Code**: Start coding your FastAPI application right away without spending time on boilerplate code.

## Prerequisites

Before using Create FastAPI App, you need to have the following tools installed on your system:

- Python (3.6 or higher)
- Pip (Python package manager)

## Installation

You can install Create FastAPI App using `pipx`. Open your terminal or command prompt and run the following command:
* `pipx install create-fastapi`

## Usage

To create a new FastAPI project, use the `create-fastapi-app` command followed by the desired project name:
`my-fastapi-app`

```bash
create-fastapi-app my-fastapi-app
```

By default, this will create a new FastAPI project in a directory named `my-fastapi-app`

Once the project is created, navigate to the project directory and start the development server:

- `cd my-fastapi-app`
- `python main.py`

## Project structure

- `app`: This directory contains the main application code.
    - `main.py`: Defines the main FastAPI application, including routes and endpoints.
    - `models`: Directory for data models and Pydantic schemas.
    - `routes`: Directory for organizing different API routes.
    - `utils`: Directory for utility functions and modules.

- `tests`: Contains test files to verify the application's functionality.

- `.env`: Environment variables file to store sensitive or configuration-specific data.

- `.gitignore`: Specifies the files and directories to be ignored by version control (e.g., `.env`, `__pycache__/`,
  etc.).

- `requirements.txt`: Lists the project dependencies needed to run the FastAPI application.
### Testing
* `pytest .`

### Linting
* `ruff .`

## Contributing

Contributions are welcome! If you find any issues with the tool or want to suggest enhancements, please create a GitHub
issue or submit a pull request.

## License

Create FastAPI App is open-source software licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
