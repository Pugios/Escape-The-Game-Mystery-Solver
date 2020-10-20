# Escape-The-Game-Mystery-Solver

This repository aims to solve the puzzle behind the game [Escape the Game](https://store.steampowered.com/app/542310/Escape_the_Game/)

## [Sus Files](sus_files/)
These are files that are in my eyes suspicious. All of them can be found in `Steam/steamapps/common/Escape the Game/Levels` (if the game was bought on steam)

## [Decoded Files](decoded_files/)
Sus Files that were decoded to be represented as an Image. Every value was seen as the brightness of a pixel and plotted on the image.

## [image_creator.py](image_creator.py)
Code used to create files in "decoded_files" using the "sus_files" as input. The code was written in a way to allow for colors to be added if wanted. There was no reason to add any color yet since the lack of information would color the entire image in one hue. Functionality was added non-the-less in case anomalies require the coloring if of the images.

## [anomalies.md](anomalies.md)
In some of the sus_files, there was a string of numbers and symbols. At the time of writing this, there is no information on what they indicate and how they should be used.