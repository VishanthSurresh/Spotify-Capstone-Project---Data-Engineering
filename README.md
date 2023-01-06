# Spotify Capstone Project - Data Engineering
Almost 10 years back — that the then-nascent term “data engineering” started to pop up in modern highly data-driven scaleups and fast-growing tech companies such as Facebook, Netflix, LinkedIn and Airbnb. As these companies harnessed massive amounts of real-time data that could provide high business value, software engineers at these companies had to develop tools, platforms and frameworks to manage all this data with speed, scalability and reliability. From this, the data engineer job started evolving to a role that transitioned away from using traditional ETL tooling to developing their own tooling to manage the increasing data volumes. 

As Data Engineers we built an ETL out of Spotify API using Apache Airflow and performed analysis using Tableau. The analysis mainly focused on user activity. We developed a python script that extracts data from user spotify account by using Spotipy API. Once the data is extracted we stored the data in SQL Server Management Studio (SSMS). We followed Star Schema method to store the data. Then we connected the database engine to Tableau, and developed dashboard in Tableau for Analysis. At Last we performed scheduling using Apache Airflow. 

# Overall Architecture
![Spotify_Architecture](https://user-images.githubusercontent.com/35566310/210908261-fea19bc0-a78a-45ff-a955-ff8ce97f55bb.png)

# About Spotify API
We extracted data out of the Spotify API using this endpoint to get the 25 most recently played tracks. The result of calling this endpoint is a dictionary which we will then take and create multiple dataframes after cleaning it up a bit first.

# Load Python and SQL Server Management Studio (SSMS)
We can connect to SSMS directly from Python using SQLAchamey library. Once the necessary libraries are installed we can connect to SSMS using Windows Authentication or using username and password. We used Windows authentication to connect SSMS, while connecting to SSMS we have to mention the user name and Database name. After a successful connection one can load the data directly from python to SSMS. 

We followed Star Schema approach to store the data in SSMS.

![Database_Schema](https://user-images.githubusercontent.com/35566310/210902041-7ab9a7f7-abc5-496b-836b-a9d517db5704.jpeg)

# Scheduling and Automation using Apache Airflow
We used Apache Airflow for Scheduling and Automation
