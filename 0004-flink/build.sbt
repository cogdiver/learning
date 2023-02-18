name := "study-flink"

version := "0.1"

scalaVersion := "2.12.15"

val flinkVersion = "1.14.4"
val postgresVersion = "42.2.2"
val awsSdkVersion = "1.7.4"
val hadoopVersion = "2.7.3"
val playVersion = "2.9.2"
// val logbackVersion = "1.2.10"

// set the main class for the main 'sbt run' task
mainClass in (Compile, run) := Some("Main")

val flinkDependencies = Seq(
  "org.apache.flink" %% "flink-clients" % flinkVersion,
  "org.apache.flink" %% "flink-scala" % flinkVersion,
  "org.apache.flink" %% "flink-streaming-scala" % flinkVersion,
)

val flinkConnectors = Seq(
  "org.apache.flink" %% "flink-connector-kafka" % flinkVersion,
  "org.apache.flink" %% "flink-connector-cassandra" % flinkVersion,
  "org.apache.flink" %% "flink-connector-jdbc" % flinkVersion,
  "org.apache.flink" % "flink-s3-fs-hadoop" % "1.14.3",
  "org.postgresql" % "postgresql" % postgresVersion
)

val playDependencies = Seq(
  "com.typesafe.play" %% "play-json" % playVersion
)

libraryDependencies ++= flinkDependencies ++ flinkConnectors ++ playDependencies
