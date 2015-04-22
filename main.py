__author__ = 'luke.luke'

import dbWrapper
import os
import csv
import numpy

class driver:
    def __init__(self):
        self.db = dbWrapper.db()
        self.vectorPath = os.path.normpath('C:/Dev/bakeOff/bakeOff/ent12vq/')

    def generateSongByFeatureMatrix(self):
        artists = self.db.fetchArtistIDs(200)
        ids = self.db.fetchTrackIDs(artists)
        songByFeature = list()
        index = 0;
        self.songIndex = dict()
        for id in ids:
            if type(id) is tuple:
                id = id[0]
            vector = open(self.vectorPath + "\\" + str(id) + ".ent12-vq-full512-01.csv", 'r')
            reader = csv.reader(vector, dialect='excel')
            songByFeature.append(list())
            self.songIndex[str(id)] = index
            index+=1
            value = reader.next()
            while True:
                try:
                    songByFeature[self.songIndex[str(id)]].append(float(value[0]))
                    value = reader.next()
                except StopIteration as error:
                    break
        return songByFeature

    def dotProductSelf(self, matrix):
        result = numpy.inner(matrix, matrix)
        return result

    def makeArtistByArtist(self, songBySong):
        for id in self.songIndex:



driver = driver()
matrix = driver.generateSongByFeatureMatrix()
matrix = driver.dotProductSelf(matrix)
