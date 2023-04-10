# Spotify Capstone Project - Data Engineering
<img width="882" alt="Introduction" src="https://user-images.githubusercontent.com/35566310/210912089-2c5aa605-66ad-46a2-b3c8-01470b024775.png">

<p align="justify"> 
Almost 10 years back — that the then-nascent term “data engineering” started to pop up in modern highly data-driven scaleups and fast-growing tech companies such as Facebook, Netflix, LinkedIn and Airbnb. As these companies harnessed massive amounts of real-time data that could provide high business value, software engineers at these companies had to develop tools, platforms and frameworks to manage all this data with speed, scalability and reliability. From this, the data engineer job started evolving to a role that transitioned away from using traditional ETL tooling to developing their own tooling to manage the increasing data volumes. 
</p>

<p align="justify">
As Data Engineers we built an ETL out of Spotify API using Apache Airflow and performed analysis using PowerBI. The analysis mainly focused on user activity. We developed a python script that extracts data from user spotify account by using Spotipy API. Once the data is extracted we stored the data in SQL Server Management Studio (SSMS). We followed Star Schema method to store the data. Then we connected the database engine to PowerBI, and developed dashboard in PowerBI for Analysis. At Last we performed scheduling using Apache Airflow. Our Project is a complete On-Premise solution.
</p>

# Overall Architecture
![overallArchitecture](https://user-images.githubusercontent.com/41756221/211175358-ec2deff8-9f1c-460d-bf0e-4db9e668eeed.png)

# Directory Structure and Description
![image](https://user-images.githubusercontent.com/35566310/230944352-3868495b-7e72-4d39-a8ea-da78071080bd.png)

                 

# About Spotify API
<p align="justify">
We extracted data out of the Spotify API using this endpoint to get the 25 most recently played tracks. The result of calling this endpoint is a dictionary which we will then take and create multiple dataframes after cleaning it up a bit first.
</p>

# Load Python and SQL Server Management Studio (SSMS)
<p align="justify">
We can connect to SSMS directly from Python using SQLalchemy library. Once the necessary libraries are installed we can connect to SSMS using Windows Authentication or using username and password. We used Windows authentication to connect SSMS, while connecting to SSMS we have to mention the user name and Database name. After a successful connection one can load the data directly from python to SSMS. 
</p>

We followed Star Schema approach to store the data in SSMS.

![Database_Schema](https://user-images.githubusercontent.com/35566310/210902041-7ab9a7f7-abc5-496b-836b-a9d517db5704.jpeg)

# PowerBI for Data Visualization
<p align="justify">
Initially we started the reporting phase with Tableau and we were able to generate worksheets with the data extracted. Then we switched to PowerBI as we were not able to display images dynamically from the ImageURL provided by Spotify. PowerBI was able to display the images once the data was selected. In PowerBI we used MS SQL connector to connect to the server and authenticate to the database. We created a simple dashboard which shows user details and information related to the users music taste.
</p>

![spotifydashboard](https://user-images.githubusercontent.com/41756221/211175578-ddec941e-fe3f-452c-84a6-99cc8cff6007.png)

# Scheduling and Automation using Apache Airflow
<p align="justify">
We used Apache Airflow for Scheduling and Automation. Airflow is a workflow management tool for scheduling data engineering pipelines. We developed the scripts and created DAG file to schedule the developed ETL scripts to run automatically. We installed Airflow in the Windows Subsystem for Linux(Ubuntu) so that we can orchestrate and monitor the jobs.

Commands used in WSL:

```pip3 install apache-airflow```

Save the ETL python files and <your DAG>.py in $AIRFLOW_HOME/dags (/root/airflow/dags/).

```airflow db init```

```airflow dags list```

```airflow tasks list spotify_dag```

```airflow scheduler```

```airflow webserver```

</p>

# Airflow DAG Run History
![Logs](https://user-images.githubusercontent.com/41756221/211175901-ab138cce-3cda-469e-ba8e-7baea9c4fb83.jpg)

# Concepts Implemented
1. Database Normalization
2. SQLalchemy Connection
3. Apache Airflow Scheduling
4. Object Oriented Programming
5. Data Modelling
6. Data Visualization
7. Orchestration and Scheduling

# Tools Used
1. Pycharm
2. PowerBI
3. Apache Airflow
4. SQL Server Management Studio

* Programming Language - Python
* Database Query Language - T-SQL
* Libraries Used - Pandas, SQLalchemy, urllib, Spotipy, Airflow, datetime
* Environment - Windows, Ubuntu

# Limitations
1. Spotify won’t allow to pull data for multiple users because of their security reasons. They allow users to pull data for single user account. 
2. We started with Tableau then we used PowerBI because Tableau was not able to display Artist images directly from web URLs.

# Future work
1. The report will aim to display more insights about the user's taste for music.
2. Machine Learning model will be applied on the data extracted to recommend tracks to the user based on the past history.

# References
### Airflow references
1. https://towardsdatascience.com/job-scheduling-with-apache-airflow-2-0-in-10-minutes-16d19f548a46
2. https://www.kirenz.com/post/2022-05-28-apache-airflow-installation-tutorial/

### Spotify API
1. https://spotipy.readthedocs.io/en/2.22.0/#
2. https://developer.spotify.com/documentation/general/guides/authorization/scopes/

### Other references
1. https://github.com/culpgrant/Spotify_ETL
