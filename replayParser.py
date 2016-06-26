import replayLoader as s2p
import sys

#reload(sys)
#sys.setdefaultencoding("utf-8")
sys.stdout = open('testinit.txt', 'w')

#data = s2p.load(['--gameevents', 'D:\NYU\Projects\Starcraft 2 Prediction\Replays\wcs-winter-2016\WCS\Championship\Final\Polt-Snute\Central Protocol (11).SC2Replay'])
data = s2p.load(['--initdata', 'D:\NYU\Projects\Starcraft 2 Prediction\Replays\wcs-winter-2016\WCS\Championship\Final\Polt-Snute\Central Protocol (11).SC2Replay'])

