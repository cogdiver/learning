import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.{functions => F}
import org.apache.spark.sql.functions.{expr,col}

val COMER_POSITION = 1
def get_comer_name(f: String):String = {f.split("/")(COMER_POSITION)}
def get_ft(f: String) = { if(f.toLowerCase.contains("ft01")) "ft01" else "ft03" }
def read_file(f: String) = { spark.read.format("parquet").load(f) }

def transform_data_specific(df, f, ft, comer) = {

}

def transform_data_general(df, f, ft, comer) = {

}

def transform_data_ft01(df, f, ft, comer) = {

}



def transform_data(df: DataFrame, f: String, ft: String, comer: String) = {
    df = transform_data_specific(df, f, ft, comer)
    df = transform_data_general(df, f, ft, comer)

    if (ft=="ft01"){
        df = transform_data_ft01(df, f, ft, comer)
    }
}

def file_processing(f: String) = {
var df = read_file(f)
val ft = get_ft(f)
val comer = get_comer_name(f)
transform_data(df, f, ft, comer)
}




def main(args: Array[String]): Unit = {

    // Creates a session on a local master
    val spark = SparkSession.builder
                        .appName("CSV to Dataset")
                        .master("local[*]")
                        .getOrCreate

    
    var paths = Array(
        "data/emcali/file_part_00_890399003_2017_FT01.parquet",
        "data/emcali/file_part_00_890399003_2017_00_FT03.parquet"
    )

    paths.map(f => file_processing(f))




    // Good to stop SparkSession at the end of the application
    spark.stop
}