object cap4 {
    // Introducing type parameterization
    def position[A](xs: List[A], value: A): Int = {
        xs.indexOf(value)
    }
    val xs = List("one", "two", "three")
    position(xs, "two")
    val ys = List(20, 30, 40)
    position(ys, 40)
    position[Int](ys, 300)

    sealed abstract class Maybe[+A] {
        def isEmpty: Boolean
        def get: A
    }
    final case class Just[A](value: A) extends Maybe[A] {
        def isEmpty = false
        def get = value
    }
    case object Nil extends Maybe[Nothing] {
        def isEmpty = true
        def get = throw new NoSuchElementException("Nil.get")
    }
    
    def position[A](xs: List[A], value: A): Maybe[Int] = {
        val index = xs.indexOf(value)
        if(index != -1) Just(index) else Nil
    }

    // call-by-name
    val logEnabled = true
    val logEnabled = false
    def log(m: String) = if(logEnabled) println(m)
    def log(m: => String) = if(logEnabled) println(m)
    val t0 = System.nanoTime
    log("The error message is ")
    println(System.nanoTime - t0)

    // Building your own function objects
    object foldl {
        def apply(value: String) = {
            println(value)
        }
    }
    trait Function1[T1, R] {
        def apply(v: T1): R
    }
    object printer extends Function1[Int, String]{
        def apply(p: Int): String = s"${p + 1}"
    }

    // type variables is as a representation of a complicated type
    type MILS = Map[Int, List[String]]
    val mapping: MILS = Map(
        1 -> List("one", "uno"),
        2 -> List("two", "dos")
    )

    // compose two functions to create a new function
    val addOne: Int => Int = x => { println(x); x + 1 }
    val addTwo: Int => Int = x => { println(x); x + 2 }
    val addThree = addOne compose addTwo // addOne.compose(addTwo)
    val addThree_ = addTwo compose addOne

    // Scala collection hierarchy
    val mapping = Map(
        "Ron" -> "admin",
        "Sam" -> "Analyst"
    )
    val mapping = collection.mutable.Map("Ron" -> "admin", "Sam" -> "Analyst")

    // Working with List and ListBuffer
    val languages = Seq("Scala", "Haskell", "OCaml", "ML")
}
