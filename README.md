# micframe
 Use your microphone to pick a frame from an image sequence
 
 Designed with the [baby eating microphone meme](https://www.youtube.com/watch?v=_nbW9WtII9Q) in mind, but not hardcoded for just that.

## Requirements
* Python 3.*
* sounddevice module

## Configuration
* **new** use the config.txt to tune settings
* `folder ` is the root where your pictures are
* use `sensitivity` if the images don't respond or always peak
* `width`/`height` change the window size for larger images
* `min`/`low`/`max` indexes for minimum frame, low - max used for microphone range
* `ext` file extension of images

## Bugs
* crashes without warning on lost focus (send help)
