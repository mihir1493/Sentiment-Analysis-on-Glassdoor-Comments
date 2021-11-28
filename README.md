# Sentiment-Analysis-on-Glassdoor-Comments
Webscraping Glassdoor Comments and Conducting Exploratory Data Analysis, Sentiment Analysis, Topic Modelling on the employee reviews. 

Final Project NLP Analysis Notebook for each company:

**Walmart**: https://nbviewer.org/github/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/walmart/Glassdoor%20NLP%20Project%20-%20Walmart.ipynb

**Comcast**: https://nbviewer.org/github/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/comcast/Glassdoor%20NLP%20Project%20-%20Comcast.ipynb

**Wells Fargo**: https://nbviewer.org/github/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/wells%20fargo/Glassdoor%20NLP%20Project%20-%20Wells%20Fargo.ipynb

**Fedex**: https://nbviewer.org/github/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/fedex/Glassdoor%20NLP%20Project%20-%20Fedex.ipynb

# Project Summary
The Internet allows users to have a space where they can share, express and receive opinions. It is used by almost everyone such as employees, recruiters, small and medium business owners and all kinds of various organizations. In recent times, with the launch of platforms like LinkedIn, Glassdoor or Indeed, employees have opted to review and anonymously give feedback about their organizations. Our team plans on gathering and analyzing these feedbacks. And then draw a comparison between different organizations in the US job market. 

Reading through scores of reviews on job platforms can be a real taxing effort while searching for a job. One must closely examine each and every review to try and form an opinion about the company. Moreover, reading thousand and thousands of comments posted for each company, potential employee is often left with a biased opinion developed over reading initial comments that he/she is exposed to. 
  
Through this project we hope to deliver a deeper insight into the company through the eyes of its current and former employee to provide a transparent insight into the company. Though sentiment analysis on the comments obtained from the portal we wish to glean an understanding of key topics such as benefits, management, culture, work-life balance, environment, diversity & inclusion.

Companies selected for analysis:
| Sr.No | Company Name |     Data Types    | Number of Reviews |                Domain                |
|:-----:|:------------:|:-----------------:|:-----------------:|:------------------------------------:|
| 1     | Walmart      | Numeric & Textual |        9970       |          E-commerce/ Retail          |
| 2     | Wells Fargo  | Numeric & Textual |       10000       | Finance/Banking/Retirement Solutions |
| 3     | Comcast      | Numeric & Textual |       10000       |             Broadcasting             |
| 4     | Fedex        | Numeric & Textual |        7053       |           Logistic/ Courier          |

### Code and Resources Used 
**Python Version:** 3.8  
**Packages:** pandas, numpy, scrapy, nltk, sklearn, matplotlib, seaborn, json  
**Scrapy Website:** https://docs.scrapy.org/en/latest/  

## Web Scraping Target Elements
Extracting the following elements for each glassdoor review posted:
*	Rating
*	Employee Type - Current/ Former Employee
*	Review - Short Review Title
*	Pros
*	Cons
*	Date Posted
*	Job Title - Position held at the company

## Web Scraping File: [Click Here](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/glassdoor/glassdoor/spiders/glassdoor_spider.py)

Scrapy is one the most powerful web scraping scalable framework in python. 

1.	Creating a virtual environment for web scraping – scrapy_ds 
2.	Installing the requirements (pip install)
3.	Create a scrapy project called Glassdoor – generate a scrapy default template
4.	Creating a spider to crawl the Glassdoor Walmart url
5.	Specifying items to extract using xpath selector 
6.	Adding fake user agents to bypass restrictions using Scrapy-UserAgents Library – Rotating user agents tricks the glassdoor website who will flag the IP if the request limit reaches a certain threshold. 
7.	Using pagination to cycle through the website pages to extract the features for each review posted on a single page. 
8.	Exporting the scraped data into a json format to perform sentiment analysis

## Web Scraping Steps:
*	Installing the requirements using requirements.txt (pip install)
*	Create a scrapy project called Glassdoor – generate a scrapy default template
*	Creating a spider to crawl the Glassdoor company url link
![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture1.jpg)
*	Specifying items to extract using css selectors
![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture2.jpg)
*	Adding fake user agents to bypass restrictions using Scrapy-User-Agents Library – Rotating user agents tricks the glassdoor website who will flag the IP if the request limit reaches a certain threshold.
![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture3.jpg)
*	Using pagination to cycle through the website pages to extract the features for each review posted on a single page.
![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture4.jpg)
*	Exporting the scraped data into a json format to perform sentiment analysis
![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture5.jpg)

## Data Dictionary: 
| Index | Attribute Name |          Description         |  Data Type |         Source         |
|:-----:|:--------------:|:----------------------------:|:----------:|:----------------------:|
|   1   |     Rating     |  Company Rating Scale (0-5)  |   Object   | https://glassdoor.com/ |
|   2   |  Employee Type |   Current/ Former Employee   |   Object   | https://glassdoor.com/ |
|   3   |     Review     |            Review            |   Object   | https://glassdoor.com/ |
|   4   |      Pros      |     Advantages/ Benefits     |   Object   | https://glassdoor.com/ |
|   5   |      Cons      |      Disadvantages/ Cons     |   Object   | https://glassdoor.com/ |
|   6   |      Date      |          Date Posted         | Datetime64 | https://glassdoor.com/ |
|   7   |    Job Title   | Position held at the company |   Object   | https://glassdoor.com/ |

## Data Cleaning: [Click Here](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/Glassdoor_Data_Cleaning.ipynb)
Data cleaning is an important step in any analysis project. For this particular case the data extracted from webscraping the glassdoor page was nested with the key being the feature and the value being a list of 10 elements for single page of the website

*	In order to perform analysis we needed to create a dataframe without the nesting where each element is represented across a single row containing the value for each entity

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture6.jpg)
*	To fix this issue we use the pandas >= 0.25, explode() function to transform each list in cell into an independent row across all column

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture7.jpg)
*	The next step in preprocessing our dataframe involved splitting the date_position column that contained the date and the job title of the individual. To create new columns by splitting the date_position column we use the split method on the column
 
![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture8.jpg)
*	After splitting the date_position column, the date column still exists as an object so we need to convert it into date type to perform further analysis. To do this, we use the pd.to_datetime function on the column date
*	Removing the index column from the dataframe using df.drop function in pandas
*	Exporting the dataframe as csv – cleaned_data.csv

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/Picture9.jpg)

## Data Analysis: [Click Here](https://nbviewer.org/github/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/wells%20fargo/Glassdoor%20NLP%20Project%20-%20Wells%20Fargo.ipynb#topic=1&lambda=0.44&term=)

* Plotting Distribution for Review Length vs Number of review

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a1.JPG)

* Plotting review rating frequency count

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a2.png)

* Employee Type Vs Rating 

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a3.png)

* Review Count Timeline

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a4.png)

* Review Count by Job Title
 
![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a5.png)

* Top Review Counts by Job Title

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a6.JPG)

* Word Cloud for Pros in all reviews combined

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a7.png)

* Word Cloud for Cons in all reviews combined

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a8.png)

* Review Length for each rating

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a9.JPG)

* Box Plot for review length 

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a10.JPG)

* Performing Topic Modelling with 5 specified topics

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a11.JPG)

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a12.JPG)

* Sentiment Analysis with emotion classification

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a13.png)

* Bi-Grams 

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a14.JPG)

* Tri-Grams

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a15.JPG)

* Name Entity Recognition using Spacy

![alt text](https://github.com/mihir1493/Sentiment-Analysis-on-Glassdoor-Comments/blob/main/img%20src/a16.png)


 

























