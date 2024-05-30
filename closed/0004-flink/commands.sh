mvn archetype:generate \
-DarchetypeGroupId=org.apache.flink \
-DarchetypeArtifactId=flink-quickstart-scala \
-DarchetypeGroupId=org.apache.spark \
-DgroupId=flink \
-DartifactId=data-upload-distributed2 \
-Dpackage=flink \
-DarchetypeVersion=1.10.3


mvn package && flink run target/data-upload-distributed-1.0-SNAPSHOT.jar
mvn package && flink run -c flink.StreamingJob target/data-upload-distributed-1.0-SNAPSHOT.jar
mvn package && flink run -c flink.BatchJob target/data-upload-distributed-1.0-SNAPSHOT.jar

.getClass.getMethods.foreach(println)