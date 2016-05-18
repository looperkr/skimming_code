#! /afs/cern.ch/atlas/software/releases/17.2.8/sw/lcg/external/Python/2.6.5/i686-slc5-gcc43-opt/bin/python

import subprocess,sys
import os,string

# define Input Containers and name of output files

fPath = os.getcwd()
print fPath
fin   = open("mc_in_redo.txt",  'r')
fout  = open("mc_out_redo.txt", 'r')

# define TopPhys Cache and date of production

fUser = "user.klooper.prun_slimmed_"
fTP   = "mc12_8TeV"
fDate = "16.12.5_v2"
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

fExcluded = ";--excludedSite=ANALY_INFN-MILANO-ATLASC;"

#tmp="python slim_mc_1l_power.py %IN"

fString_in  = fin.readlines()
fString_out = fout.readlines()

fin.close()
fout.close()

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
     cmd = ("prun;--inDS;" + fInput + ";--outDS;" + fOutput + ";--exec;" + "python slim_mc_2l_160214.py %IN" + ";--nFilesPerJob=1;" + ";--cmtConfig=" + fCMT + ";--rootVer=" + froot + fExcluded +fCPU +  ";--outputs;" + fFile)
     print cmd.split(";")
     subprocess.call(cmd.split(";"), cwd=fPath)


