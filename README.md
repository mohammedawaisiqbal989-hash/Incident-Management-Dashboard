# Incident Dashboard System

One of my first more invovled projects on python. I made a data dashboard system that can track and analyze incident reports. It uses SQLite for the database and can import data from CSV files. i learned quite a lot building this project espeically around sql and how that works. I did have quite a bit of inspiration from a few other similar Github projects such as https://github.com/tandem-tech/Incident-Management-Dashboard/tree/main and a few toutorials espeically on.

## What does the project do
The Incident Dashboard System lets you:

Import incident data from CSV files

Store the data in a SQLite database

View summary statistics (total, open, closed incidents)

See incidents broken down by category

Search for specific incidents

Filter incidents by date range

Generate charts with matplotlib to visualize the data

## what I used
Python 3

SQLite

pandas 

matplotlib 


## How to install
1. Have python installed
2. Install required packaged such as metplotlib and pandas by running
pip install pandas metplotlib
3. download project
4. run the python main.py file

## How to use

1. Run `python main.py`
2. You'll see menu with a few options
3. First, choose option 1 to import the CSV data
4. Then you can go through the data with the other options such as:
   
   View summary statistics
   ,See incidents by category
   ,View open incidents
   ,Search for incidents
   ,Filter by date and
   generate charts.

## Sample data

I included a sample CSV file with 25 incident records covering different categories like Network, Hardware, Software, and Security issues. Data dosent span a long time but can be easily changed

## What I learnt making this

Making this project taught me:

How to use SQLite
,How to write SQL queries
,How to use pandas
,How to make charts with matplotlib
,How to structure a Python project with multiple files amd
How to handle errors (mostly with try/except).


## Future improvements

I want to try to add:

A proper GUI instead of the text menu

Better error messages




