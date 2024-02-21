# Image Temperature Adjustment

This script to allow you change the temperature of JPEG image by adjusting its color tones to simulate warmer or cooler temperatures.

## Requiments:
- Make sure you have installed python >=3.9.6 [Required]
- IDE e.g vscode [Optional]

## Dependencies
On this script we used 2 main dependencies:

1. [opencv-python](https://pypi.org/project/opencv-python/), this library helps us to image processing.
2. [numpy](https://pypi.org/project/numpy/), this library helps us to casting data type of number.


## How to run on local (Unix/macOS)
1. open code on your favorite IDE or we can use the terminal and direct to project path.
2. [Optional] create and activate the virtual environment 
```
python3 -m venv .venv 
source .venv/bin/activate
```
3. Prepare the pip to install all dependencies
```
python3 -m pip install --upgrade pip
```
4. Running the script:
```
python3 main.py image_1.jpeg output.jpeg --temperature -11
```