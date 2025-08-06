CREATE EXTERNAL TABLE IF NOT EXISTS customers_ext
WITH (
    LOCATION = 'silver/customers_cleaned/',
    DATA_SOURCE = your_external_data_source,
    FILE_FORMAT = your_file_format
)
AS SELECT * FROM OPENROWSET(
    BULK 'silver/customers_cleaned/',
    DATA_SOURCE = 'your_external_data_source',
    FORMAT = 'DELTA'
) AS rows;