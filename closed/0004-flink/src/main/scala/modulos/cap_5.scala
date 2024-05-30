package modulos

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.functions.co.CoMapFunction
import org.apache.flink.api.scala.typeutils.Types

case class Element(id: Int, key: Int, name: String)

object Cap5{
    def run() = {
        val env = StreamExecutionEnvironment.getExecutionEnvironment
        val defaultP = env.getParallelism
        println(defaultP)
        val stream = env.fromElements(1,2,3,4)

        stream.map(r => s"Sumando 2: ${r+2}").print()
        stream.filter(r => r%2==0).map(r => s"Pares ${r}").print()
        stream.flatMap(r =>
            if (r%2==0) List(r, r) else List(r)
        ).map(r => s"Duplicando registros pares: ${r}").print()


        val stream2 = env.fromElements(
            (1, 1, "name 1"),
            (2, 0, "name 2"),
            (3, 1, "name 3"),
            (4, 0, "name 4")
        )
        stream2.keyBy(1).sum(0).print()
        stream2.keyBy(1).reduce((x, y) => (x._1 + y._1, x._2, s"name for key ${x._2}")).print()

        // Multistream Transformations
        val stream3 = env.fromElements(30, 31, 32)
        val stream4 = env.fromElements(40, 41, 42)
        val stream5 = env.fromElements(50, 51, 52)
        val stream6 = env.fromElements("60", "61", "62")
        stream3.union(stream4, stream5).map(r => s"Union: ${r}").print()
        stream3.connect(stream6).map(new CoMapFunction[Int, String, String]() {
            override def map1(r: Int): String = {
                s"Connect Map1: ${r+1}"
            }
            override def map2(r: String): String = {
                s"Connect Map2: $r"
            }
        }).print()

        // // split and select (No funciona)
        // val stream7 = env.fromElements(70, 71, 72, 73, 74)
        // val stream7_split = stream7.split(r => if(r > 72) "large" else "small")
        // stream7_split.select("large").map(r => s"Split Select Large: $r").print()
        // stream7_split.select("small").map(r => s"Split Select Small: $r").print()

        // RichMapFuntion
    
        env.execute("Cap5")
    }
}