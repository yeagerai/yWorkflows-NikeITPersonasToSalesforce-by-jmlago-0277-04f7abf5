
# ScrapeNikeITPersonas

Scrapes the web for Nike IT employees, collecting their names and emails if available. This component inputs nothing, and outputs the 'employees_data' as a list of dictionaries with keys 'name' and 'email'.

## Initial generation prompt
description: Scrapes the web for Nike IT employees, collecting their names and emails
  if available. This component inputs nothing, and outputs the 'employees_data' as
  a list of dictionaries with keys 'name' and 'email'.
name: ScrapeNikeITPersonas


## Transformer breakdown
- Initialize an empty list to store the employee data
- Perform web scraping to collect information about Nike IT employees
- Loop through the collected information
- For each employee, extract their name and email (if available)
- Create a dictionary with keys 'name' and 'email' for each employee
- Append the dictionary to the employees_data list

## Parameters
[]

        