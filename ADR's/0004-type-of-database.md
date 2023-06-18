#fin_cander
Date: '2023-06-09'
##Status
To be proposed
##Context
Data delivered by user throught our site needs to be stored.
Thanks to that we will be able to save the data and user will have access to it.

Buisness requirements:
> 1. Simply and fast,
> 2. Needs to handle multiple queries at one time (we are counting on a large number of users),
> 3. Needs to work on virtual server,
> 4. Potential for additional extensions in case of future application development

##Decision
We shuld use PostgreSQL database instead of built in SQLite3.
Main reason of the decision is better management of multiple queries within a single process.


## Consequences 


## Keywords
- PostgreSQL,
- SQLite3,
- database,
- db,