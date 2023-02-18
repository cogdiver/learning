name := "scala_project"

// scalaVersion := "2.10.4"
scalaVersion := "2.11.12"

autoCompilerPlugins := true

scalacOptions ++= Seq("-unchecked", "-deprecation")

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor" % "2.4.20",
  "com.typesafe.akka" %% "akka-dataflow" % "2.3.16",
  "com.typesafe.akka" %% "akka-stream" % "2.5.32"
)
