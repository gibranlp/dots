#!/usr/bin/bash
# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
#
#
shopt -s nullglob
jpg_files=(*.jpg)

if [ ${#jpg_files[@]} -eq 0 ]; then
    echo "No .jpg Wallpapers found, ending script"
    exit 1
fi

for image in "${jpg_files[@]}" ;
do
    magick "$image" "${image%.*}.png" ;
done

rm -rf *.jpg
echo "All .jpg Wallpapers converted to .png"