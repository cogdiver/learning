DROP TABLE IF EXISTS cleaned_records_ft01;
DROP TABLE IF EXISTS cleaned_records_ft03;
DROP TABLE IF EXISTS failed_records_ft01;
DROP TABLE IF EXISTS failed_records_ft03;
DROP TABLE IF EXISTS errors_summary;
DROP TABLE IF EXISTS original_data;

CREATE TABLE IF NOT EXISTS cleaned_records_ft01(
    "TIPO_DOCUMENTO" VARCHAR,
    "NUMERO_DOCUMENTO" VARCHAR,
    "DIGITO_VERIFICACION" VARCHAR,
    "PRIMER_NOMBRE_RAZON_SOCIAL" VARCHAR,
    "SEGUNDO_NOMBRE" VARCHAR,
    "PRIMER_APELLIDO" VARCHAR,
    "SEGUNDO_APELLIDO" VARCHAR,
    "NIU" VARCHAR,
    "NIC_CODIGO_ID" VARCHAR,
    "MEDIDOR" VARCHAR,
    "DIRECCION_ENVIO" VARCHAR,
    "CIUDAD_ENVIO" VARCHAR,
    "DIRECCION_SUMINISTRO" VARCHAR,
    "BARRIO_SUMINISTRO" VARCHAR,
    "CORREGIMIENTO_SUMINISTRO" VARCHAR,
    "MUNICIPIO_SUMINISTRO" VARCHAR,
    "MERCADO" VARCHAR,
    "SECTOR" VARCHAR,
    "DESTINO ECONOMICO PREDIO" VARCHAR,
    "ESTRATO" VARCHAR,
    "NUMERO_FACTURA" VARCHAR,
    "PERIODO_FACTURADO_INICIO" VARCHAR,
    "PERIODO_FACTURADO_FINAL" VARCHAR,
    "AÑO_VIGENCIA" VARCHAR,
    "PERIODO_MES" VARCHAR,
    "CICLO_FACTURACION" VARCHAR,
    "FECHA_VENCIMIENTO_FACTURA" VARCHAR,
    "CONSUMO_KWH" VARCHAR,
    "CONSUMO_KWH_SUBSIDIADO" VARCHAR,
    "CONSUMO_ENERGIA_SIN_SUBSIDIO" VARCHAR,
    "CONSUMO_ENERGIA_SUBSIDIADO" VARCHAR,
    "TARIFA_APLICADA_KWH" VARCHAR,
    "TARIFA_SUBSIDIADA_KWH" VARCHAR,
    "FICHA_CATASTRAL" VARCHAR,
    "CORREO_ELECTRONICO" VARCHAR,
    "OPERADOR" VARCHAR,
    origin VARCHAR
);
CREATE TABLE IF NOT EXISTS cleaned_records_ft03(
    "Número de Identificación" VARCHAR,
    "Digito de Verificación" VARCHAR,
    "NIU" VARCHAR,
    "NIC" VARCHAR,
    "Número de Factura" VARCHAR,
    "Valor Facturado Tasa Seguridad" VARCHAR,
    "Valor Intereses" VARCHAR,
    "Fecha Límite de Pago" VARCHAR,
    "Valor Recaudo" VARCHAR,
    "Fecha de Recaudo" VARCHAR,
    origin VARCHAR
);
CREATE TABLE IF NOT EXISTS failed_records_ft01(
    "TIPO_DOCUMENTO" VARCHAR,
    "NUMERO_DOCUMENTO" VARCHAR,
    "DIGITO_VERIFICACION" VARCHAR,
    "PRIMER_NOMBRE_RAZON_SOCIAL" VARCHAR,
    "SEGUNDO_NOMBRE" VARCHAR,
    "PRIMER_APELLIDO" VARCHAR,
    "SEGUNDO_APELLIDO" VARCHAR,
    "NIU" VARCHAR,
    "NIC_CODIGO_ID" VARCHAR,
    "MEDIDOR" VARCHAR,
    "DIRECCION_ENVIO" VARCHAR,
    "CIUDAD_ENVIO" VARCHAR,
    "DIRECCION_SUMINISTRO" VARCHAR,
    "BARRIO_SUMINISTRO" VARCHAR,
    "CORREGIMIENTO_SUMINISTRO" VARCHAR,
    "MUNICIPIO_SUMINISTRO" VARCHAR,
    "MERCADO" VARCHAR,
    "SECTOR" VARCHAR,
    "DESTINO ECONOMICO PREDIO" VARCHAR,
    "ESTRATO" VARCHAR,
    "NUMERO_FACTURA" VARCHAR,
    "PERIODO_FACTURADO_INICIO" VARCHAR,
    "PERIODO_FACTURADO_FINAL" VARCHAR,
    "AÑO_VIGENCIA" VARCHAR,
    "PERIODO_MES" VARCHAR,
    "CICLO_FACTURACION" VARCHAR,
    "FECHA_VENCIMIENTO_FACTURA" VARCHAR,
    "CONSUMO_KWH" VARCHAR,
    "CONSUMO_KWH_SUBSIDIADO" VARCHAR,
    "CONSUMO_ENERGIA_SIN_SUBSIDIO" VARCHAR,
    "CONSUMO_ENERGIA_SUBSIDIADO" VARCHAR,
    "TARIFA_APLICADA_KWH" VARCHAR,
    "TARIFA_SUBSIDIADA_KWH" VARCHAR,
    "FICHA_CATASTRAL" VARCHAR,
    "CORREO_ELECTRONICO" VARCHAR,
    "OPERADOR" VARCHAR,
    origin VARCHAR,
    com_name VARCHAR,
    err VARCHAR
);
CREATE TABLE IF NOT EXISTS failed_records_ft03(
    "Número de Identificación" VARCHAR,
    "Digito de Verificación" VARCHAR,
    "NIU" VARCHAR,
    "NIC" VARCHAR,
    "Número de Factura" VARCHAR,
    "Valor Facturado Tasa Seguridad" VARCHAR,
    "Valor Intereses" VARCHAR,
    "Fecha Límite de Pago" VARCHAR,
    "Valor Recaudo" VARCHAR,
    "Fecha de Recaudo" VARCHAR,
    origin VARCHAR,
    com_name VARCHAR,
    err VARCHAR
);
CREATE TABLE IF NOT EXISTS errors_summary(
    origin VARCHAR,
    total_initial_records VARCHAR,
    total_errors_no_tf VARCHAR,
    total_errors_tf VARCHAR
);
CREATE TABLE IF NOT EXISTS original_data(
    data VARCHAR,
    origin VARCHAR
);


SELECT * FROM cleaned_records_ft01;
SELECT * FROM cleaned_records_ft03;
SELECT * FROM failed_records_ft01;
SELECT * FROM failed_records_ft03;
SELECT * FROM errors_summary;
SELECT * FROM original_data;



