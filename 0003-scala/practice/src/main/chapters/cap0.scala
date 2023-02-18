// tipos
type PersonaId = Int
case class Persona(id: PersonaId, name: String)
type Estudiante = Persona
new Estudiante(1, "valentina")

// Definición de un trait
trait ejemplo {
    val valor = 5
    def funcion(x: Int) = x * x
}

// Para instanciarse debe usarse un objeto
object ejemplo_object extends ejemplo


// tipos genericos
def f[A](x: A): String = s"valor dado $x"
trait ejemplo[A,B]{
    def g(x: A, f: A => B):B = f(x)
}
object ejemplo_object extends ejemplo[Int, String]


// tipos de datos algebraicos
sealed trait Persona
case class Estudiante(nombre:String) extends Persona
case class Profesor(nombre:String, profesion:String) extends Persona
val me:Persona = Profesor("Daniel","Desarrollador")

val res = me match{
    case Profesor(nombre, profesion) => s"$nombre, es $profesion"
    case Estudiante(nombre) => s"$nombre es estudiante"
}

println(res)

// evaluación lazy
println(y)
lazy val y = x-1
lazy val x = 100
LazyList(1,2,3)

// Disyunciones: Option
val lista = List(1, 2, 3)
lista.find(x=>x==3).map(_+1)
lista.find(x=>x==3).map(x=>lista.headOption.map(y=>x+y))
val resultado = lista.find(x=>x==3).map(x=>lista.headOption.map(y=>x+y))
resultado.getOrElse(0)
None.getOrElse(0)

// 
def divideXByY(x: Int, y: Int): Either[String, Int] = {
    if (y == 0) Left("Dude, can't divide by 0")
    else Right(x / y)
}

divideXByY(4,2)
divideXByY(4,0)