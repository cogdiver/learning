-- Construyendo estructura para petición de estructura de datos

DROP TABLE IF EXISTS template_fields_section_config;

CREATE TABLE IF NOT EXISTS template_fields_section_config(
    template_section_id int,
    field_order int,
    field_description varchar,
    data_type varchar,
    format varchar,
    allowed_values varchar,
    required Boolean
);

SELECT * FROM template_fields_section_config;

SELECT (field_order - 1) AS column, field_description , data_type, format, allowed_values , required
FROM template_fields_section_config tfsc
WHERE template_section_id = 12 ORDER BY field_order;
