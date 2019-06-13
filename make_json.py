import csv

"""
Take in a CSV where the columns represent different dumpling candidates
and rows represent a given trait.

Output two JSON documents:
1) Traits matched to human readable names
2) A JSON document of the format:
  {
   candidates: [{
     "name": "Sample Name",
     "traits": {
        "boolean_trait": False,
        "numeric_trait": 1.0
     }
   }]
  }
"""

data_file = "dumplings.csv"

with open(data_file) as csvfile:
  reader = csv.reader(csvfile)

  headers = reader.next()
  # format the headers
  for row in reader:
    pass
  # read in the data
