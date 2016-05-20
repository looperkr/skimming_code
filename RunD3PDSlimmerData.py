#! /afs/cern.ch/atlas/software/releases/17.2.8/sw/lcg/external/Python/2.6.5/i686-slc5-gcc43-opt/bin/python

from __future__ import with_statement

import subprocess, sys
import os, string

# define Input Containers and name of output files

fPath = os.getcwd()
print fPath


def read_filenames_from_file(filename):
    """
    Open specified read lines. Return a list of all non-blank lines in
    file, stripped of leading/trailing whitespace.
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

fNLines_in  = len(fString_in)
fNLines_out = len(fString_out)

if fNLines_in != fNLines_out:
     print "\n"
     print 'Number of input and output files is not equal! ---> EXIT.'
     print "\n"
     sys.exit(1)

for i in range(0, fNLines_in):
     fString = fUser+fString_out[i]+"_"+fDate+"/"
     fOutput = fString.replace("\n", "")
     fInput  = fString_in[i].replace("\n", "")
     print fOutput
     cmd = []
     cmd = ("prun;--inDS;" + fInput + ";--outDS;" + fOutput + ";--exec;" + "python slim_data_2l.py %IN" + ";--nFilesPerJob=1;" + ";--cmtConfig=" + fCMT + ";--rootVer=" + froot + fExcluded +fCPU +  ";--outputs;" + fFile)
     print cmd.split(";")
     subprocess.call(cmd.split(";"), cwd=fPath)
