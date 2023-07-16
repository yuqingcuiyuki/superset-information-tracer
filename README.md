A multi-narrative, multi-platform information tracing dashboard
=========

- A dashboard built on top of [Information Tracer](https://informationtracer.com/) data 
- Useful to monitor multiple narratives over multiple platforms (Twitter, Facebook, Instagram, Youtube, Reddit)
- **Real-world use case**: monitor and compare popularity and sentiments of 4 candidates during the [2023 Coahuila Election](https://mexico.informationtracer.com/superset/dashboard/12/) ([media coverage](https://conecta.tec.mx/es/noticias/nacional/educacion/docentes-de-tec-y-nyu-crean-plataforma-que-analiza-redes-en-elecciones))

![image](https://github.com/zhouhanc/superset-information-tracer/assets/71556325/6130b4e5-1f0f-4cc6-afaa-ef356dff162f)


<br>

[**General Functions of the Dashboard**](#general-functions-of-the-dashboard) |
[**Graph Documentation**](#graph-documentation) | 
[**Architecture**](#architecture) |
[**Installation and Configuration**](#installation-and-configuration) 

## General Functions of the Dashboard
### Interactivity:
- **Hover**: Hover on graphs to see statistics in details; Hover on an edge or node to check weight and highlight part of the network.
- **Click**: Click on legends to show or hide a candidate; Click "Grouped" or "Stacked" to change bar plot orientation.
- **Sort**: Click on column names to sort tables.
- **Search**: enter keywords into search bar to find records.
- **Drag**: Drag columns to change the order of table; Customize timeframe by dragging the blue time bar below each graph.

### Filtering:
Expand the sidebar to select sentiment type, node names and edge weights and click apply tp update the whole dashbaord.

### Others:
- **Refresh**: Manually force refresh dashboard to show latest data or set auto-refresh interval.
- **Download & Export**: Save dashboard and/or analytics as images; Export analytics as csv. 


## Graph Documentation

### Content 
- [**Interactions**](#interactions)
- [**Sentiment Analysis**](#sentiment-analysis)
- [**Principal Actor and Word Cloud**](#principal-actor-and-word-cloud)
- [**Network Analysis**](#network-analysis)


### Interactions

**How we define interactions?**<br>
- Twitter: The total number of retweet count and like count on a Twitter post
- Facebook: The total number of reactions, shares and comments on a Facebook post
- Instagram: The total number of likes and comments on an Instagram post
- Youtube: The total number of like count and comment count on a Youtube video

**1. Total Interactions**<br>
This graph shows how total number of daily interactions (aggregated statistics from Twitter, Facebook, Instagram, Youtube) change by time for different candidates.
 
**2. Interactions by Platform**<br>
  - **Total Interactions** <br>
This graph shows how daily interactions change by time on a specific platform for different candidates.

  - **Cumulative Interactions**<br>
This graph shows how cumulative interactions change by time on a specific platform for different candidates. It's useful for identifying long-term trends and overall patterns in the data.

  - **Interaction Percentage**<br>
This graph shows daily interactions as a percentage on a specific platform for different candidates. <br>
$$\frac{\text{candidate}_i \text{ interaction}}{\sum\text{candidate}_i \text{ interaction}}$$




### Sentiment Analysis
We work with three types of sentiment: Positive, Neutral, Negative. To improve the accuracy of sentiment analysis, we parse each post into individual sentences and assign each sentence the interaction of that post.<br>
<br>
**1. Evaluación total**<br>
This graph shows the cumulative number of sentences of each sentiment type by candidates. 

**2. Evaluación en el tiempo**<br>
This graph shows the number of sentences of each sentiment type by candidates daily.

**3. Interacciones totales**<br>
Graph 1 and 2 only consider number of sentences. Graph 3 and 4 use number of interactions of each sentence as a weight. For example, if a sentence is negative and has 1k interactions, all 1k interactions will be put into negative class. This graph shows the cumulative number of interactions of each sentiment type by candidates. 

**4. Interacciones en el tiempo**<br>
This graph shows the number of interactions of each sentiment type by candidates daily.


### Principal Actor and Word Cloud
**1. Principal Actor**<br>
This table shows username, number of interactions and post content of top posts within last 14 days for each candidate on each platform.

**2. Word Cloud**<br>
It shows words that occur most from all posts related to a candidate on a platform within last 14 days.

### Network Analysis
Each **node** represents a user, a hashtag or an url.<br>
An **edge** means a user post with this hashtag or url.<br>

How we calculate the **weight of an edge** between node user-A and node hashtag-B:<br>
1. Collect all posts from user-A that mentions hashtag-B
2. Sum up all interaction counts 
3. Take the natural logarithm of the sum (why? the edge weight follows a logarithmic distribution. we take the log to visualize edges because the visualization tool assumes a linear weight distribution)

The network graph is cumulative.

## Architecture
![workship architecture](https://github.com/zhouhanc/superset-information-tracer/assets/71556325/07b4b3d3-9dde-4c4d-9495-43692803cdf2)

**Update Mechanism**<br>
- **Daily Update:** We perform daily data collection at 11:45 PM UTC to capture the latest data for the current day.
- **Refresh:** We also refresh data collected 48 hours ago, as real-time interactions tend to stabilize after this time period.

## Installation and Configuration
- Clone the repository
```
git clone https://github.com/zhouhanc/superset-information-tracer.git
```
- Prepare db_info.txt, infotracer_token.txt, youtube_tokens.txt and modify paths
- Schedule database_buildup.py daily using crontab
```
# create crontab job
crontab -e

PATH=<...> # sync the path with system
45 23 * * * python ~/superset-information-tracer/database_buildup.py >> /tmp/dashboard_log/monitor_$(date +\%Y\%m\%d_\%H\%M\%S).txt
# add empty line at the end to run

# exit and view crontab job
crontab -l
```



## License
MIT

