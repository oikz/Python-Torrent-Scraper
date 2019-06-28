torrentList = {
    "Torrent1": "40/10",
    "Torrent2": "2/15",
    "Torrent3": "1/20",
    "Torrent4": "3/50",
}

#for key in sorted(torrentList.keys()):
#    print("%s: %s" % (key, torrentList[key]))

for key, value in sorted(torrentList.items(), reverse=True, key=lambda item: item[1]):
    print("%s: %s" % (key, value))

