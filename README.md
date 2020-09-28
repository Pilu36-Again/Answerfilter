# Answerfilter
This script is a solution to search for strings among all responses after a questionnaire is filled/closed and the DB (a .csv file) is available. There is a simple, however yet not solved task: define those respondents who mentioned a specific string anywhere among their answers. So filter for these respondents and make a list about these. 

Responses are checked when we meet the next challenge: 
- who's answer includes a specific string 
- strings to filter for can be a closed or opened quesion also
- there could be commas within the answer itself and the DB is structured as Comma Separated file. 
- it works for .txt and for .csv file also.

Preparation for the DB: 
- names (or other identifiers) should be in the last column
- the input DB should be in the same folder where this .py script is run
- the spript can run on Ubuntu like this: $ python Respfilter_multiple_str_write.py

Results can be seen: 
- on the Terminal itself
- saved in a .txt file, with the following name as reference: month-day-hour-minutes-seconds
