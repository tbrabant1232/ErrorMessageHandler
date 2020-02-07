from csv import DictReader, DictWriter
from datetime import date

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
    mydict = dict(reader2)

    writer = DictWriter(fout, fieldnames=reader2.fieldnames)
    writer.writeheader()

    for line1 in reader1:
        fin2.seek(0) # resets the reader2 iterator
        outline = dict(mydict)
        outline['Error Message'] = line1['Error']
        outline['Error Code'] = 'MC'
        for line2 in reader2:
            if line2['Error Message'] in line1['Error']:
                outline['Error Code'] = line2['Error Code']
                break
                writer.writerow(outline)
                break
        writer.writerow(outline)


