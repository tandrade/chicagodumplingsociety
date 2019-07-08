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
    headers = next(reader)
    position_map = {index: {"name": key, "traits": {}} for (index, key) in enumerate(headers) if key}

    for row in reader:
        property_name = row[0]
        for index, value in enumerate(row[1:]):
            position_map[index + 1]["traits"][property_name] = bool(value)

    # this is what we want to write!
    final = {"candidates": [v for k, v in position_map.items()]}
