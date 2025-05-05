# Simple Python Web App (To-Do List) using Docker

This is a simple Python web application that allows users to view and add tasks to a to-do list.

## Steps to Build and Run the Application

1. Clone this repository:
    ```bash
    git clone https://github.com/Darw1n-Dav1s/To-do-list-application-using-docker.git
    ```
    ```
    cd To-do-list-application-using-docker
    ```

2. Docker should be installed.

   To install : https://docs.docker.com/get-docker/     

3. Build the Docker image:
    ```bash
    docker build -t todo-app .
    ```

4. Run the Docker container:
    ```bash
    docker run -p 5000:5000 todo-app
    ```

5. Visit the app at `http://localhost:5000` in your web browser.
