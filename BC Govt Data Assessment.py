#!/usr/bin/env python
# coding: utf-8

# Raw Data
# https://drive.google.com/file/d/1669IOH10XDepp1U54pqiog8aTGMq9PwW/view?usp=sharing https://drive.google.com/file/d/1ISQkmtetNZkdZUQMC738zu5uzDbwLN8_/view?usp=share_link
# 

# In[ ]:


import pandas as pd

Mar2024 = pd.read_csv("/Users/richardshaw/Documents/BC_sales_report/Mar2024.csv")
Feb2024 = pd.read_csv("/Users/richardshaw/Documents/BC_sales_report/Feb2024.csv")
Jan2024 = pd.read_csv("/Users/richardshaw/Documents/BC_sales_report/Jan2024.csv")
Dec2023 = pd.read_csv("/Users/richardshaw/Documents/BC_sales_report/Dec2023.csv")
Nov2023 = pd.read_csv("/Users/richardshaw/Documents/BC_sales_report/Nov2023.csv")
Oct2023 = pd.read_csv("/Users/richardshaw/Documents/BC_sales_report/Oct2023.csv")


HS_Mar2024 = pd.read_csv("/Users/richardshaw/Documents/BC_HouseSigma/BC 2023-09-01 to 2024-03_31.csv")
HS_Feb2024 = pd.read_csv("/Users/richardshaw/Documents/BC_HouseSigma/BC 2023-08-01 to 2024-02-29.csv")
HS_Jan2024 = pd.read_csv("/Users/richardshaw/Documents/BC_HouseSigma/BC 2023-07-01 to 2024-01-31.csv")
HS_Dec2023 = pd.read_csv("/Users/richardshaw/Documents/BC_HouseSigma/BC 2023-06-01 to 2023-12-31.csv")
HS_Nov2023 = pd.read_csv("/Users/richardshaw/Documents/BC_HouseSigma/BC 2023-05-01 to 2023-11-30.csv")
HS_Oct2023 = pd.read_csv("/Users/richardshaw/Documents/BC_HouseSigma/BC 2023-04-01 to 2023-10-31.csv")

HS_Mar2024['addr'] = HS_Mar2024['addr'].str.upper()
HS_Feb2024['addr'] = HS_Feb2024['addr'].str.upper()
HS_Jan2024['addr'] = HS_Jan2024['addr'].str.upper()
HS_Dec2023['addr'] = HS_Dec2023['addr'].str.upper()
HS_Nov2023['addr'] = HS_Nov2023['addr'].str.upper()
HS_Oct2023['addr'] = HS_Oct2023['addr'].str.upper()


import string

