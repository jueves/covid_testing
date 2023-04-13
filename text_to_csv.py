import pandas as pd
import androidhelper

droid = androidhelper.Android()

# Get the text from the shared data
shared_data = droid.getIntent().result[u'extras'][u'android.intent.extra.TEXT']

# Do something with the data
print(shared_data)

names_list = []
surnames_list = []
birthdate_list = []
testID_list = []

with open("data.txt") as f:
    for line in f:
        if (line[:12] == "First Name: "):
            names_list.append(line[12:].strip())
        elif (line[:11] == "Last Name: "):
            surnames_list.append(line[11:].strip())
        elif (line[:15] == "Date Of Birth: "):
            birthdate_list.append(line[15:].strip())
        elif (line[:19] == "Sample Identifier: "):
            testID_list.append(line[19:].strip())

data = pd.DataFrame({"name":names_list, "surname":surnames_list,
                     "birthdate":birthdate_list, "testID":testID_list})

data.to_csv("data.csv")