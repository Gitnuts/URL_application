# URL_application

In this README.md you find how to run the application. The application periodically scans a list of http URLs to find out whether a page meets requirements. 

To run the application, you need to install Docker / Docker Desktop. Once Docker was installed, go to the folder that contains Dockerfile and run the following command in a terminal:

``` docker build . ```

This will build the image. Then go back to and run these two commands:

``` docker-compose build --pull ```

``` docker-compose up ```

This starts up a docker image with an airflow container but also sets up python libraries that we need for the application. Airflow sits on port 8080, thus to launch the application, go to:

``` localhost:8080 ```

and switch on the DAG. If you want to change the periodicity of the application, you may adjust the ```schedule_interval``` parameter in dag_file.py. Logfile should be generated in the log folder after the first run.

# Design question

In a case of the application that runs from multiple geographically distributed locations, we may want to connect these nodes, for example with Kafka server, build secured channels with SSH between them and send data to a single report. If security is an issue, we may also want to set up requests with POST rather than GET method.
