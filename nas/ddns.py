import httplib, urllib
import urllib2
import socket
import time
import json
import sys
comm_params = dict(
    login_token='your own token',
    format='json',
)
def getCommParams():
    global comm_params
    return comm_params

def getIp():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    ip = sock.recv(16)
    sock.close()
    return ip

def doRequest2(url,params):
    url = 'https://dnsapi.cn'+url
    params = urllib.urlencode(params)
    params = urllib.unquote(params)
    req = urllib2.Request(url,params)
    response = urllib2.urlopen(req)
    data = response.read()
    data = json.loads(data)
    return data

def getDomainList():
    comm_params = getCommParams()
    data = doRequest2('/Domain.List',comm_params)
    return data

def getDomainInfo(id):
    params = getCommParams()
    params['domain_id']=id
    url = '/Domain.Info';
    data = doRequest2(url,params)
    return data

def getRecordList(id):
    params = getCommParams()
    params['domain_id']=id
    url = '/Record.List';
    data = doRequest2(url,params)
    return data

def getSubRecord(record_list,name):
    total = record_list['info']['record_total']
    records = record_list['records']
    sub_item = {}
    for i in records:
        if name == i['name']:
            sub_item = i
            break
    return sub_item

def doRecordModify(domain_id,record_id,record_type,record_line_id,sub_domain,value):
    params = getCommParams()
    params['domain_id']=domain_id
    params['record_id']=record_id
    params['record_type']=record_type
    params['record_line_id']=record_line_id
    params['sub_domain']=sub_domain
    params['value']=value
    url = '/Record.Modify';
    data = doRequest2(url,params)
    return data


def doChangeIp(ip):
    domain_list = getDomainList()
    id = domain_list['domains'][0]['id']
    domain = domain_list['domains'][0]['punycode']
    record_list = getRecordList(id)
    home = getSubRecord(record_list,'home')
    home_id = home['id']
    home_prev_ip = home['value']
    line_id = home['line_id']
    if ip == home_prev_ip:
        return 
    status = doRecordModify(id,home_id,'A',line_id,'home',ip)
    if status['status']['code'] == '1':
        print "home ip was changed! from:"+home_prev_ip+" to:"+ip
        print status
    else:
        print "ERROR: home something wrong"
        print status

raw_ip = getIp()
doChangeIp(raw_ip)
while True:
    time.sleep(600)
    ip = getIp()
    if ip == raw_ip:
        continue
    raw_ip = ip
    doChangeIp(ip)
