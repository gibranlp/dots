#!/usr/bin/bash
for image in *.jpg ; 
do 
    magic "$image" "${image%.*}.png" ;
done

rm -rf *.jpg