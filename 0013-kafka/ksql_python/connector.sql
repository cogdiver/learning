CREATE SOURCE CONNECTOR jdbc_source WITH (
  'connector.class'          = 'io.confluent.connect.jdbc.JdbcSourceConnector',
  'connection.url'           = 'jdbc:postgresql://localhost:5430/postgres',
  'connection.user'          = 'postgres',
  'connection.password'      = 'postgres',
  'topic.prefix'             = 'jdbc_',
  'table.whitelist'          = 'business_profiles',
  'mode'                     = 'incrementing',
  'numeric.mapping'          = 'best_fit',
  'incrementing.column.name' = 'business_id',
  'key'                      = 'business_id',
  'key.converter'            = 'org.apache.kafka.connect.converters.IntegerConverter');