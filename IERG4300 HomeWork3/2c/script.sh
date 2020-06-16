tmp_data_dir="tmp_data"
input_dir="homework3/data/test_images"
map_num=30
# red_num shouldnot higher than 10
#sometimes there will be centroid near 0 datapoint, we set it be 5
red_num=5
j=0
#create folder for tmp data
rm -r $tmp_data_dir
mkdir $tmp_data_dir
rm final_output*

for i in 1
do
	init_file="init_rand_seed$i"
	final_file="final_output$i"
	output_dir="homework3/2c/tmp_output$i"
	tmp_data_file="tmp_cent_$i"
	#run first time for init_rand_seed
	hdfs dfs -rmr $output_dir
	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.map.tasks=$map_num -D mapred.reduce.tasks=$red_num -files ./$init_file#f_cent -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input $input_dir -output $output_dir
	hdfs dfs -cat $output_dir/* >> $tmp_data_dir/${tmp_data_file}_0
	num_iteration=50
	#run n time for init_rand_seed
	for (( j = 0 ;j <$num_iteration; j++))
	do
		hdfs dfs -rmr $output_dir
		hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.map.tasks=$map_num -D mapred.reduce.tasks=$red_num -files ./$tmp_data_dir/${tmp_data_file}_$j#f_cent -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input $input_dir -output $output_dir
		hdfs dfs -cat $output_dir/* >> $tmp_data_dir/${tmp_data_file}_$((j+1))
	done
	hdfs dfs -rmr $output_dir
	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.map.tasks=$map_num -D mapred.reduce.tasks=1 -files ./$tmp_data_dir/${tmp_data_file}_$j#f_cent -file mapper.py -mapper mapper.py -file reducer_last_rnd.py -reducer reducer_last_rnd.py -input $input_dir -output $output_dir
	hdfs dfs -cat $output_dir/* >> ./$final_file
done
