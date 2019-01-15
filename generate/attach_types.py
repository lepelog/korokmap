import csv
import json

# load files
with open('allkoroks.json') as jsf:
    rawallkoroks = json.load(jsf)

with open('rawtypes.csv') as csvf:
    rawtypes = list(csv.reader(csvf))

# Get all types from rawtypes second column, set to distinct then sort and to list, disregard title

# map one csv row to dict member
def rawtypetodict(rawtype):
    tid = "{:0>3}".format(rawtype[0])
    # in case it's a rock korok differentiate
    if (rawtype[1] == 'Lift the Rock' and rawtype[2] != ''):
        # the comment is always 'Under' something
        rawtype[1] = rawtype[1] + ' (' + rawtype[2][6:] + ')'
        rawtype[2] = ''
    return (tid, rawtype)

dicttypes = dict(rawtypetodict(x) for x in rawtypes[1:])
allkoroks = [{'type':dicttypes[x['id'][4:]][1], 'comment':dicttypes[x['id'][4:]][2], **x} for x in rawallkoroks]
allkoroktypes = list(sorted(set(x['type'] for x in allkoroks)))
with open('allkoroks.js', 'w') as resf:
    resf.write('const allkoroktypes = ')
    json.dump(allkoroktypes, resf)
    resf.write(';\nconst allkoroks = ')
    json.dump(allkoroks, resf)
    resf.write(';')

