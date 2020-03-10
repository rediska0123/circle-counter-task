[![Build Status](https://travis-ci.com/rediska0123/circle-counter-task.svg?branch=master)](https://travis-ci.com/rediska0123/circle-counter-task)

# Circle Counter

A program which counts the number of black and red circles in .png file.

The input .png file should contain only black/red circles and rectangles separated with green background.

### Before using
```
$ pip install -r requirements.txt
```

### Usage
```
$ python3 main.py 'your_filepath'
```

### Usage Example
```
$ python3 main.py tests/test1.png
Read circles: 3
Black circles: 1
```
test1.png file looks like this:

![Test image](https://github.com/rediska0123/circle-counter-task/blob/master/tests/test1.png)

### Tests
To run tests type:
```
$ pytest
```
