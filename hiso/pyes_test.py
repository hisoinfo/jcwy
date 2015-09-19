#coding:utf-8

import pyes
import json


conn = pyes.ES(['121.41.30.237:9200'])#连接es

def creat():
    try:
        conn.indices.create_index('zhang-index1')#新建一个索引
    except:
        pass

    #定义索引存储结构
    mapping = { u'id': {'boost': 1.0,
                          'index': 'not_analyzed',
                          'store': 'yes',
                          'type': u'string',
                          "term_vector" : "with_positions_offsets"},
                  u'user_id': {'boost': 1.0,
                             'index': 'not_analyzed',
                             'store': 'yes',
                             'type': u'string',
                             "term_vector" : "with_positions_offsets"},
                  u'nick': {'boost': 1.0,
                             'index': 'analyzed',
                             'store': 'yes',
                             'type': u'string',
                             "term_vector" : "with_positions_offsets"},
                  u'city': {'boost': 1.0,
                             'index': 'analyzed',
                             'store': 'yes',
                             'type': u'string',
                             "term_vector" : "with_positions_offsets"},
            }

    conn.indices.put_mapping("test-type1", {'properties':mapping}, ["test-index1"])#定义test-type
    conn.indices.put_mapping("test-type2", {"_parent" : {"type" : "test-type1"}}, ["test-index1"])#从test-type继承

    #插入索引数据
    #{"id":"1", "user_id":"u1", "nick":u"压力很大", "city":u"成都"}: 文档数据
    #test-index：索引名称
    #test-type: 类型
    #1: id 注：id可以不给，系统会自动生成
    conn.index({"id":"1", "user_id":"u1", "nick":u"wills", "city":u"chengdu"}, "test-index1", "test-type1", 1)
    conn.index({"id":"2", "user_id":"u2", "nick":u"压力很小", "city":u"北京"}, "test-index1", "test-type1")
    conn.index({"id":"3", "user_id":"u3", "nick":u"没有压力", "city":u"成都"}, "test-index1", "test-type1")

    conn.default_indices=["test-index1"]#设置默认的索引
    conn.indices.refresh()#刷新以获得最新插入的文档

def query():
    print 'pyes====='
    counts_index = conn.indices.get_indices()
    print 'counts====', counts_index

    h=pyes.HighLighter(['<font color="red">'], ['</font>'], fragment_size=20)
    #查询nick中包含压力的记录
    q = pyes.QueryStringQuery( u"力")

    s=pyes.Search(q,highlight=h)
 
    s.add_highlight('nick')
 
    results=conn.search(s)
    print "总共有多条记录+++",results.total

    print q
    # results = conn.search(query = q, highlight=h)

    for r in results:
        print isinstance(r['city'], unicode)
        print json.dumps(r)
        # print 'results are :',r['nick'], r['city'].encode('utf8')
        # print u"查询nick中包含压力的记录", r['nick'].encode('gb2312'), r['city'].encode('gb2312')

    list=[]

    for r in results:
        if(r._meta.highlight.has_key("nick")):
            r['nick']=r._meta.highlight[u"nick"][0]
            list.append(r)
            print r['nick'].encode('utf8')

    print len(list)

    # #查询city中包含成都的数据
    # q = pyes.query.MatchQuery('city', u"成都")
    # results = conn.search(q)

    # for r in results:
    #     print "查询city中包含成都的数据", r['nick'].encode('utf8'), r['city'].encode('utf8')

    #查询nick中包含很小或没有的数据
    q = pyes.query.MatchQuery('nick', u"很小 OR 没有")
    
    results = conn.search(q)
    print q
    print len(results)
    print results

    response = {"status_code": 200, "message": "Successful", "content": []}
    

    p = [p for p in results]
    print 'dict====',p
    for r in results:
        response["content"] = [result for result in results]
        print "查询nick中包含很小或没有的数据", r['nick'].encode('utf8'), r['city'].encode('utf8')
    print 'json', json.dumps(response)

def delete():
    '''
    删除index
    '''
    try:
        conn.indices.delete_index('test')#新建一个索引
    except:
        pass

if __name__ == '__main__':
    creat()
    # query()
    # delete()




'''
#elasticsearch客户端应用
import itertools
import string
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()
# k is a generator expression that produces
 # a series of dictionaries containing test data.
# The test data are just letter permutations
# created with itertools.permutations.
#
# We then reference k as the iterator that's
# consumed by the elasticsearch.helpers.bulk method.
k = ({'_type':'foo', '_index':'test','letters':''.join(letters)}
      for letters in itertools.permutations(string.letters,2))

# calling k.next() shows examples
# (while consuming the generator, of course)
# each dict contains a doc type, index, and data (at minimum)
k.next()
# {'_type': 'foo', 'letters': 'ab', '_index': 'test'}
k.next()
# {'_type': 'foo', 'letters': 'ac', '_index': 'test'}
# create our test index
es.indices.create('test')
# {u'acknowledged': True}
helpers.bulk(es,k)

# check to make sure we got what we expected...
es.count(index='test')
# {u'count': 2650, u'_shards': {u'successful': 1, u'failed': 0, u'total': 1}}
'''



