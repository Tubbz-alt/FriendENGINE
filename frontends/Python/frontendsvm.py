import socket;
import sys;
import os;
from friendEngine import Engine;

engine = Engine();

# creating the main socket variable
engine.connectEngine();

# creating a session and getting sessionID
engine.createSession();
print("sessionID received = %s" % (engine.sessionID));

# reading the actual run number
if (len(sys.argv)>1):
   option = str(sys.argv[1]);
else:
   option = "1";

PIPELINE = int(option);
 
if (PIPELINE > 1):
   # changing the directory of the volumes
   engine.setVariable('Prefix', 'outputdirRUN0' + option + os.path.sep + 'DRIN-');   
   # changing the current suffix
   engine.setVariable('ModelRunSuffix', 'RUN01');   
   # changing the current suffix
   engine.setVariable('CurrentRunSuffix', 'RUN0' + option);   

   # not using all the subject mask
   engine.setVariable('UseWholeSubjectSpaceMask', '0');   
   
   # changing the threshold Type
   engine.setVariable('ByCutOff', '2');   

   # changing the p-value cut off
   engine.setVariable('pvalueCutOff', '0.005');   
   
# initiating processing
engine.startTheEngine(2, PIPELINE!=1);
