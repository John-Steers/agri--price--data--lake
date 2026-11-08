import duckdb
def main():
    con=duckdb.connect()
    sql="""SELECT county,commodity,round(avg(price_kes),2) avg_price_kes,count(*) observations
    FROM read_parquet('data/warehouse/**/*.parquet',hive_partitioning=true)
    GROUP BY county,commodity ORDER BY county,commodity"""
    print(con.execute(sql).df().to_string(index=False))
if __name__=="__main__": main()
