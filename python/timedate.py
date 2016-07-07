import datetime
import uuid

if __name__ == '__main__':
    timeStamp = 1464317644
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)

    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    print otherStyleTime
    key = str(uuid.uuid1())
    print str(uuid.uuid1()).upper()
