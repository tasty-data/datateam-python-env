import sys
print(sys.version)

import os
sys.path.append(f'/Users/{os.environ.get("USER")}/Code/')
import snowflake_connector

sql = "select * from marts.fct_trades limit 10"
df = snowflake_connector.query_snowflake(sql)
print(df.head())
