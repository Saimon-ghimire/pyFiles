import json
import time

#name below..........
mainFile = open('timedtext.json')  # open JSON


srtfile = open("timedtext.srt", "w+")  # open SRT
fileW = mainFile.read()  # read JSON
stamps_dict = json.loads(fileW)  # JSON object
headerNumber = 0


def toStdTime(tseconds):
    std_time = time.strftime("%H:%M:%S", time.gmtime(int(tseconds/1000)))
    milisecond = int(tseconds-(int(tseconds/1000)*1000))

    #possibly not needed
    #if len(str(milisecond ==3)):
        #milisecond = int(str(milisecond)+"0")
        
    std_time = str(std_time)+", "+str(milisecond)
    return(std_time)


for terms in stamps_dict['events']:
    #write in SRT
    headerNumber += 1

    tstartms = int(terms['tStartMs'])
    tendms = tstartms+int(terms["dDurationMs"])
    Dialouge = terms['segs']

    # 'make the data' block
    startTime = toStdTime(tstartms)
    endTime = toStdTime(tendms)
    arrow = " --> "
    dialouge = Dialouge[0]['utf8']

    # write all in srt format
    srtfile.write(str(headerNumber)+"\n"+startTime +
                  arrow+endTime+"\n"+dialouge+"\n\n")
