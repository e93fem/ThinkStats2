"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = ReadFemPreg()

    print(df["pregnum"].value_counts().sort_index())

    assert(len(df) == 7643)
    assert(df.pregnum.value_counts()[1] == 1267)

    print('%s: All tests passed.' % script)


def ReadFemPreg(dct_file='2002FemResp.dct',dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

if __name__ == '__main__':
    main(*sys.argv)
