import csv
import json

# load files
with open('allkoroks.json') as jsf:
    rawallkoroks = json.load(jsf)

with open('rawtypes.csv') as csvf:
    rawtypes = list(csv.reader(csvf))

# Get all types from rawtypes second column, set to distinct then sort and to list, disregard title
allkoroktypes = list(sorted(set(x[1] for x in rawtypes[1:])))

# map one csv row to dict member
def rawtypetodict(rawtype):
    tid = "{:0>3}".format(rawtype[0])
    return (tid, rawtype)

dicttypes = dict(rawtypetodict(x) for x in rawtypes[1:])
allkoroks = [{'type':dicttypes[x['id'][4:]][1], 'comment':dicttypes[x['id'][4:]][2], **x} for x in rawallkoroks]
with open('allkoroks.js', 'w') as resf:
    resf.write('const allkoroktypes = ')
    json.dump(allkoroktypes, resf)
    resf.write(';\nconst allkoroks = ')
    json.dump(allkoroks, resf)
    resf.write(';')

