A multi-narrative, multi-platform information tracing dashboard
=========

- A dashboard built on top of Information Tracer data 
- Useful to monitor multiple narratives over multiple platforms
- Real-world use case: monitor and compare popularity and sentiments of 4 candidates during the 2023 Coahuila Election  

[**How to use this dashboard**](#how-to-use-this-dashboard) | 
[**Installation and Configuration**](#installation-and-configuration) |

## General Functions of the Dashboard
- Hover on graphs to see statistics in details.
- Customize timeframe by dragging the blue time bar below each graph.
- Click on legends to show or hide a candidate.
- Click "Grouped" or "Stacked" to change bar plot orientation.
- Search bar: enter keywords to filter records.
- Drag columns to change the order of table.
- Click on column names to sort tables.
- Hover on an edge or node to check weight and highlight part of the network.


## How to use this dashboard?

### Content 
- **Interactions**
- **Sentiment Analysis**
- **Principal Actor and Word Cloud**
- **Network Analysis**


### Interactions

**How we define interactions?**<br>
.....

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


## Architecture
Database Schema,
update mechanism, etc

## Installation and Configuration
[TODO]

## License
MIT

