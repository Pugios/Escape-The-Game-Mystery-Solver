# Escape-The-Game-Mystery-Solver

This repository aims to solve the puzzle behind the game [Escape the Game](https://store.steampowered.com/app/542310/Escape_the_Game/)

## [Sus Files](sus_files/)
These are files that are in my eyes suspicous. All of them can be found in `Steam/steamapps/common/Escape the Game/Levels` (if the game was bought on steam)

## [Decoded Files](decoded_files/)
Sus Files that were decoded to be represented as an Image. Every value was seen as the brightnis of a pixel and ploted on the image. 

## [image_creator.py](image_creator.py)
Code used to create files in "decoded_files" using the "sus_files" as input.
Code was written in a way to allow for colors to be added if wanted. There was no reason to add any color (it would be all just one hue). Functionality was added non-the-less incase anomalies require the coloring if of the images.

## [anomalies.md](anomalies.md)
In some of the sus_file there was a string of numbers and symbols. As time of writing this there is no information on what they indicate and how they should be used. 