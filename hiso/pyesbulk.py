# -*- coding:utf-8 -*-
import json
from datetime import datetime, timedelta

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

# client = Elasticsearch()

# testresult = client.get(index='test-index', id=1)
# print testresult['_source']



# s = Search(using=client, index="test-index").query("match", nick="wills")
# s = s.highlight('nick')

# testresult = client.search(index='test-index', body=s.to_dict())
# print '=====fgd========',testresult

# # s = Search(index="test-index").using(client).query("match", title="wills")
# print 'test',s.to_dict()
# response = s.execute()
# print response.hits
# print type(response.hits)
# print response.hits.total

# for hit in response:
#     print type(hit)
#     print(hit.meta)


a = range(10)
# a = []
print a
for i in a:
	aa = i
	testdate = datetime.now()
	timeFormat = datetime.utcfromtimestamp(float(216564865))-timedelta(hours=8)
timeFormat = timeFormat.replace(microsecond=0, second=0, tzinfo=pytz.timezone('UTC')).isoformat()

print timeFormat