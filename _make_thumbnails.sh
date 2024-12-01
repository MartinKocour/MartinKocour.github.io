#!/bin/bash

for file in images/*.jpg; do
    echo $file
    [ ! -f "tn/$file" ] && magick "$file"  -thumbnail 160x160 "tn/$file"
done
