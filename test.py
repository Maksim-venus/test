#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

def fetch_ip_info():
    url = 'https://ipinfo.io'
    try:
        # 使用 with 语句确保请求完毕后自动关闭连接
        with urllib.request.urlopen(url) as response:
            # 读取响应并解码为 utf-8 字符串
            data = response.read().decode('utf-8')
            print(data)
    except Exception as e:
        print(f"提取IP信息时发生错误: {e}")

if __name__ == '__main__':
    fetch_ip_info()
