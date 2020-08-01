import os
import sys
import json
import argparse

import numpy as np
import pandas as pd

from ligo.lw import utils as ligolw_utils
from ligo.lw.lsctables import SimInspiralTable
from ligo.lw.lsctables import SnglInspiralTable
from ligo.skymap.io.events.ligolw import ContentHandler


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inj", action="store",
                    help="Name of the injection xml file")
parser.add_argument("-C", "--coinc", action="store",
                    help="Name of the injection xml file")
parser.add_argument('-c','--cols', nargs='+',
                    help='columns of parameters to be read', required=True)
args = parser.parse_args()

if args.inj:
    file_obj = open(args.inj, 'rb')
elif args.coinc:
    file_obj = open(args.coinc, 'rb')
else:
    print('Must supply either injection xml file or coinc xml file')
    sys.exit(0)


xmldoc = ligolw_utils.load_fileobj(file_obj, contenthandler=ContentHandler)
if args.inj:
    inspiral_table = SimInspiralTable.get_table(xmldoc)
else:
    inspiral_table = SnglInspiralTable.get_table(xmldoc)


df = pd.DataFrame()
json_dict = {}
for column in args.cols:
    values = inspiral_table.get_column(column)
    df[column] = values
    json_dict[column] = values.tolist()
df.index += 1

print(df)
jsonfilename = args.inj.split(".")[0] + ".json"
with open(jsonfilename, 'w') as f:
    json.dump(json_dict, f, indent=2, sort_keys=True)


