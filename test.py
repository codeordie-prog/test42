from langchain_google_cloud_sql_mysql import MySQLEngine,MySQLLoader
import sqlalchemy


# @markdown Please fill in the both the Google Cloud region and name of your Cloud SQL instance.
REGION = ""  # @param {type:"string"}
INSTANCE = ""  # @param {type:"string"}
DATABASE = ""  # @param {type:"string"}
TABLE_NAME = ""  # @param {type:"string"}
USER = ''
PASSWORD = ''
PROJECT_ID = ''



engine = MySQLEngine.from_instance(
    project_id=PROJECT_ID, region=REGION, instance=INSTANCE, database=DATABASE,user=USER,password=PASSWORD
)

def result():
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text(f'SELECT * FROM {TABLE_NAME}'))
        return result.fetchall()


res = result()

print(res)