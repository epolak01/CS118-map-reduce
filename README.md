################################
Map Reduce Project for CS 118
Fall 2022
################################

How to run locally:
    - Make mapper1.py and reduce1.py executable using 'chmod +x filename.py'
    - Run the following command to pipe sample_data into mapper and mapper output
    into reducer 'cat sample_data |  ./mapper1.py | ./reducer1.py'

Note:
    - Reducers expect sorted inputs
        - For reducer to run properly give sample_data_sorted as an input to 
        the mapper instead