#!user/bin/env python
# -*- coding: utf-8 -*-

# TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。
# 相对TCP，UDP则是面向无连接的协议。

# 使用UDP协议时，不需要建立连接，
# 只需要知道对方的IP地址和端口号，就可以直接发数据包。
# 但是，能不能到达就不知道了。

# 虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，
# 对于不要求可靠到达的数据，就可以使用UDP协议。

# 我们来看看如何通过UDP协议传输数据。
# 和TCP类似，使用UDP的通信双方也分为客户端和服务器。
# 服务器首先需要绑定端口：

s=socket.socket(scoket.AF_INET,socket.SOCK.DGRAM)
# 绑定端口：
s.bind(('127.0.0.1',9999))
