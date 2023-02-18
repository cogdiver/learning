name := "studyTestingScala"

scalaVersion := "2.12.16"


val scalatestVersion = "3.2.13"
val test_dependencies = Seq(
    "org.scalatest" %% "scalatest" % scalatestVersion % "test",
    // "org.scalatest" %% "scalatest-funsuite" % scalatestVersion % "test",
    // "org.scalatest" %% "scalatest-flatspec" % scalatestVersion % "test",
    // "org.scalatest" %% "scalatest-funspec" % scalatestVersion % "test",
    // "org.scalatest" %% "scalatest-wordspec" % scalatestVersion % "test",
    // "org.scalatest" %% "scalatest-freespec" % scalatestVersion % "test",
)

val other_dependencies = Seq(
)

val dependencies = Seq(
    test_dependencies,
    other_dependencies
).flatten

libraryDependencies ++= dependencies
