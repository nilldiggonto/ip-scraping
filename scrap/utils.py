import httpx

from .models import *


def save_ip_info():
    url = f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
    response = httpx.get(url)
    if response.status_code == 200:
        res = response.json()

        for d in res['data']:
            ip_info,_ = IpInfo.objects.get_or_create(ip=d['ip'])
            protocols = d['protocols']
            list_of_protocols = []
            for p in protocols:
                protocol,_ = Protocols.objects.get_or_create(name=p)
                list_of_protocols.append(protocol)
            ip_info.protocol.add(*list_of_protocols)
            ip_info.port = d['port']
            ip_info.country = d['country']
            ip_info.up_time = d['upTime']

            ip_info.save()
        
        return True
    else:
        return False