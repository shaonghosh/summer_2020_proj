import os
import sys
import json
import argparse

import numpy as np
import pandas as pd

from ligo.lw import utils as ligolw_utils
from ligo.lw.lsctables import SimInspiralTable
from ligo.skymap.io.events.ligolw import ContentHandler


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inj", action="store",
                    help="Name of the injection xml file")
parser.add_argument('-c','--cols', nargs='+',
                    help='columns of parameters to be read', required=True)
args = parser.parse_args()

inj_file_obj = open(args.inj, 'rb')

inj_xmldoc = ligolw_utils.load_fileobj(inj_file_obj, contenthandler=ContentHandler)
orig_sim_inspiral_table = SimInspiralTable.get_table(inj_xmldoc)

df = pd.DataFrame()
for column in args.cols:
    values = orig_sim_inspiral_table.get_column(column)
    df[column] = values
df.index += 1 

print(df)
