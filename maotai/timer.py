# -*- coding:utf-8 -*-
import time
import requests
import json

from datetime import datetime
from maotai.jd_logger import logger
from maotai.config import global_config

def jdtimer():
    url = "https://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5"

    payload={}
    headers = {
    'authority': 'api.m.jd.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__jda=76161171.1662704395096758715487.1662704395.1662704395.1662704395.1; __jdc=76161171; __jdv=76161171|direct|-|none|-|1662704395096; __jdu=1662704395096758715487; areaId=19; ipLoc-djd=19-1655-0-0; PCSYCityID=CN_440000_441900_0; shshshfpa=5cabc27e-ef57-60b4-93c7-f03db9fdd1ab-1662704397; shshshfpb=bZhCt56J9DV5Fkfye7WD5vw; __jdb=76161171.2.1662704395096758715487|1.1662704395; shshshfp=cb8d594f205a8afff5b182e41feec7a4; shshshsID=d957bf00a3d02c4641405fd7a06f0913_2_1662705393787; 3AB9D23F7A4B3C9B=IXWO3TLCTKBLWYRLQS65GPR7EXH7SZF3YHJ6JX5RTFUCNCFIMH75XNU5TPPQTXRQMTM24QU2ESEYADAD2XDXDI26PU',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

class Timer(object):
    def __init__(self, sleep_interval=0.01):
        # '2018-09-28 22:45:50.000'
        # buy_time = 2020-12-22 09:59:59.500
        localtime = time.localtime(time.time())
        buy_time_everyday = global_config.getRaw('config', 'buy_time').__str__()
        last_purchase_time_everyday = global_config.getRaw('config', 'last_purchase_time').__str__()

        # 最后购买时间
        last_purchase_time = datetime.strptime(
            localtime.tm_year.__str__() + '-' + localtime.tm_mon.__str__() + '-' + localtime.tm_mday.__str__() + ' ' + last_purchase_time_everyday,
            "%Y-%m-%d %H:%M:%S.%f")

        buy_time_config = datetime.strptime(
            localtime.tm_year.__str__() + '-' + localtime.tm_mon.__str__() + '-' + localtime.tm_mday.__str__() + ' ' + buy_time_everyday,
            "%Y-%m-%d %H:%M:%S.%f")

        if time.mktime(localtime) < time.mktime(buy_time_config.timetuple()):
            # 取正确的购买时间
            self.buy_time = buy_time_config
        # elif time.mktime(localtime) > time.mktime(last_purchase_time.timetuple()):
        #     # 取明天的时间 购买时间
        #     self.buy_time = datetime.strptime(
        #         localtime.tm_year.__str__() + '-' + localtime.tm_mon.__str__() + '-' + (
        #                 localtime.tm_mday + 1).__str__() + ' ' + buy_time_everyday,
        #         "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.buy_time = datetime.strptime(
                localtime.tm_year.__str__() + '-' + localtime.tm_mon.__str__() + '-' + (
                        localtime.tm_mday + 1).__str__() + ' ' + buy_time_everyday,
                "%Y-%m-%d %H:%M:%S.%f")

        # self.buy_time = buy_time_config
        print("购买时间：{}".format(self.buy_time))

        self.buy_time_ms = int(time.mktime(self.buy_time.timetuple()) * 1000.0 + self.buy_time.microsecond / 1000)
        self.sleep_interval = sleep_interval

        self.diff_time = self.local_jd_time_diff()

    def jd_time(self):
        """
        从京东服务器获取时间毫秒
        :return:
        """
        # url = 'https://a.jd.com//ajax/queryServerData.html'
        # ret = requests.get(url).text
        # print(ret)
        # js = json.loads(ret)
        # return int(js["serverTime"])

        ret = jdtimer()
        js = json.loads(ret)
        return int(js["currentTime2"])

    def local_time(self):
        """
        获取本地毫秒时间
        :return:
        """
        return int(round(time.time() * 1000))

    def local_jd_time_diff(self):
        """
        计算本地与京东服务器时间差
        :return:
        """
        return self.local_time() - self.jd_time()

    def start(self):
        logger.info('正在等待到达设定时间:{}，检测本地时间与京东服务器时间误差为【{}】毫秒'.format(self.buy_time, self.diff_time))
        while True:
            # 本地时间减去与京东的时间差，能够将时间误差提升到0.1秒附近
            # 具体精度依赖获取京东服务器时间的网络时间损耗
            if self.local_time() - self.diff_time >= self.buy_time_ms:
                logger.info('时间到达，开始执行……')
                break
            else:
                time.sleep(self.sleep_interval)