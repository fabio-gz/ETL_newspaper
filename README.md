# ETL_newspaper
This is a ETL process using Python with the objective of retrieve articles from newspaper websites,
initially is set to retrive form the Vanguardia website https://www.vanguardia.com/ and Antena2 website https://www.antena2.com/ the process have detail information in the console with the logging module

## Extraction
I Webscraped the website using Beautifulsoup and Requests modules and a yaml config file to store the configuration for scrapping

## Transform
In this step I cleaned the csv generated createing ids and cleaning missing data

## Load
The cleaned file was stored in a SQLlite db using sqlalchemy

Finally the pipeline file automate the ETL process in a single command

```Python pipeline.py [newspaper_name]```
