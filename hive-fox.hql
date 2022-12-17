CREATE EXTERNAL TABLE IF NOT EXISTS results (
    pagename string,
    dates string,
    date_views string,
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
SELECT pagename, dates, date_views, total_views, pop_trend 
FROM results
WHERE pagename LIKE '%fox%'
ORDER BY total_views DESC, pagename;



