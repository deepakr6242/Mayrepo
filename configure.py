# # es (17 sloc)  569 Bytes
# """
# Demonstrates how to use the blocking scheduler to schedule a job that executes on 3 second
# intervals.
# """

# from datetime import datetime
# import os

# from apscheduler.schedulers.blocking import BlockingScheduler


# def tick():
#     print('Tick! The time is: %s' % datetime.now())
#     with open("test.txt", "a") as myfile:
#          myfile.write("appended text")  
#          print"function without metadata"


# if __name__ == '__main__':
#     scheduler = BlockingScheduler()
#     scheduler.add_job(tick, 'interval', seconds=3)

#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

#     try:
#         print scheduler.get_jobs()

#         scheduler.start()

#     except (KeyboardInterrupt, SystemExit):
#         pass

from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.mongodb import MongoDBJobStore

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
# SQLAlchemyJobStore.add_job()
from apscheduler.schedulers.background import BackgroundScheduler
# SQLAlchemyJobStore.get_all_jobs()
engine = create_engine('sqlite:///sqlalchemy_example.db')

h=SQLAlchemyJobStore()
# The "apscheduler." prefix is hard coded
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor

#
# jobstores = {
#     'mongo': {'type': 'mongodb'},
#     'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
# }
# executors = {
#     'default': {'type': 'threadpool', 'max_workers': 20},
#     'processpool': ProcessPoolExecutor(max_workers=5)
# }
# job_defaults = {
#     'coalesce': False,
#     'max_instances': 3
# }
# scheduler = BackgroundScheduler()
#
# # .. do something else here, maybe add jobs etc.
#
# scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
