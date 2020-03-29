# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import datetime


#variable declaration
Emp_ID = []
Name = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []
formatted_DOB = []
formatted_SSN = []
state_code = []

csvpath = os.path.join('employee_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader) 
    
    #create lists for csv data
    for row in csvreader:
        Emp_ID.append(row[0])
        Name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        State.append(row[4])

    #Split name into first name and last name
    First_Name = [x.split()[0] for x in Name]
    Last_Name = [x.split()[1] for x in Name]

    #format DOB
    for i in DOB:
        new_date=datetime.datetime.strptime(i, "%Y-%m-%d").strftime('%m/%d/%Y')
        formatted_DOB.append(new_date)

    #format SSN
    for i in SSN:
        new_SSN="***-**-"+i[-4:]
        formatted_SSN.append(new_SSN)

    #Create state dictionary
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
 
    #Find state codes in dictionary and append to new list
    for i in State:
        for j in us_state_abbrev:
            if i==j:
                state_code.append(us_state_abbrev[j])
    
# Zip lists together
cleaned_csv = zip(Emp_ID, First_Name, Last_Name, formatted_DOB, formatted_SSN, state_code)

# Set variable for output file
output_file = os.path.join("formatted_employee_data.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