# Create a lookup table with full street types and their abbreviations
lookup_table = {
    "ABBEY": "ABBEY", "ACRES": "ACRES", "ALLEY": "ALLEY", "AVENUE": "AVE", "BAY": "BAY", "BEACH": "BEACH", "BEND": "BEND", "BOULEVARD": "BLVD", 
    "CAMPUS": "CAMPUS", "CAPE": "CAPE", "CENTRE": "CTR", "CHASE": "CHASE", "CIRCLE": "CIR", "CIRCUIT": "CIRCT", "CLOSE": "CLOSE", "COMMON": "COMMON",
    "CONCESSION": "CONC", "CORNERS": "CRNRS", "COURT": "CRT", "COVE": "COVE", "CRESCENT": "CRES", "CROSSING": "CROSS", "CUL-DE-SAC": "CDS",
    "DALE": "DALE", "DELL": "DELL", "DIVERSION": "DIVERS", "DOWNS": "DOWNS", "DRIVE": "DR", "END": "END", "ESPLANADE": "ESPL", "ESTATES": "ESTATE",
    "EXPRESSWAY": "EXPY", "EXTENSION": "EXTEN", "FARM": "FARM", "FIELD": "FIELD", "FOREST": "FOREST", "FREEWAY": "FWY", "FRONT": "FRONT",
    "GARDENS": "GDNS", "GATE": "GATE", "GLADE": "GLADE", "GLEN": "GLEN", "GREEN": "GREEN", "GROUNDS": "GRNDS", "GROVE": "GROVE", "HARBOUR": "HARBR",
    "HEATH": "HEATH", "HEIGHTS": "HTS", "HIGHLANDS": "HGHLDS", "HIGHWAY": "HWY", "HILL": "HILL", "HOLLOW": "HOLLOW", "INLET": "INLET", "ISLAND": "ISLAND",
    "KEY": "KEY", "KNOLL": "KNOLL", "LANDING": "LANDNG", "LANE": "LANE", "LIMITS": "LMTS", "LINE": "LINE", "LINK": "LINK", "LOOKOUT": "LKOUT",
    "LOOP": "LOOP", "MALL": "MALL", "MANOR": "MANOR", "MAZE": "MAZE", "MEADOW": "MEADOW", "MEWS": "MEWS", "MOOR": "MOOR", "MOUNT": "MOUNT", "MOUNTAIN": "MTN",
    "ORCHARD": "ORCH", "PARADE": "PARADE", "PARK": "PK", "PARKWAY": "PKY", "PASSAGE": "PASS", "PATH": "PATH", "PATHWAY": "PTWAY",
    "PINES": "PINES", "PLACE": "PL", "PLATEAU": "PLAT", "PLAZA": "PLAZA", "POINT": "PT", "PORT": "PORT", "PRIVATE": "PVT", "PROMENADE": "PROM",
    "QUAY": "QUAY", "RAMP": "RAMP", "RANGE": "RG", "RIDGE": "RIDGE", "RISE": "RISE", "ROAD": "RD", "ROUTE": "RTE", "ROW": "ROW", "RUN": "RUN",
    "SQUARE": "SQ", "STREET": "ST", "SUBDIVISION": "SUBDIV", "TERRACE": "TERR", "THICKET": "THICK", "TOWERS": "TOWERS", "TOWNLINE": "TLINE",
    "TRAIL": "TRAIL", "TURNABOUT": "TRNABT", "VALE": "VALE", "VIA": "VIA", "VIEW": "VIEW", "VILLAGE": "VILLGE", "VILLAS": "VILLAS", "VISTA": "VISTA",
    "WALK": "WALK", "WAY": "WAY", "WHARF": "WHARF", "WOOD": "WOOD", "WYND": "WYND"
}

# Function to replace full street types with abbreviations
def replace_street_types(address):
    if isinstance(address, str):
        for full_street_type, abbreviation in lookup_table.items():
            address = address.replace(full_street_type, abbreviation)
    return address

# Apply the function to the "addr" column in HS_Mar2024 dataset
HS_Mar2024['addr'] = HS_Mar2024['addr'].apply(replace_street_types)
HS_Feb2024['addr'] = HS_Feb2024['addr'].apply(replace_street_types)
HS_Jan2024['addr'] = HS_Jan2024['addr'].apply(replace_street_types)
HS_Dec2023['addr'] = HS_Dec2023['addr'].apply(replace_street_types)
HS_Nov2023['addr'] = HS_Nov2023['addr'].apply(replace_street_types)
HS_Oct2023['addr'] = HS_Oct2023['addr'].apply(replace_street_types)


# Define a function to add apt_num in front of addr with a hyphen if apt_num is a pure number or contains no more than one alphabet character
def add_apt_num_to_addr(row):
    if pd.notnull(row['apt_num']):  # Check if apt_num is not null
        if row['apt_num'].isdigit() or sum(c.isalpha() for c in row['apt_num']) <= 1:  # Check if apt_num is a pure number or contains no more than one alphabet character
            apt_num_length = len(row['apt_num'])  # Get the length of apt_num
            if not row['addr'].startswith(row['apt_num']):  # Check if apt_num is not identical to the first x characters of addr
                return f"{row['apt_num']}-{row['addr']}"  # Concatenate apt_num and addr with a hyphen
    return row['addr']  # Return addr as it is if apt_num is null, doesn't meet the condition, or is identical to the first x characters of addr

# Apply the function to the DataFrame
HS_Mar2024['addr'] = HS_Mar2024.apply(add_apt_num_to_addr, axis=1)
HS_Feb2024['addr'] = HS_Feb2024.apply(add_apt_num_to_addr, axis=1)
HS_Jan2024['addr'] = HS_Jan2024.apply(add_apt_num_to_addr, axis=1)
HS_Dec2023['addr'] = HS_Dec2023.apply(add_apt_num_to_addr, axis=1)
HS_Nov2023['addr'] = HS_Nov2023.apply(add_apt_num_to_addr, axis=1)
HS_Oct2023['addr'] = HS_Oct2023.apply(add_apt_num_to_addr, axis=1)


