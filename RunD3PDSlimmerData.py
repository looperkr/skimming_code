#! /afs/cern.ch/atlas/software/releases/17.2.8/sw/lcg/external/Python/2.6.5/i686-slc5-gcc43-opt/bin/python

# the with statement *should* be available in python 2.6, but we will import
# compatibility module just in case (MUST BE FIRST LINE EXECUTED IN FILE)
from __future__ import with_statement

import subprocess, sys
import os
from itertools import izip

# define Input Containers and name of output files

fPath = os.getcwd()
print fPath


def read_filenames_from_file(filename):
    """
    Open file and return list of non-blank lines. All lines are
    stripped of leading & trailing whitespace.
    """
    with open(filename, 'r') as file:
        return [name for name in map(str.strip, file) if name != '']


fString_in = read_filenames_from_file("data_in_redo.txt")
fString_out = read_filenames_from_file("data_out_redo.txt")


# define TopPhys Cache and date of production
# ns: new skim

fUser = "user.klooper.prun_slimmed_ns"
fTP   = "data12_8TeV"
fDate = "16.16.5_v0"
#fAth  = "17.3.10"
fCMT = "x86_64-slc5-gcc43-opt"
froot = "5.34/10"
fFile = "skim.root "
#fCPU  = ";"

fCPU  = ";--maxCpuCount=100000"
#fCPU  = ";--maxCpuCount=85000"
#fNin   = ";--maxNFilesPerJob=50"
#fDest  = ";--destSE=DESY-HH_LOCALGROUPDISK;"

# ANALY_CERN_XROOTD is always excluded because output files lying there can just be downloaded at CERN (inconvenient)

fExcluded = ";" #--excludedSite=ANALY_GOEGRID,ANALY_DESY-HH"
#fExcluded = ";--excludedSite=ANALY_TOKYO;"

#tmp="python slim_mc_1l_power.py %IN"

if len(fString_in) != len(fString_out):
    print >> sys.stderr, '\n\nNumber of input and output files is not equal! ---> EXIT.\n'
    sys.exit(1)

# format of the output file, filename will be added later in loop hence {{ }}
output_format = "{user}{{filename}}_{date}/".format(user=fUser, date=fDate)

# loop though the input and output filename pairs
#   run the command for each pair
for fInput, fOutput in izip(fString_in, fString_out):
    # fill in the filename formatting option
    fOutput = output_format.format(filename=fOutput)
    print fOutput
    # create command to be executed (';' separates args)
    cmd = ("prun;--inDS;{input};--outDS;{output};--exec;"
           "python slim_data_2l.py %IN;--nFilesPerJob=1;"
           "--cmtConfig={cmt_config};"
           "--rootVer={root}{excluded}{CPU};"
           "--outputs;{file}").format(input=fInput,
                                      output=fOutput,
                                      cmt_config=fCMT,
                                      root=froot,
                                      excluded=fExcluded,
                                      CPU=fCPU,
                                      file=fFile)
    print cmd.split(";")
    subprocess.call(cmd.split(";"), cwd=fPath)
