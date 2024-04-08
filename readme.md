### HOW TO RUN THIS PROJECT


*   Install Docker and Docker-Compose
    ```
    $ docker --version
    $ docker-compose --version
    ```

*   Build the project
    ```
    $ docker-compose build
    ```

*   Run the project
    ```
    $ docker-compose up
    ```

### ABOUT THIS PROJECTS

This project is an example of how to use Django with Redis and Celery. This project retrieves data from https://geonode.com/free-proxy-list and saves it in a SQLite database. You can use the webpage to fetch data, or Celery Beat will schedule the data every day.

To run the project in a web browser, visit: http://localhost:8010
To access the Admin Panel, go to: http://localhost:8010/admin/
Username: nill
Password: nill@1234