# To remove duplicates based on the 'addr' column in HS_Feb2024 example,
HS_Mar2024 = HS_Mar2024.drop_duplicates(subset=['addr'])
HS_Feb2024 = HS_Feb2024.drop_duplicates(subset=['addr'])
HS_Jan2024 = HS_Jan2024.drop_duplicates(subset=['addr'])
HS_Dec2023 = HS_Dec2023.drop_duplicates(subset=['addr'])
HS_Nov2023 = HS_Nov2023.drop_duplicates(subset=['addr'])
HS_Oct2023 = HS_Oct2023.drop_duplicates(subset=['addr'])

# Select observations where status = 'sld'
HS_Mar2024 = HS_Mar2024[HS_Mar2024['status'] == 'Sld']
HS_Feb2024 = HS_Feb2024[HS_Feb2024['status'] == 'Sld']
HS_Jan2024 = HS_Jan2024[HS_Jan2024['status'] == 'Sld']
HS_Dec2023 = HS_Dec2023[HS_Dec2023['status'] == 'Sld']
HS_Nov2023 = HS_Nov2023[HS_Nov2023['status'] == 'Sld']
HS_Oct2023 = HS_Oct2023[HS_Oct2023['status'] == 'Sld']


Compare number of rows in BC govt data and our table "listing"  from October 2023 to March 2024:

# Perform inner join between on the 'addr' and 'Property_Address' columns
overlap_Mar2024 = HS_Mar2024.merge(Mar2024, how='inner', left_on='addr', right_on='Property_Address')
overlap_Feb2024 = HS_Feb2024.merge(Feb2024, how='inner', left_on='addr', right_on='Property_Address')
overlap_Jan2024 = HS_Jan2024.merge(Jan2024, how='inner', left_on='addr', right_on='Property_Address')
overlap_Dec2023 = HS_Dec2023.merge(Dec2023, how='inner', left_on='addr', right_on='Property_Address')
overlap_Nov2023 = HS_Nov2023.merge(Nov2023, how='inner', left_on='addr', right_on='Property_Address')
overlap_Oct2023 = HS_Oct2023.merge(Nov2023, how='inner', left_on='addr', right_on='Property_Address')

Counted matching rows for each months: 

row_count = overlap_Mar2024.shape[0]
print("Number of rows:", row_count)

row_count = overlap_Feb2024.shape[0]
print("Number of rows:", row_count)

row_count = overlap_Jan2024.shape[0]
print("Number of rows:", row_count)

row_count = overlap_Dec2023.shape[0]
print("Number of rows:", row_count)

row_count = overlap_Nov2023.shape[0]
print("Number of rows:", row_count)

row_count = overlap_Oct2023.shape[0]
print("Number of rows:", row_count)


# Number of Observations Marked as Sold by month:
# March 2024: 2067
# February 2024: 2567
# January 2024: 2784
# Dec 2023: 2313
# November 2023: 3405
# October 2023: 3487
# 
# 
# 
# Number of rows of BC govt data by month:
# 
# March 2024: 3978
# February 2024: 4486
# January 2024: 5275
# Dec 2023: 4917
# November 2023: 6216
# October 2023: 7306
# 
# 
# Preliminary conclusion:
# 
# On average, we have around 47-55% of the data in BC Govt Report every month. Considering there are some addresses of listings in our dataset that are wrongly or improperly formatted that cannot be corrected by coding, we actually have slightly more data than the estimate aforementioned. 

# Further investigation on our data coverage in selected municipalities: City of Vancouver', "City of Richmond", 'City of Surrey', "City of Richmond", 'City of Nanaimo', 'City of Chilliwack', 'District of Kitimat', "City of Prince Rupert", "Quesnel Rural", "Nanaimo Rural", "Duncan Rural"

# In[ ]:


# Define the list of cities you want to count
cities_of_interest = ['City of Vancouver', "City of Richmond", 'City of Surrey', "City of Richmond",
                      'City of Nanaimo', 'City of Chilliwack', 'District of Kitimat', "City of Prince Rupert",
                      "Quesnel Rural", "Nanaimo Rural", "Duncan Rural"]

# Initialize dictionaries to store the counts for each city
overlap_counts = {}
mar_counts = {}

# Count rows for each city in overlap_Mar2024
for city in cities_of_interest:
    overlap_counts[city] = overlap_Mar2024.loc[overlap_Mar2024['Jur_Description'] == city].shape[0]

