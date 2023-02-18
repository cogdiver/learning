// package modulos

// import akka.dataflow._
// import scala.concurrent.ExecutionContext.Implicits.global
// import scala.concurrent.Promise

// object Cap12 {
//     def run = {

//         val messageFromFuture, rawMessage, parsedMessage = Promise[String]()
//         flow {
//             messageFromFuture << parsedMessage()
//             println("z = " + messageFromFuture())
//         }
//         flow { rawMessage << "olleh" }
//         flow { parsedMessage << toAscii(rawMessage()) }
        
        
//         def toAscii(s: String) = s.reverse
//     }
// }