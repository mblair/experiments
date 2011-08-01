#!/usr/bin/env bash
#Originally found here: http://www.linuxquestions.org/questions/linux-software-2/howto-convert-flac-to-mp3-544109/

#TODO: Error handling and such.

for file in *.flac; do
#find . -type f -iname '*.flac' | sort | while read file; do
	ffmpeg -i "$file" -ab 192k "$file.mp3"
	new=$(echo "$file.mp3" | sed "s/.flac//g")
	mv "$file.mp3" "$new"
done

rm -rf *.flac
