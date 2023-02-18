

object cap1 {

    List(1, 2, 3).map((x: Int) => x + 1)
    List(1, 2, 3).map(new Function1[Int, Int]{ def apply(x:Int): Int = x + 1})

    def loopTill(cond: => Boolean)(body: => Unit): Unit = {
        if (cond) {
            body
            loopTill(cond)(body)
        }
    }

    var i = 10
    loopTill (i > 0) {
        println(i)
        i -= 1
    }


    // Finding an uppercase character in a string using Scala
    val name = "Valentina"
    val hasUpperCase = name.exists(_.isUpper)

    // Defining a Programmer class in Scala
    class Programmer(var name:String, var language:String, var favDrink:String)
    val p = new Programmer("valentina", "spanish", "coffee")

    // Counting the number of lines in a file in Scala
    val src = scala.io.Source.fromFile("data/someFile.txt")
    val count = src.getLines().map(x => 1).sum

    class FileAsIterable { def iterator = scala.io.Source.fromFile("data/someFile.txt").getLines() }
    val newIterator = new FileAsIterable with Iterable[String]
    newIterator.foreach { line => println(line) }


    val someMap = Map("foo" -> 1, "bar" -> 2)
    someMap.get("foo")

    import scala.language.dynamics
    class MyMap extends Dynamic {
        def selectDynamic(fieldName: String) = map.get(fieldName)
        private val map = Map("foo" -> "1", "bar" -> 2)
    }


    val computers = Array(
        Map("name" -> "Macbook", "color" -> "white"),
        Map("name" -> "HP Pavillion", "color" -> "black")
    )

    // Universal access principles in Scala
    class UAPExample {
        val someField = "hi"
        def someMethod = "there"
    }
    val o = new UAPExample
    o.someField
    o.someMethod
}