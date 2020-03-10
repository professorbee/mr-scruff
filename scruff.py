import os

test = "0.00 TRIO MOCOTO 'NAO ADIANTA'"

def getTime(x):
    split1 = x.split(" ",1)[0].rstrip()
    timelist = split1.split(".")
    hours = timelist[0]
    minutes = timelist[1]
    timeElapsed = ((int(hours) * 60) + int(minutes)) * 60
    return timeElapsed

def getArtist(x):
    intermediate = x.split(" ",1)
    artistStep = intermediate[1]
    artist = artistStep.split("'",1)[0].rstrip()
    return artist.lower()

def getSong(x):
    intermediate = x.split(" ",1)
    songStep = intermediate[1]
    song = songStep.split("'", 1)[1].rstrip()[:-1]
    return song.lower()

f = open("setlist.txt", "r")

setlist = f.readlines()

assemblyLine = []

assembledList = []

for i in setlist:
    assemblyLine = [getTime(i), getArtist(i), getSong(i)]
    assembledList.append(assemblyLine)

for i in range(0, len(assembledList)):
    artist = assembledList[i][1]
    song = assembledList[i][2]
    startTime = assembledList[i][0]
    if i == (len(assembledList) - 1):
        endingTime = 19643
    else:
        endingTime = assembledList[i + 1][0]
    os.system("ffmpeg -i Mr-Scruff-DJ-Mix-from-London-Koko-Saturday-16th-february-2013-79847030.mp3 -ss " 
            + str(startTime) + " -to " + str(endingTime) + " -c copy '" + artist + "-" + song + ".mp3'")

