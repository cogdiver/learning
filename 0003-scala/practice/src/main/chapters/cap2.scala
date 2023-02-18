import org.apache.http._
import org.apache.http.client.entity._
import org.apache.http.client.methods._
import org.apache.http.impl.client._
import org.apache.http.client.utils._
import org.apache.http.message._
import org.apache.http.params._


object cap2 {
    val bookName = "Scala in \"Action\""

    val multiLine = """This is a
    multi line
    string"""

    // String interpolation
    val name = "Nilanjan"
    s"My name $name"

    val height = 1.9d
    val name = "James"
    println(f"$name%s is $height%2.2f meters tall")

    // XML LITERALS
    val book = <book>
        <title>Scala in Action</title>
        <author>Nilanjan Raychaudhuri</author>
    </book>

    val message = "I didn't know xml could be so much fun"
    val code = "1"
    val alert = <alert>
        <message priority={code}>{message}</message>
        <date>{new java.util.Date()}</date>
    </alert>

    // Defining variables
    var willKnowLater:String = _
    val first :: rest = List(1, 2, 3)

    // Defining functions
    def myFirstMethod():String = { "exciting times ahead" }
    def max(a: Int, b: Int) = if(a > b) a else b

    // FUNCTION LITERALS
    val evenNumbers = List(2, 4, 6, 8, 10)
    evenNumbers.foldLeft(0) { (a: Int, b:Int) => a + b }
    evenNumbers.foldLeft(0) { _ + _ }

    // 
    def break = new RuntimeException("break exception")
    def install = {
        val env = System.getenv("SCALA_HOME")
        if(env == null) break
        println("found scala home lets do the real work")
    }

    // Working with Array and List
    val array = new Array[String](3)
    array(0) = "This"
    array(1) = "is"
    array(2) = "mutable"

    val myList = scala.collection.immutable.List("This", "is","immutable")

    val oldList = List(1, 2)
    val newList = 3 :: oldList
    val newList = oldList :+ 3
    val myList = "This" :: "is" :: "immutable" :: Nil
    val afterDelete = newList.filterNot(_ == 3)

    // documentation
    def getClassAsString(x: Any):String = x match {
        case x: String => "String"
        case x: Int => "Int"
        case x: Float => "Float"
        case x: Double => "Double"
        case x: List[_] => "List"
        case _ => "Unknown"
    }

    // For-comprehensions
    val files = new java.io.File("src/main/package").listFiles
    for(file <- files) {
        val filename = file.getName
        if (filename.endsWith(".scala")) println(file)
    }

    val aList = List(1, 2, 3)
    val bList = List(4, 5, 7)
    for { a <- aList; b <- bList } println(a + b)

    val result = for { a <- aList; b <- bList } yield a + b
    val xmlNode = <result>{result.mkString(",")}</result>

    // Pattern matching
    def ordinal(number:Int) = number match {
        case 1 => println("1st")
        case 2 => println("2nd")
        case 3 => println("3rd")
        case 4 => println("4th")
        case 5 => println("5th")
        case 6 => println("6th")
        case 7 => println("7th")
        case 8 => println("8th")
        case 9 => println("9th")
        case 10 => println("10th")
        case _ => println("Cannot do beyond 10")
    }

    def printType(obj: AnyRef) = obj match {
        case s: String => println("This is string")
        case l: List[_] => println("This is List")
        case a: Array[_] => println("This is an array")
        case d: java.util.Date => println("This is a date")
    }

    List(1, 2, 3, 4) match {
        case f :: s :: rest => List(f, s)
        case _ => Nil
    }

    def rangeMatcher(num:Int) = num match {
        case within10 if within10 <= 10 => println("with in 0 to 10")
        case within100 if within100 <= 100 => println("with in 11 to 100")
        case beyond100 if beyond100 < Integer.MAX_VALUE => println("beyond 100")
    }

    val suffixes = List("th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th")
    def ordinal(number:Int) = number match {
        case number if 10 to 20 contains number => number + "th"
        case rest => rest + suffixes(number % 10)
    }

    // Exception handling
    def rangeMatcher(num:Int) = num match {
        case within10 if within10 <= 10 => println("with in 0 to 10")
        case within100 if within100 <= 100 => println("with in 11 to 100")
        case _ => throw new IllegalArgumentException(
        "Only values between 0 and 100 are allowed")
    }

    try {
        rangeMatcher(1000)
    } catch {
        case e: IllegalArgumentException => e.getMessage
    }
    
    
    // Introducing HttpClient library
    val url = "https://www.example.com/"
    val httpDelete = new HttpDelete(url)
    val http = new HttpGet(url)
    val httpResponse = new DefaultHttpClient().execute(httpDelete)
    val httpResponse = new DefaultHttpClient().execute(http)

    // Building the client, step by step
    require(args.size >= 2, "at minimum you should specify action(post, get, delete, options) and url")
    def parseArgs(args: Array[String]): Map[String, List[String]] = {
        def nameValuePair(paramName: String) = {
            def values(commaSeparatedValues: String) =
                commaSeparatedValues.split(",").toList
            val index = args.indexOf(paramName)
            (paramName, if(index == -1) Nil else values(args(index + 1)))
        }
        Map(nameValuePair("-d"), nameValuePair("-h"))
    }

    val command = args.head
    val params = parseArgs(args)
    val url = args.last

    // Creating a Tuple
    val tuple2 = ("list of one element", List(1))
    val tuple2 = new scala.Tuple2("list of one element", List(1))
    val m = Map(("key1", "value1"), ("key2", "value2"))

    command match {
        case "post" => handlePostRequest
        case "get" => handleGetRequest
        case "delete" => handleDeleteRequest
        case "options" => handleOptionsRequest
    }

    def headers = for(nameValue <- params("-h")) yield {
        def tokens = splitByEqual(nameValue)
        new BasicHeader(tokens(0), tokens(1))
    }

    def handleGetRequest = {
        val query = params("-d").mkString("&")
        val httpget = new HttpGet(s"${url}?${query}")
        headers.foreach { httpget.addHeader(_) }
        val responseBody = ew DefaultHttpClient().execute(
            httpget,
            new BasicResponseHandler()
        )
        println(responseBody)
    }

    // Preparing a POST request and invoking the REST service
    def formEntity = {
        def toJavaList(scalaList: List[BasicNameValuePair]) = {
            java.util.Arrays.asList(scalaList.toArray:_*)
        }
        def formParams = for(nameValue <- params("-d")) yield {
            def tokens = splitByEqual(nameValue)
            new BasicNameValuePair(tokens(0), tokens(1))
        }
        def formEntity = new UrlEncodedFormEntity(toJavaList(formParams), "UTF-8")
        formEntity
    }
    def handlePostRequest = {
        val httppost = new HttpPost(url)
        headers.foreach { httppost.addHeader(_) }
        httppost.setEntity(formEntity)
        val responseBody = new DefaultHttpClient().execute(
            httppost,
            new BasicResponseHandler()
        )
        println(responseBody)
    }

    val scalaList = List(1, 2, 3)
    val javaList = java.util.Arrays.asList(scalaList.toArray)
    val javaList = java.util.Arrays.asList(scalaList.toArray:_*)
}