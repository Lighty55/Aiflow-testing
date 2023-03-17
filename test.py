from textwrap import dedent
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG(
    'dag_example_read',
    default_args={'retries': 0},
    description="example",
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    dag.doc_md = __doc__

    def hdfs_example(**kwargs):
        print("Hello World")
        print("Testing Airflow flow")

    example_read = PythonOperator(
        task_id='example_read',
        python_callable=hdfs_example,
    )
    example_read.doc_md = dedent(
        """ extract task
            extract data
        """
    )
