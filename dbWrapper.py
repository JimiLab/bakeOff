__author__ = 'lukez'

import MySQLdb

class db:
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost', user='lukezim5', passwd='zim865', db='oldmegs')
        self.cur = self.connection.cursor()

    def fetchArtistIDs(self, count):
        self.cur.execute("""SELECT id FROM artist ORDER BY lastListenerCount DESC LIMIT %s""", (count,))
        res = self.cur.fetchall()
        output = list()
        for tuple in res:
            output.append(tuple[0])
        return output

    def fetchTrackIDs(self, artistIds):
        trackIDs = list()
        for id in artistIds:
             self.cur.execute("""SELECT enTrackID FROM track INNER JOIN tracktoartist ON track.id=tracktoartist.trackID where artistID=%s""", (id,))
             ids = self.cur.fetchall()
             if len(ids) > 1:
                for en in ids:
                    trackIDs.append(en[0])
             else:
                 trackIDs.append(ids[0])
        return trackIDs
