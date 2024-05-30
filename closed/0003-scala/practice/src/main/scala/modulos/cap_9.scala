package modulos

import akka.pattern.{ask, pipe}
import akka.actor._
import akka.util.Timeout
import scala.concurrent.duration._
import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global

object Cap9 {
    val system = ActorSystem("greetings")
    case class Name(name: String)
    class GreetingsActorSpanish extends Actor {
        def receive = {
            case Name(n) => println("Hola " + n)
        }
    }

    class GreetingsActor extends Actor {
        val b = system.actorOf(Props[GreetingsActorSpanish], name = "greetings-actor-spanish")
        def receive = {
            case Name(n) => {
                println("Hello " + n)
                b ! Name(n)
            }
        }
    }

    def run() = {
        println("9")
        val a = system.actorOf(Props[GreetingsActor], name = "greetings-actor")
        
        a ! Name("Nilanjan")
        a ! Name("Nilanjan2")

        AskPipeExample.run

        Thread.sleep(100)
        system.terminate()
        // system.awaitTermination
    }
}

object AskPipeExample {
  
    implicit val timeout = Timeout(5.seconds) 
    
    class GreetingsActor extends Actor {
        val messageActor = context.actorOf(Props[GreetingsChildActor])
        def receive = {
        case name => 
            val f: Future[String] = (messageActor ask name).mapTo[String]
            f pipeTo sender 
        }
    }
    
    class GreetingsChildActor extends Actor {
        def receive = {
        case name => 
            val now = System.currentTimeMillis
            if(now % 2 == 0) 
                sender ! "Hey " + name  
            else 
                sender ! "Hello " + name
        }
    }

    def run() = { 

        val actorSystem = ActorSystem("askPipeSystem")
        
        val actor = actorSystem.actorOf(Props[GreetingsActor])
        
        val response: Future[String] = (actor ? "Nilanjan").mapTo[String]
        response.onComplete { e =>
            println(e)
            actorSystem.terminate()
        }
    }
}
