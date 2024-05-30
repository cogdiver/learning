// Building a Scala MongoDB driver: user stories

// clase con atributos accesibles e inmutables
class MongoClient(val host:String, val port:Int)
// clase con atributos accesibles y mutables
class MongoClient(var host:String, var port:Int)
// clase con atributos no accesibles fuera de la clase
class MongoClient(host:String, port:Int)

val host = "127.0.0.1"
val port = 27017
val client = new MongoClient(host, port)


// Scala imports
import java.util.Date
import java.sql.{Date => SqlDate}
import RichConsole._

// Case class
object cap3 {

    case class Person(firstName:String, lastName:String)
    class Person1(firstName:String, lastName:String)
    val p = Person("Valentina","Arenas")
    val p1 = new Person1("Valentina","Arenas")
    val p2 = Person("Valentina","Arenas")
    p.equals(p2)

    p match {
        case Person(first, last) => println(">>>> " + first + ", " + last)
    }

    object PersonO {
        def apply(firstName:String, lastName:String) = {
            new Person(firstName, lastName)
        }
        def unapply(p:Person): Option[(String, String)] =
            Some((p.firstName, p.lastName))
    }

    val people = List(
        PersonO("Simon", "kish"),
        PersonO("Phil", "Marzullo"),
        PersonO("Eric", "Weimer")
    )
    for(PersonO(first, last) <- people) yield first + "," + last
}
