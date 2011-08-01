# Based on:
# http://www.blackberryforums.com/linux-users-corner/240979-script-copy-sync-playlists-music-blackberry.html 

#TODO: Clean this shit up.
import os
import shutil

def ensureDir(f):
    if not os.path.exists(f):
        os.makedirs(f)

inputPlaylist = raw_input('Enter Name of Playlist: ')
inputPlaylist += '.m3u'

target_dir = raw_input('Enter target directory, must end in a slash: ')
target_dir = os.path.expanduser(target_dir)
ensureDir(target_dir)

readPlay = open(inputPlaylist, 'r')  
for line in readPlay:
    line = line.strip()
    if (line[0] == '#'):
        pass
    else:
        line = line.replace('"','\"')
        line = line.replace("'","\'")
        filename = os.path.basename(line)
        if (not os.path.isfile(''.join([target_dir, filename]))):
            full_filename = target_dir + filename
            shutil.copyfile(line, full_filename)
        else:
            pass #Don't copy duplicates.
readPlay.close()
