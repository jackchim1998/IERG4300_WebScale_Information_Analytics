#!/bin/bash
input_file="shakespeare_basket2"
can_tri_file="can_tri_basket2"
local_can_tri_file="local_can_tri_basket2.txt"
final_output_file="final_basket2"
local_count_file="count.txt"
now=$(date +"%T")
echo "Current time : $now"
hdfs dfs -rmr homework2/1c/$can_tri_file 
hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.map.tasks=30 -D mapred.reduce.tasks=5 -file mapper0.py -mapper mapper0.py -file reducer0.py -reducer reducer0.py -input homework2/data/$input_file -output homework2/1c/$can_tri_file
rm $local_can_tri_file
hdfs dfs -cat homework2/1c/$can_tri_file/* >> $local_can_tri_file
hdfs dfs -rmr homework2/1c/$final_output_file
rm $local_count_file
wc -l ../$input_file >> $local_count_file
hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.map.tasks=30 -D mapred.reduce.tasks=5 -files ./$local_can_tri_file#cand_tri,./$local_count_file#count_file -file mapper1.py -mapper mapper1.py -file reducer1.py -reducer reducer1.py -input homework2/data/$input_file -output homework2/1c/$final_output_file
hdfs dfs -cat  homework2/1c/$final_output_file/* | sort -k4 -n -r | sed -n '1,20'p
now=$(date +"%T")
echo "Current time : $now"

