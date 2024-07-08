# Joke Generator

This is a simple Joke Generator Flask application, containerized with Docker and served through Nginx.


## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Local Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/althaffazil/JokeGenerator.git
    cd JokeGenerator
    ```

2. **Build and start the Docker containers:**

    ```bash
    docker-compose -f docker-compose.yml up --build
    ```

3. **Access the application:**

    Open your browser and go to `http://localhost:5000`.

