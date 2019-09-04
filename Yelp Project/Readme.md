# **Yelp Project**
Data from Yelp Inc. which included business attributes, user attributes, reviews, and checkin log
There are many parts in this project. I shall explain below.

There are five datasets: 'yelp_academic_dataset_checkin.json', 'yelp_academic_dataset_review.json', 'yelp_academic_dataset_business.json', 'yelp_academic_dataset_user.json', 'yelp_academic_dataset_tip.json'

**What can we do to make the data manageable?**

We can analyze subparts of this data by separating it by location or business category.
The business category I am interested in is Food. The location I am interested in is San Francisco Bay Area. But with the data available, the location I will be focusing on is Arizona and potentially Nevada.

** Objectives of this Project **

1. Discover some interesting trends on business closures

2. Understand the market and economic factors in the location. And how it can influence the businesses.

3. Improve user experience by offering them restaurants in the area they may be interested in based on their past reviews

4. Learn how to do text analysis and use Naive Bayes classifier

5. Study the behavior of checkins and how businesses can utilize checkins to improve traction. 

6. *action-oriented analyses*


** What are questions or topics we have for the Yelp dataset?**

* Does the overall sentiment for user's reviews correlate with the user's average_stars?

* Does the business location has an effect on total number of reviews for the business?

* What kind of categories in the Food section of Yelp are the most popular?

* Do Yelp users with no Yelp friends tend to post negative reviews?

* **Analyze the text of the reviews for specific categories such as service, food quality, and experience.**
    
    How do we quantify or qualify these categories to examine for in the text?
    
    
    * ** Predict ratings based on text of reviews **

* **Predict what kind of restaurants users would like based on past reviews**

* **Predict ratings based on similar businesses' rating and users' previous ratings**

* More reviews led to more stars, but what are other factors that led to higher rating besides popularity?

* Do checkin has an effect on the rating? For example, rate 5/5 for a free item.

* **The growth of food business in certain locations** 

* Does opening of a business led to greater average housing value in the area?

* Do certain areas have more expensive restaurants than others? What kind of users eat at these places?

* **Why do businesses close? Does it affect the location?**

* Which category of business is popular?

* User acquistion 

* Which metropolian area is popular for its food scene?

**What are other data we can combine with this data?**

We can use social media data, census tract data, transportation data, housing sale price data, and etc.

Median Income Level of Neighborhoods. 

Sources: https://www.phoenixopendata.com, https://www.phoenix.gov/nsdsite/Documents/lowmod-ct51.pdf,
https://www.governing.com/gov-data/phoenix-gentrification-maps-demographic-data.html

**Definitions**
Reviews with 3 stars are considered neutral. x>3 is considered positive. x < 3 is considered negative.


**Challenges to our Questions and Expectations**

I thought that we can filter by location and study specific locations but the yelp academic dataset is limited. In the dataset, it is only limited to 19 businesses in CA. It is difficult to understand growth and urban problems. Looking at the value counts of businesses in each state, AZ, NV, and ON have significant numbers of businesses we can study for location. Thus, if we continue with that area of study, AZ would be a good location pick.

There are lot of data in this package. There will be alot of features we do not need to evaluate in our study. The challenge is picking what features are important to answering our questions. 

The location's latitude and longitude doesn't match up with the address or there could be multiple businesses in one latitude and longitude but it doesn't tell us if that is one physical location.

Future Plans:

Built an uniform script for other states

## Data Visualizations
  Tools: matplotlib, seaborn, pandas
  - number of new Yelp users enrolling per Year
  - number of restaurants in each star group
  - visualizing the restaurants in Arizona with different hues of a third variable
## Regression Analysis on Measurable Metrics
  Tools: sklearn, pandas
  - Linear regression on whether total number of checkins, total number of reviews, percentage of positive
  reviews, percentage of negative reviews have a significant effect on the average rating of the business store.
## Restaurant Demand and Supply
  Tools: pandas, seaborn
  - Studying the reasons why restaurant closed down
  - Growth rate of the restaurant market in Arizona
  - Number of new businesses enrolling on Yelp in Arizona
## Recommendation Models
  Tools: sklearn, nltk
  - Finding similar businesses based on the content of the reviews
## Geospatial Location Analysis 
  - tools: requests, urllib, json, Census Tract API, seaborn
  - Location is important in the growth of the business. Find out how and whether it truly does.
## Sentiment Analysis of Reviews
  Tools: RandomForest, sklearn, pandas, nltk, countvector
  - Classification
  - Predicting the sentiment of the reviews based on the content
  - Predicting the rating of the reviews based on the content
  - Collocation and commonly occuring words in the reviews
  
  
  
