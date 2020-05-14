#!/usr/bin/env python3

#  dirs and files
BaseDir = '/Users/whawley/Research/github/Download-Seismic-Data/'
ConfigDir = BaseDir+'config/' # where we keep setup files
DataDir = BaseDir+'data/'  # where the data will be saved
EventsDataDir = DataDir+'SAC_Events/' # event sac files - saved by EVENT/[dataFile]
NoiseDataDir = DataDir+'SAC_Noise/' # noise sac files - saved by NW_STNM/[datafile]
EventsFileName = ConfigDir+'EventFile.txt' # expected format 'YYYYMMDDHHMM/n'
DayFileName = ConfigDir+'NoiseFile.txt' # format same as above
Stafn = ConfigDir+'X9_stations.txt'  # station names separated by newline

#  Event download
minMag = 6.5
webservice = "IRIS"
network = "X9"  # X9 = Blanco
isCMT_params = 1  # use GCMT parameters for SAC header; 0 = use IRIS
isCentroid = 1  # if isCMT_params = 1, use centroid; 0 = epicentral

#  Noise Download
trLen = 60 * 60 * 24  # seconds 
#  If using noise to correct OBS:
noDays = 4  # number of days prior to event to use
isCalDay = 1  # 0 to start each day at 00:00; 0 to use 24h segments prior to eq
# If downloading noise by day:


tstart = '2012-09-18T00:00:00'
tend = '2013-10-06T23:00:00'

# Stations to download
# need one for low-pass filtered stations
inFile = open(XStafn)
XStaList = []
for line in inFile:
    XStaList.append(line.rstrip('\n'))
XChanList = ['LHZ', 'LH1', 'LH2', 'BXH']

# and for all stations...
inFile = open(Stafn)
StaList = []
for line in inFile:
    StaList.append(line.rstrip('\n'))
ChanList = ['LHZ', 'LH1', 'LH2', 'BDH']

# Event trace info
isDownsamp = 1  # downsample option
isRemoveResp = 1  # remove response option
srNew = 1  # new sample rate, samples/sec
trLen = 6000  # len of traces (sec)

# Frequency Limits for Response Removal
# Hi corner deternimed by Nyquist
# Lo corner defined by
LoFreq1 = 0.001
LoFreq2 = 0.005