# Project Outline

### Questions for Visuals 10/1/20:
* Regardless of party do you raise more money as a challenger or incumbent?
* One column per party average raised by party
* On average do incumbents or challengers raise more money?
* If your an incumbent do you raise more money in state?
* How viable is a state in regards to raising money out of state?
* 


### Roles

**Reid** : API Guru, SME

**Carlos**: Analyst, make correlations

**Karen**: Python, Github Admin, Co-lead

**Felipe**: PM, Co-lead

**Michelle**: Visuals, clean, organize the presentation

**All**: Data Munge

**Felipe/ Reid**: Presenters

Break out into groups

### Timeline
* **Tuesday 9/22
    *[x]Discuss Your Topic and Sources
    *[x]Meet with Ed to get approval
* **Thursday 9/24
    * Finalize Data Sources
    * Attempt to clean Data
    * Discuss Issues 
    * Create Issues in Github
    * [x]Assign Roles
    
* **Saturday 9/26
    * IceBreaker
    * Realigh on question and mission
    * Each Individual create their data set
    	*Issue will be created
    * Break Into Group
    * Identify method of visuals (Tableau, Plotly, Matplotlib)
    
* Tuesday 9/29
    * Ice Breaker
    * Begin first draft of Presentation | Outline Read Me
    * Finalize data
    * Identify any missing data
    
* Thursday 10/1
    * Consolidate visuals
    * Get Presentation Finalized
    * Practice
* Saturday 10/3
    ##  **Presentation Day!**

**Advice** 
Michaels Advice : Define more planning upfront, you can be constrained by Data. What we define now, we can pull the data if it is there, or how can we find it if it is not there. Bottle neck is waiting on Data

Ed + Michael Advice:

Thursday during class:
Assign pieces out to people
Milestones, when things get done
Techniques

# Project Plan - " Knowledge Share of Ideas"

1. Define Questions
	a. Of these variables which one has the largest effect on your ability to raise money out of state, Incumbency, Partisanship, State, Election Cycle (Specefic Year)
2. Define Source needed for each question
3. Define API Extraction
4. Define Possible Correlation between data APIS
5. Extract Data &  Data Frame Conversion
6. Define type of merge based on item 4
7. Define type of clean, index changes if neccassary
8. Define types of graph to reprent question at hand


Data Sets

API Retrival

**Data Cleaning**
- *Spend most time here
   * Prepare Data to be analyzed
   * Aggregate grouping by questions we are trying to answer
   * Define visuals for each incident
      * Bar Chart
      * Scatter Plot
      * Line Chart
   
Data Visualsion
   * Get aligned with group on possible linear regression
   * Start putting presentation together
   
Practice Presentation
  
Present
  
 In Conclusion:
 
 We have identified our question and hypothesis. We will find and consolidate data. 75% of our project is cleaning the data to get it ready for the visuals (Think Whisker-Plot HW). Ask our questions, identefy where we need the data from, which sets, 

* API Identification
* API Extraction
* Data Fram Conversion
* Data Cleaning
   * Understand each column in df
   * What subset do we really need?
   * Merge data sets
* For each Questions: Use steps in notebook, from the df, presenting how you went through / Anything particluar challenging
   *  Highlight interesting difficult Data cleaning
   * Why did we choose each subset
   * Thought Process
    - Michaels Advice : Define more planning upfront, you can be constrained by Data. What we define now, we can pull the data if it is there, or how can we find it if it is not there. Bottle neck is waiting on Data
    * Felipe and Carlos can ask questions that align with the orignal problem statement. 
    * What are our Correlations
      Representation for each catagory
      What kind of correlationa are we looking for
      Diff correlation are represented better by dif charts
      
  * Visuals
   * Preferred data visual tool
   



## QUESTION: 
Does any of these have an effect 
Of these variables which one has the largest effect on your ability to raise money out of state, Incumbency, Partisanship, State, Election Cycle (Specefic Year)

Create a similarity score for candidates (cosign similarity) - each person has at least two traits (age, median age of state) the dot product of the two angles of the vectors, 
	
Candidate profile -  

fec.api ($ received) + 
census api +  
google sentiments api +
(demographics):

As a Congressional candidate what indicates the probability of you being able to pull in money from out of state. Creating a Candidate Demographic*- what kind of candidate is more likely to get money from out of state. 

* Candidate Demographics (Incumbant/Challenger, Gender, Religion, Party, Age-Range, Rural, Education, Income, Race)

	Based on similar candidates who are the best fundraisers?

Ed + Michael Advice:

Thursday during class:
Assign pieces out to people
Milestones, when things get done
Techniques

Github workflow: 
master, Felipe and Karen merging branches
Branch name: 
Issue-Number-Description

Create Issue card for new features, and give a milestone, and assign. You can create another issue card for bugs 

Protect master branch so that folks can’t accidentally merge to master. Assign a person to manage pull requests and manage conflicts

Before you commit to github, convert your Jupiter Notebooks to copy and paste your files into python files. The difference comparison is hard to determine with Jupiter files. All kinds of stuff in the Notebook that you don’t need to commit. 

Jupiter Notebooks for development, Python for github. Gitignore your .ipynb 

FALLBACK IDEA
FEC spending idea
Facebook api
