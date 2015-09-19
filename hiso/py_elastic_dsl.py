# -*- encoding: utf-8 -*-

import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


client = Elasticsearch()
        
s = Search(using=client, index="test-index").query("match", nick=u"压力")

testresult = client.search(index='test-index', body=s.to_dict(),size=3, from_=3)
print '=============',testresult

response = s.execute()
print s.to_dict()