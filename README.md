# Library Collections

Example Code Louisville data analysis project. Python analysis of library 
collection data.

## Demo Overview

The purpose of this demo is to show the data analysis process and concepts using 
Python. 

For this example project, we'll look at data about the Louisville Free Public 
Library. Louisville has a number of datasets published on their Open Data 
website with three datasets on the library topic.

At a high level, this demo will show:
1. How to **describe data** including the shape of the data, the types of data 
in the columns, and what the data in the columns looks like. The purpose of this 
step is to understand what cleaning will be needed and what questions can be 
answered.  
1. How to **clean a data set** including dealing with missing records and 
creating new columns based on existing ones.
1. How to **analyze a data set** by grouping and aggregating data. 
1. How to **visualize data** in tables and graphs. 

## Demo Setup

1. Fork the repo and clone your forked repo to your machine. Note that the data 
file used in this project is very large (~25MB).
1. Open GitBash in Windows or Terminal in Mac and navigate to the project folder.
1. Create a virutal environment, activate it, and install the packages listed in 
the `requirements.txt` file. 
1. Follow the instructions for each demo.
1. When you finish each demo, create a Pull Request back to the original repo 
to get feedback from the mentors.

### Project Layout

| File/Folder | Description |
| ----- | ----- |
| README.md |  project documentation |
| requirements.txt | list of required Python packages |
| data/raw/books.csv.gz | zipped csv file with library collection data |
| data/clean | folder for storing cleaned data |
| 01_load_authors.py | python program to scrape author data |
| 02_discover.ipynb | Jupyter notebook with data discovery code |
| 03_clean.py | python program to clean the data |
| 04_analyze.ipynb | Jupyter notebook with data analysis code |
| 05_visualize.ipynb | Jupyter notebook with data visualization code |

### Source Data

This project uses data from the Louisville Metro Open Data site. You can find 
the main info page for this data set here: 
[Library Collection Inventory](https://data.louisvilleky.gov/datasets/LOJIC::louisville-metro-ky-library-collection-inventory-/about).


This project also scrapes data about Young Adult book genre from wikipedia using
the beautiful soup library. The wikipedia article is here:
[title](url).

## Demo 1: Data Discovery

The first step in the data analysis process is to describe the data in the 
dataset. This will help you understand the source data and inform what data 
preparation will be needed and what questions you will be able to answer with 
this dataset.

### Instructions:

Document the folloiwng in the 01-discover.ipynb file:

1. Provide a link to the data source and a description of the data
1. Describe the shape of the data (# rows and # cols)
1. Define the columns / fields in the data using a data dictionary (a table 
containing the list of columns with the column name, data type, description, 
and cleaning notes).
1. Summarize the # of records for each distinct value in the categorical columns.
1. Summarize the descriptive statistics (min, max, mean, median, mode, 
std. dev.) for each numerical column. 
1. Document the cleaning needed including what to do with outlier records, what 
columns will not be needed, etc.
1. Document the questions you will be able to answer with the data.
1. Document any new columns that will need to be created based on calculations 
using existing columns.

### Notes:
- You can read more about Markdown, the language used in both README files and 
Jupyter notebooks here: 
- you can read more about web scraping here.