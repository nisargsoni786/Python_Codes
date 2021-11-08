from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
)

topic_list = [NewTopic(name="topic_2_partition", num_partitions=2, replication_factor=1)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)