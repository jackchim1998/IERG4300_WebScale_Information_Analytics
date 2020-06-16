#!/bin/bash
input_file="shakespeare_basket2"
can_pair_file="can_pair_basket2"
local_can_pair_file="local_can_pair_basket2.txt"
final_output_file="final_basket2"
now=$(date +"%T")
local_count_file="count.txt"
echo "Current time : $now"
hdfs dfs -rmr homework2/1b/$can_pair_file 
hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.map.tasks=30 -D mapred.reduce.tasks=5 -file mapper0.py -mapper mapper0.py -file reducer0.py -reducer reducer0.py -input homework2/data/$input_file -output homework2/1b/$can_pair_file
rm $local_can_pair_file
hdfs dfs -cat homework2/1b/$can_pair_file/* >> $local_can_pair_file
hdfs dfs -rmr homework2/1b/$final_output_file
rm $local_count_file
wc -l ../$input_file >> $local_count_file
hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.map.tasks=30 -D mapred.reduce.tasks=5 -files ./$local_count_file#count_file,./$local_can_pair_file#cand_pair -file mapper1.py -mapper mapper1.py -file reducer1.py -reducer reducer1.py -input homework2/data/$input_file -output homework2/1b/$final_output_file
hdfs dfs -cat  homework2/1b/$final_output_file/* | sort -k3 -n -r | sed -n '1,40'p
now=$(date +"%T")
echo "Current time : $now"

