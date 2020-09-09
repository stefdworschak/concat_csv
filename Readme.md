# Concatenate two CSV files

## Prerequisites

- Python 3.x & pip ([install instructions](https://raturi.in/blog/installing-python3-and-pip3-ubuntu-mac-and-windows/))

## Setup

1) Clone or download the files from GitHub
3) Start Command Line (Windows) / Terminal (Linux, Mac)
4) Open folder 
```
cd [file download location]
``` 
5) Install requirements
```
[pip|pip3] install -r requirements.txt 
```
6) Copy the two CSV files to be merged to the folder

## Running the script

7) Run script
``` 
[python|python3] concat_csv.py -ff [first filepath] -sf [second filepath] -col [column name]
```

## Using multiple columns

When using multiple columns pass them in separated by a space.

``` 
[python|python3] concat_csv.py -ff [first filepath] -sf [second filepath] -col [col1] [col2] [colN]
```

Using the `-scol` flag the same number and order of values as specified in the `-col` flag need to be used.

## Further Help

For further help run `[python|python3] concat_csv.py -h`.