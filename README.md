# Synchronization tool
This tool performs one-way synchronization between two directories: `Source` and `Replica`.

The tool maintains a full, identical copy of `Source`
directory at `Replica` directory.

## Pre-requisities
`schedule` library is required to be installed to use the tool.

    pip install schedule

or 

`requirements.txt` included in the project can be used to install the dependencies.

      pip install -r requirements.txt

## Usage
1. Clone the repository:
    
        git clone https://github.com/puklu/Synchronize-directories.git

2. Change directory to the src folder:
    
         cd src

3. To run the script, pass the following command-line arguments:

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
