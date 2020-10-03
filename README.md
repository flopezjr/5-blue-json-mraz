# Group: 1-blue-json-mraz Project 1

# Topic: Individual Campaign Fundraising

![dem_rep](Images/dem_rep.png)


## Team Members
* Felipe Lopez 
* Carlos Pires 
* Michelle Nguyen 
* Karen Kitchens 
* Reid Haynie  

## Background: Individual Campaign Fundraising for Senate Candidates 

Candidates running for federal office in the United States must report all donations, and money that their campaign receives to the FEC (Federal Election Committee). This information is on public record and made available by that agency. The FEC.gov website allows you to do an extraordinary amount of research and comparison. It is easy to look up who raised the most money in 2020 from Super Pacs or Individual donors. The FEC provides their public information in many forms throughout their website (in bulk downloads, in-browser tools), but they also have a robust API,the OpenFec https://api.open.fec.gov/developers/. Where people can draw out the exact data that they are interested in. 

We were mostly curious about in-state versus out-of-state campaign donations. Why would someone who can't vote for a person donate to that person's campaign? Why would a Senator who has difficult raising money in the state of his own constituents, yet major success from outsider contributions? Since that question is so broad and involves so many factors, we narrowed our question down to one easily answered question about the 2020 Senate race:

## Question 

What encourages a donor to donate to senate candidates from another state?
Does a challenger raise more money from out of state donors if they are a member of their states majority party or if they are a member of their states oppositions party? 

## Hypothesis

We think that having the best opportunity to gain a seat for either party will most encourage out-of-state of donations (so, Republican challengers in Republican states and Democratic Challengers in Democratic States).

If a candidate is a member their state's opposition party, they will likely raise less money in-state on average, and more from states with whom they share a party affiliation.

## Data Sources

* A `config.py` file will be required for the notebook to run. This contains the FEC API Key. We are pulling donations from individual donors.
* FEC API 
    * Candidate information: "https://api.open.fec.gov/v1/candidates/"
    * Finance Data: "https://api.open.fec.gov/v1/schedules/schedule_a/by_state/by_candidate/"
* FEC CSV 
    * `2012.csv` & `2016.csv`
    *FEC Presidential election data for map of blue states and red states 
    
* Tableau:  https://public.tableau.com/profile/michelle.nguyen4439#!/vizhome/Project1-FINAL/Sheet4?publish=yes


## Data Munging

OpenFec had many endpoints to choose from. Occasionally we had to switch out the endpoints because the data was not sufficient. We narrowed it down to an endpoint that gave us a table of 2020 senate candidates with one row per candidate including their party, state, and incumbency status. 

Example of Data from candidate endpoint: 

Candidate Name | Candidate ID | Party | State | Incumbency Status
Mitch McConnell, XXXXX, Republican, KY, incumbent
Mark Kelly, OOOOO, Democrat, AZ, challenger

Next we used a financial endpoint to get the total amount raised by state for every candidate as of September 1, 2020. The data was structured as one row per state donation for a particular candidate.

Example of Data from financials endpoint: 

Candidate ID | State Donation Originated From | Amount Donated
XXXXX, TX, $1,000,000
XXXXX, AZ, $1,000,000
XXXXX, WA, $1,000,000
OOOOO, TX, $1,000,000
OOOOO, AZ, $1,000,000
OOOOO, WA, $1,000,000

We were able to join the data on the Candidate ID, and include the separate amounts donated per state. Then we added all of the out-of-state donations per Candidate so that our data was structured as:

Candidate Name | Candidate ID | Party | State | Incumbency Status | Total Raised Out of State
Mitch McConnell, XXXXX, Republican, KY, incumbent, $3,000,000
Mark Kelly, OOOOO, Democrat, AZ, challenger, $3,000,000

Next, we needed to determine whether a state was affiliated with Democrats or Republican so that we could associate it to the candidate. We gathered this data from the past two presidential results and concluded that if a state voted for a Democrat both times, then a state was a Democratic state, and if a state voted for a Republican both times is was a Republican state. If it was switched back and forth, then it was a Non-affiliated state.

The final data was structured this way:

Candidate Name | Candidate ID | Party | State | Incumbency Status | Total Raised Out of State | State Status
Mitch McConnell, XXXXX, Republican, KY, incumbent, $3,000,000, Republican
Mark Kelly, OOOOO, Democrat, AZ, challenger, $3,000,000, Republican

We considered only Republican or Democratic Senate candidates that were going into the general election.

## Definitions

* Red state = Voted Republican last two presidential elections
* Blue state = Voted Democrat last two presidential elections
* Member of the opposition = Your party doesn’t align with the color of your state 
* Member of the majority = Your party aligns with the color of your state
* Individual Donors = non group funds

## Findings

Democratic Challengers regardless of their state's majority raised the best among Democrats and Republican incumbents in Republican majority states did the best among Republicans.

Figure 1:

![fig1](Images/Fig1.png)

Figure 2:

![fig2](Images/Fig2.png)

Figure 3:

![fig3](Images/Fig3.png)


## Conclusion

Democrats clearly have a strategy to go on the offense while Republicans are clearly trying to maintain the seats that they have.

## Future Research

We consider that this could be determined by who holds a majority in the senate. It would be interesting to analyze current House races to see if this would be inverted, considering Democrats hold a majority there. It would also be helpful to look at past Senate elections to see if our conclusions hold true.
