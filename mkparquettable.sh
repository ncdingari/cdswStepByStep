impala-shell -i 10.0.0.41:21000 <<eoj
drop table sample_07p;
create table sample_07p stored as parquet as select * from sample_07;
select * from sample_07p limit 5;
eoj
