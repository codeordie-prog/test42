from langchain_google_cloud_sql_mysql import MySQLEngine,MySQLLoader
import sqlalchemy


# @markdown Please fill in the both the Google Cloud region and name of your Cloud SQL instance.
REGION = "us-central1"  # @param {type:"string"}
INSTANCE = "mysqlbudget"  # @param {type:"string"}
DATABASE = "expense_tracker"  # @param {type:"string"}
TABLE_NAME = "expenses"  # @param {type:"string"}
USER = 'kelvin'
PASSWORD = 'Kelvinjoe692'
PROJECT_ID = 'local-vehicle-427618-q4'



engine = MySQLEngine.from_instance(
    project_id=PROJECT_ID, region=REGION, instance=INSTANCE, database=DATABASE,user=USER,password=PASSWORD
)

def result():
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text(f'SELECT * FROM {TABLE_NAME}'))
        return result.fetchall()
