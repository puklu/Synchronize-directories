# Synchronization tool

The "Synchronization Tool" is a Python-based utility that facilitates one-way synchroniza-
tion between two directories: the `Source` directory and the `Replica` directory. This tool
ensures that the contents of the Replica directory remain fully identical to the Source direc-
tory.

## Pre-requisities
The Synchronization Tool is developed using Python programming language. It has
been tested and verified to work with Python 3.x (where x is the latest version at
the time of development). Please ensure that you have Python 3.x installed on your
system to run the tool.


`schedule` library is required to be installed to use the tool.

    pip install schedule

or 

`requirements.txt` included in the project can be used to install the dependencies.

      pip install -r requirements.txt

## Usage
1. Clone this repository:
    
        git clone https://github.com/puklu/Synchronize-directories.git

2. Navigate to the location where the project is cloned. Navigate into the "src" folder:
    
         cd src

3. Execute the script with appropriate command-line arguments to initiate synchronization. 

   The tool accepts the following parameters:

   <u><strong>Mandatory</strong></u>
 
   1. `-src`: Path to the `Source` directory.

   <u><strong>Optional but recommended</strong></u>

   2. `-rep`: Path to the `Replica` directory.
   
         Default location is the root of this project if not provided by the user.

   3. `-sync`: Interval (in minutes) at which synchronization should be performed.
    
         Default value is 30 minutes if not provided by the user.

   4. `-logf`: Path to where a log file should be saved. 

         Default location is the root of this project if not provided by the user.

   Example 1 (with all the parameters):

         python3 main.py -src <path/to/source-dir> -rep <path/to/replica-dir> -sync <sync_interval> -logf <path/to/logfile>

   Example 2 (with only the mandatory parameter):

         python3 main.py -src <path/to/source-dir>
