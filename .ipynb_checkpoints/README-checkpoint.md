# 1-blue-json-mraz Project 1

## Group Name
1-blue-json-mraz

# Topic

## Team Members & Roles
* Felipe Lopez | **Github Admin**
* Carlos Pires | **Visualization, Analyst**
* Michelle Nguyen | **Visualtion, Analyst**
* Karen Kitchens | **Python, Github Admin**
* Reid Haynie  | **API Guru, SME**
* All | **Data Munge**
* Presenters | **Felipe/ Reid**

## Background: Campaign Fund Raising

This project aims to answer the questions ff these variables which one has the largest effect on your ability to raise money out of state, Incumbency, Partisanship, State, Election Cycle based on the resources below.

As a Congressional candidate what indicates the probability of you being able to pull in money from out of state. Creating a Candidate Demographic*- what kind of candidate is more likely to get money from out of state. 

* Candidate Demographics (Incumbant/Challenger, Gender, Religion, Party, Age-Range, Rural, Education, Income, Race)

## Data Sources
* A `config.py` file will be required for the notebook to run. This contains the FEC API Key. We are pulling donations from individual donors.
* FEC API 
    * Canidate information ="https://api.open.fec.gov/v1/candidates/"
    * Finance Data ="https://api.open.fec.gov/v1/schedules/schedule_a/by_state/by_candidate/"
* Census API
    * url = 

* We started out with 2 seperate CSV files that seperated financial data by Democratic and Republicans then we ended up merging into one.

## Data Munging

## QUESTIONS and Analysis: 
* How much $$ was raised by Democrats based on individual donors by state?
* Total $ raised by state
* Who were the top 3
* Who does better raising funds, incumbents or challenger?
* Which state raised more money?
* How much money this state donates to other states campaign?
* Which candidates received more donation from this state.


Visualizations - 
1st visualization - Which states have the most funding? Republicans & Democrats per state
2nd visualization - For that state with the most funds, split Republicans and Democrats (ex. California and Texas)
3rd visualization - How much money donated were from instate/outofstate/superpacs?
4th visualization - Top 2 Senate candidates (Republican + Democrat from each state) per state

