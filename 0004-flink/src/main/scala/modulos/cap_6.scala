package modulos

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.TimeCharacteristic
import java.util.Calendar
import org.apache.flink.streaming.api.functions.source.RichParallelSourceFunction
import org.apache.flink.streaming.api.functions.source.SourceFunction.SourceContext
import scala.util.Random


case class Event(value: String, timestamp: Long)

class EventSource extends RichParallelSourceFunction[Event] {

    var running: Boolean = true

    override def run(srcCtx: SourceContext[Event]): Unit = {

        val rand = new Random()
        val taskIdx = this.getRuntimeContext.getIndexOfThisSubtask
        var curFTemp = (1 to 10).map {
        i => ("event_" + (taskIdx * 10 + i), 65 + (rand.nextGaussian() * 20))
        }

        while (running) {
        curFTemp = curFTemp.map( t => (t._1, t._2 + (rand.nextGaussian() * 0.5)) )
        val curTime = Calendar.getInstance.getTimeInMillis
        curFTemp.foreach( t => srcCtx.collect(Event(t._1, curTime)))

        // wait for 100 ms
        Thread.sleep(100)
        }
    }

    override def cancel(): Unit = {
        running = false
    }
}

object Cap6{
    def run() = {
        val env = StreamExecutionEnvironment.getExecutionEnvironment
        env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)
        // env.setStreamTimeCharacteristic(TimeCharacteristic.ProcessingTime)
        
        val stream = env.addSource(new EventSource)
        stream.print()
        // val withTimestampsAndWatermarks = stream.assignAscendingTimestamps(e => e.timestamp)
        // withTimestampsAndWatermarks.print()
    }
}