# Count rows for each city in Mar2024
for city in cities_of_interest:
    mar_counts[city] = Mar2024.loc[Mar2024['Jur_Description'] == city].shape[0]

# Print the row counts for overlap_Mar2024
print("Overlap_Mar2024 Counts:")
for city, count in overlap_counts.items():
    print(f"{city}: {count}")

# Print the row counts for Mar2024
print("\nMar2024 Counts:")
for city, count in mar_counts.items():
    print(f"{city}: {count}")


# Number of observations that exist in both BC govt data and HousSigma data Mar2024:
# City of Vancouver: 320
# City of Richmond: 131
# City of Surrey: 272
# City of Nanaimo: 46
# City of Chilliwack: 83
# District of Kitimat: 0
# City of Prince Rupert: 0
# Quesnel Rural: 0
# Nanaimo Rural: 10
# Duncan Rural: 12
# 
# BC Govt Mar2024 Counts:
# City of Vancouver: 453
# City of Richmond: 174
# City of Surrey: 363
# City of Nanaimo: 77
# City of Chilliwack: 110
# District of Kitimat: 10
# City of Prince Rupert: 12
# Quesnel Rural: 13
# Nanaimo Rural: 17
# Duncan Rural: 18
# 
# Based on the sample we selected, we can infer that our data coverage is better in Metro Vancouver and BC lower mainland than in more rural area. Our data coverage rate in BC lower mainland is around 65%, slightly better than average, but we only have less than half of the data that BC govt has in some more rural areas, we even have nothing in District of Kitimat, City of Prince Rupert, Quesnel Rural. So BC govt data is of certain value in all regions, and it is very important if we want to improve our service for more rural part of BC.

# In[ ]:


# Set display options to show all rows and columns (optional)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Filter both dataframes where Jur_Description is 'City of Vancouver'
overlap_Mar2024_vancouver = overlap_Mar2024[overlap_Mar2024['Jur_Description'] == 'City of Vancouver']
Mar2024_vancouver = Mar2024[Mar2024['Jur_Description'] == 'City of Vancouver']


# Find rows in Mar2024_vancouver that are not in overlap_Mar2024_vancouver
unmatched_in_Mar2024 = Mar2024_vancouver[~Mar2024_vancouver['Property_Address'].isin(overlap_Mar2024_vancouver['Property_Address'])]

# Display the unmatched rows
print(unmatched_in_Mar2024)

# Save the unmatched rows to a CSV file
unmatched_in_Mar2024.to_csv('unmatched_rows_vancouver.csv', index=False)


# Manually checked 20 out of 134 observations that are only found in BC govt data：
# Out of 20 unmatched observations, we found that we actually have 7 of them on HouseSigma, which are possibly due to incorrect format of address in our data. Of the remaining 13 properties, 8 of them are likely private sale. 

# Used following code to find addresses only exist in HS data, not BC govt data. 78 addresses of all listing on HS marked as sold are not found in BC govt data. Manually checked 10 of them. 

# In[ ]:


Oct2023Mar2024 = pd.concat([Mar2024, Feb2024, Jan2024, Dec2023, Nov2023, Oct2023], ignore_index=True)


# Filter HS_Oct2023_Only by municipality 'Vancouver'
HS_Oct2023_Van = HS_Oct2023_Only[HS_Oct2023_Only['municipality'] == 'Vancouver']

# Filter Oct2023Mar2024 by Jur_Description 'City of Vancouver'
Oct2023Mar2024_Van = Oct2023Mar2024[Oct2023Mar2024['Jur_Description'] == 'City of Vancouver']

# Find rows in HS_Oct2023_Van that are not in Oct2023Mar2024_Van
Unique_HS_Oct2023 = pd.merge(HS_Oct2023_Van, Oct2023Mar2024_Van, left_on='addr', right_on='Property_Address', how='left', indicator=True)                     .query('_merge == "left_only"')                     .drop(columns=['_merge', 'Jur_Description', 'Property_Address'])

# Display the rows unique to HS_Oct2023_Van
print(Unique_HS_Oct2023)

# Optional: Save the unique rows to a new CSV file
Unique_HS_Oct2023.to_csv("/Users/richardshaw/Documents/Unique_to_HS_Oct2023.csv", index=False)


# 4 of them actually exist on BC Assessment, one of them is typo, 5 of them indeed don't exist on BC Assessment. 
