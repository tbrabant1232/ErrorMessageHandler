from csv import DictReader, DictWriter
from datetime import date
import re

today = date.today()
# dateStr = today.strftime("%d-%b-%Y")
dateStr = today.isoformat()
csvfile = (dateStr + "raw.csv")
inputFile = csvfile
finalcsvfile = (dateStr + "processed.csv")


with open(inputFile) as fin1, \
        open('errorFile.csv') as fin2, \
        open(finalcsvfile, 'w') as fout:

    reader1 = DictReader(fin1)
    reader2 = DictReader(fin2)
    mydict = {"Error Message" : 1, "Code" : 2, "Mode" : 3, "Scenario": 4, "Line Number" : 5, "Error Summary" : 6}

    writer = DictWriter(fout, fieldnames=["Error Message", "Code", "Mode", "Scenario", "Line Number", "Error Summary"])
    writer.writeheader()

    for line1 in reader1:
        fin2.seek(0) # resets the reader2 iterator
        outline = dict(mydict)
        outline['Error Message'] = line1['Error']
        outline['Code'] = 'Master Consol'
        outline['Mode'] = re.search('file:src/feature/Robots/(.+?)/Functional', line1['Error']).group(1)
        outline['Scenario'] = re.search('/Functional/(.+?).feature', line1['Error']).group(1)
        outline['Error Summary'] = re.search('com.expd.test.transportation.glue.legacy.exceptions.(.+?)(at com.expd.test.transportation.glue.legacy|Message on screen was)', line1['Error']).group(1)
        outline['Line Number'] = re.search('Functional.feature:(.+?)\\)', line1['Error']).group(1)
        for line2 in reader2:
            if line2['Error Message'] in line1['Error']:
                outline['Code'] = line2['Error Code']
                break
                writer.writerow(outline)
                break
        writer.writerow(outline)


