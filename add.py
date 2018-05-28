from sqlalchemy import create_engine
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler

from apscheduler.jobstores.base import BaseJobStore, JobLookupError, ConflictingIdError
from apscheduler.util import maybe_ref, datetime_to_utc_timestamp, utc_timestamp_to_datetime
from apscheduler.job import Job

# import psycopg2

# conn = psycopg2.connect(database="lightSaber", user="postgres", password="admin", host="127.0.0.1", port="5432")
# engine=create_engine('postgresql://postgres:hello@localhost/admin')
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/deepak')
print engine

conn = engine.connect()
print type(conn)
cur=(conn.connection)
e=cur.cursor
print type(e)
e=SQLAlchemyJobStore
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler


jobstores = {
    # 'sqlalchemy': SQLAlchemyJobStore,
    'default': SQLAlchemyJobStore(url='postgresql+psycopg2://postgres:admin@localhost/deepak')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
sched = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
print jobstores
# sched = BlockingScheduler()
print sched.get_jobs()


@sched.scheduled_job('interval', seconds=2)
def myfunc():
	
	with open("test.txt", "a") as myfile:
         myfile.write("appended text")  
         print"function without metadata"


# scheduler.add_job(myfunc, 'interval', seconds=3)
@sched.scheduled_job('interval', seconds=2)
def myfunc1():
         print"function without"

x=sched.add_job(myfunc, jobstore=jobstores)
job = sched.add_job(myfunc, 'interval', seconds=2,jobstore=jobstores)

sched.print_jobs()
print "job is ",job
print "jobstores is ",jobstores


y=sched.add_job(myfunc1, jobstore=jobstores)
print  "x is ",x

print  "y is ",y
# print sched.get_all_jobs()

print "hello is ",sched.print_jobs()

scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

scheduler.start()
