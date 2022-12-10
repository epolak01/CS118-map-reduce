## Map Reduce Project for CS 118 # Fall 2022

#### How to run locally:
Make `mapper1.py` and `reduce1.py` executable using `'chmod +x filename.py'`  
Run the following command to pipe sample_data into mapper and mapper output into reducer:  
`'cat sample_data | ./mapper1.py | ./reducer1.py'`

Note:
Reducers expect sorted inputs  
For reducer to run properly, give sample_data_sorted as an input to the mapper instead. 
        
### AWS Cluster Configuration:  

Launch mode:       Step Execution  
Step type:         Streaming program  

Run1  
Mapper:              `./mappers-buckets/mapper1.py`   
Reducer:             `./reducers-buckets/reducer1.py`   
Input S3 location:   `./input-logs-files/`  
Output S3 location:  `./output-logs-files/m1-r1-2hrs/`  

Run2  
Mapper:              `./mappers-buckets/mapper2.py`  
Reducer:             `./reducers-buckets/reducer2.py`  
Input S3 location:   `./output-logs-files/m1-r1-2hrs/`  
Output S3 location:  `./output-logs-files/m2-r2-2hrs/`  

Action on failure: Terminate cluster  

Release:             emr.5.36.0  
Applications:        Hadoop 2.10.1  

Instance type:       m4.large  
Number of instances: 3  


### CLI Args
`hadoop-streaming -files s3://mappers-bucket/mapper1.py,s3://reducers-bucket/reducer1.py -mapper mapper1.py -reducer reducer1.py -input s3://input-logs-files/ -output s3://output-logs-files/m1-r1-2hrs/`

`hadoop-streaming -files s3://mappers-bucket/mapper2.py,s3://reducers-bucket/reducer2.py -mapper mapper2.py -reducer reducer2.py -input s3://output-logs-files/m1-r1-2hrs/ -output s3://output-logs-files/m2-r2-2hrs/`
