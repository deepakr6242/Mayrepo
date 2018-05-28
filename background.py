## Example 1: Using looping technique
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
  print  a,b
print fib(5)

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    print num
factorial(5)

from sqlalchemy import create_engine
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

from datetime import date

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler

from apscheduler.jobstores.base import BaseJobStore, JobLookupError, ConflictingIdError
from apscheduler.util import maybe_ref, datetime_to_utc_timestamp, utc_timestamp_to_datetime
from apscheduler.job import Job
import logging

import jenkins



logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

# import psycopg2

# conn = psycopg2.connect(database="lightSaber", user="postgres", password="admin", host="127.0.0.1", port="5432")
# engine=create_engine('postgresql://postgres:hello@localhost/admin')
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/hello')
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
        'default': SQLAlchemyJobStore(url='postgresql+psycopg2://postgres:admin@localhost/hello')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1,
    'misfire_grace_time':1200
}

sched = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

#  print job_defaults

# except Exception as e:
#   print e
# # seca=40
# @sched.scheduled_job('interval', seconds=4)
# def myfunc():
    
#   with open("test.txt", "a") as myfile:
#          myfile.write("hello")  
#          print"function  After restart"

# secb=40
# @sched.scheduled_job('interval', seconds=40)
# def hello():
#   with open("test.txt", "a") as myfile:
#          myfile.write("second 40  file")  
#          print"hello"
# date='2018-03-0 10:28:55'
# @sched.scheduled_job('date', run_date=date)
# def build_add():
#     # supplying the values  for kwargs
  
#      # server_c = jenkins.Jenkins('http://10.144.169.116:8080', username='admin', password='TechL@b')
#      # print request.POST['CARD/CPS/Authorization']
#      # url=request.POST['url2']
#      # print url
#      try:
#       # build=server_c.build_job('POC/ET_Trail');
#       print "job build initiated successfully"
#       # return HttpResponse(simplejson.dumps(build), content_type='application/json')
#      except Exception as e:
#         print e
#      with open("test.txt", "a") as myfile:
#          myfile.write("2018-03-07 08:39:55' printed")
# #          print"hello
       
# sched.add_job(build_add, 'date', run_date='2018-03-08 18:01:50',misfire_grace_time=10000,max_instances=3)
# # # sched = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

# # print "scheduled job from store",sched.get_jobs('default')


# date='2018-03-08 18:05:58'

# @sched.scheduled_job('date', run_date=date)
# def build_scheduled():
#     # supplying the values  for kwargs
  
#      # server_c = jenkins.Jenkins('http://10.144.169.116:8080', username='admin', password='TechL@b')
#      # print request.POST['CARD/CPS/Authorization']
#      # url=request.POST['url2']
#      # print url
#      try:
#       # build=server_c.build_job('POC/ET_Trail');
#       print "job build initiated successfully"
#       # return HttpResponse(simplejson.dumps(build), content_type='application/json')
#      except Exception as e:
#         print e
#      with open("test.txt", "a") as myfile:
#          myfile.write("2017-03-07 13:37:40' printed")  

print "scheduled job from store",sched.get_jobs('default')
# print "scheduled jobs are ",sched.get_jobs(pending='True')

sched.start()   
sched.wakeup()    
sched.shutdown(wait=True)


