import csv, json


with open('MOCK_DATA.json') as js_file:
    js_dicts = json.loads(''.join(js_file.readlines()))


with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(
        csvfile, delimiter='|', quotechar='*', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(list(js_dicts[0].keys()))
    for dct in js_dicts:
        spamwriter.writerow(list(dct.values()))
