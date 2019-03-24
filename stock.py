# -*- coding: utf-8 -*-
import os
import json
import requests

headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Accept-Language': 'zh-Hans-CNq=1'
}

class Stock:

    code = None
    exchange = None
    name = None
    close = None
    price_change = None
    p_change = None
    volume = None
    amount = None
    amplitude = None
    high = None
    low = None
    open = None
    last_colse = None
    volume_ratio = None  # 量比
    turnoverrate = None  # 换手率
    pe = None
    pb = None
    market_capital = None  # 总市值
    float_market_capital = None  # 流通市值
    published_at = None
    updated_at = None

    keys = ['code', 'exchange', 'name', 'close', 'price_change', 'p_change', 'volume', 'amount', 'amplitude', 'high', 'low', 'open', 'last_colse',
            'volume_ratio', 'turnoverrate', 'pe', 'pb', 'market_capital', 'float_market_capital', 'published_at', 'updated_at']

    def __init__(self, stock):
        if isinstance(stock, int):
            self.id = stock
        elif isinstance(stock, dict):
            for i in self.keys:
                setattr(self, i, stock[i])

    def __str__(self):
        return json.dumps({
            'exchange': self.exchange,
            'code': self.code,
            'name': self.name,
            'close': self.close,
            'price_change': self.price_change,
            'p_change': self.p_change,
            'volume': self.volume,
            'amount': self.amount,
            'amplitude': self.amplitude,
            'high': self.high,
            'low': self.low,
            'open': self.open,
            'last_colse': self.last_colse,
            'volume_ratio': self.volume_ratio,
            'turnoverrate': self.turnoverrate,
            'pe': self.pe,
            'pb': self.pb,
            'market_capital': self.market_capital,
            'float_market_capital': self.float_market_capital,
            'published_at': self.published_at,
            'updated_at': self.updated_at,
        }, ensure_ascii=False)

def get_stocks():
    keys = ['type', 'code', 'name', 'close', 'price_change', 'p_change', 'volume', 'amount', 'amplitude', 'high', 'low', 'open', 'last_colse', 'xxx1', 'volume_ratio',
            'turnoverrate', 'pe', 'pb', 'market_capital', 'float_market_capital', '60rizhangfu', 'jinchuzhijinzhangfu', 'zhangsu', 'published_at', 'updated_at']
    url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx'
    params = {
        'type': 'CT',
        'token': '4f1862fc3b5e77c150a2b985b12db0fd',
        'sty': 'FCOIATC',
        'cmd': 'C._A',
        'st': '(Code)',
        'sr': '1',
        'p': '1',
        'ps': '100000',
        '_': '1553353282462',
    }
    stocks = []
    res = requests.get(url, params=params, headers=headers)
    data = res.content[1:len(res.content)-1]
    data = json.loads(data.decode('utf-8'))
    i = 0
    for v in data:
        temp = v.split(',')
        item = {}
        for k in range(len(keys)):
            keys[k]
            item[keys[k]] = temp[k]
        if item['type'] == '2':
            item['exchange'] = 'SZ'
        if item['type'] == '1':
            item['exchange'] = 'SH'
        i = i+1
        stock = Stock(item)
        stocks.append(item)
    return stocks
