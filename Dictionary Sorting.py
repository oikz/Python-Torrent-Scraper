torrentList = {
    "Torrent1": 40,
    "Torrent2": 2,
    "Torrent3": 1,
    "Torrent4": 3,
}

#for key in sorted(torrentList.keys()):
#    print("%s: %s" % (key, torrentList[key]))

for key, value in sorted(torrentList.items(), reverse=True, key=lambda item: item[1]):
    print("%s: %s" % (key, value))

