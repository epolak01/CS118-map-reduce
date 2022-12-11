CREATE EXTERNAL TABLE IF NOT EXISTS results (
    pagename string,
    dates array<date>,
    date_views array<int>,
    total_views int,
    pop_trend int
)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION "${INPUT}";

INSERT OVERWRITE DIRECTORY "${OUTPUT}"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
  SELECT pagename, total_views 
  FROM results
  ORDER BY total_views DESC, pagename
  LIMIT 100;