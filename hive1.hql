-- DROP TABLE IF EXISTS results1;

-- CREATE EXTERNAL TABLE results1 (
--               pagename string,
--               dates array<date>,
--               date_views array<int>,
--               total_views int,
--               pop_trend int
--        )
-- ROW FORMAT DELIMITED
-- FIELDS TERMINATED BY '\t'
-- LINES TERMINATED BY '\n'
-- STORED AS TEXTFILE
-- -- LOCATION "${INPUT}";
-- LOCATION "/sample_data/hive_sample.txt";

-- INSERT OVERWRITE DIRECTORY "/sample_data/hive_output.txt"
-- SELECT * FROM results1;

-- CREATE TABLE results1 (
--     pagename string,
--     dates array<date>,
--     date_views array<int>,
--     total_views int,
--     pop_trend int
-- ) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

-- describe results1;

-- LOAD DATA LOCAL INPATH '/sample_data/hive_sample.txt' INTO TABLE results1;

CREATE TABLE results (pagename string,
                dates array<date>,
                date_views array<int>,
                total_views int,
                pop_trend int
              ) row format delimited fields terminated by '\t' stored as textfile

-- Top 100 websites by views
SELECT pagename, total_views 
FROM results1
ORDER BY total_views, pagename
LIMIT 100;


-- Top 100 websites by popularity trend
SELECT pagename, pop_trend 
FROM results1
ORDER BY pop_trend, pagename
LIMIT 100;

-- Search by "sort"
SELECT pagename, dates, date_views, total_views, pop_trend 
FROM results1
WHERE pagename LIKE '%sort%'
ORDER BY pagename;

-- Search by "house"
SELECT pagename, dates, date_views, total_views, pop_trend 
FROM results1
WHERE pagename LIKE '%house%'
ORDER BY pagename;

-- Search by "men"
SELECT pagename, dates, date_views, total_views, pop_trend 
FROM results1
WHERE pagename LIKE '%men%'
ORDER BY pagename;

-- Search by "fox"
SELECT pagename, dates, date_views, total_views, pop_trend 
FROM results1
WHERE pagename LIKE '%fox%'
ORDER BY pagename;



-- <configuration>
-- <property>
-- <name>hive.querylog.location</name>
-- <value>/Users/apache-hive-3.1.3-bin/log/hive.log</value>
-- </property>
-- <property>
-- <name>hive.log.explain.output</name>
-- <value>false</value>
-- </property>
-- <property>
-- <name>javax.jdo.option.ConnectionURL</name>
-- <value>jdbc:mysql://localhost:3306/hive?createDatabaseIfNotExist=true</value>
-- </property>
-- <property>
-- <name>javax.jdo.option.ConnectionDriverName</name>
-- <value>com.mysql.cj.jdbc.Driver</value>
-- </property>
-- <property>
-- <name>javax.jdo.option.ConnectionUserName</name>
-- <value>hive</value>
-- </property>
-- <property>
-- <name>javax.jdo.option.ConnectionPassword</name>
-- <value>Malabia@1424</value>
-- </property>
-- <property>
-- <name>hive.metastore.schema.verification</name>
-- <value>false</value>
-- </property>
-- <property>
-- <name>hive.metastore.warehouse.dir</name>
-- <value>hdfs://localhost:9000/user/hive/warehouse</value>
-- </property>
-- </configuration>
