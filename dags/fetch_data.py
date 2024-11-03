import time
from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from util.utils import getData
# Creating my default arguments
default_args = {
    'owner' : 'v01d',
    'email' : 'mohamed.ouhami2001@gmail.com',
    'start_date' : datetime(2024,11,3)
}

# Get the data from the API
fetch_data_task = PythonOperator(
    task_id="FetchData",
    python_callable=getData
)

# Pass the data into Apache Kafka


# Train the model on the new data
with DAG('weather_realtime_DAG',default_args=default_args) as weather_dag:
    pass

    # Get the data each 2 minutes
    