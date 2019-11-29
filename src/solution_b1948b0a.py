"""
Name: Mohamed Talaat
ID:19240057
"""

import json
import numpy as np
import sys
import json



def solve(input_json):
    with open(input_json) as f:
        data = json.load(f)
    for key, value in data.items():
        test = list(data.get('test'))
        testList = list(map(lambda d: d['input'], test))
        train = list(data.get('train'))
        trainList = list(map(lambda d: d['input'], train))
        combined = testList + trainList
    for a, b in enumerate(combined):
        for c, d in enumerate(b):
            for e, f in enumerate(d):
                if f == 6:
                    d[e] = 2
    output = json.dumps(combined)
    return output
printable_output = solve(sys.argv[1])
print(printable_output)
