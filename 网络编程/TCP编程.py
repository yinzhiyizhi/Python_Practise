#!user/bin/env python
# -*- coding: utf-8 -*-

# Socket是网络编程的一个抽象概念。
# 通常我们用一个Socket表示“打开了一个网络链接”，
# 而打开一个Socket需要知道目标计算机的IP地址和端口号，
# 再指定协议类型即可。



# 客户端
# 大多数连接都是可靠的TCP连接。
# 创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

# 举个例子，当我们在浏览器中访问新浪时，
# 我们自己的计算机就是客户端，浏览器会主动向新浪的服务器发起连接。
# 如果一切顺利，新浪的服务器接受了我们的连接，
# 一个TCP连接就建立起来的，后面的通信就是发送网页内容了。

# 所以，我们要创建一个基于TCP连接的Socket，可以这样做：

# 导入socket库：
import socket

# 创建一个socket：
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接：
s.connect(('www.sina.com.cn',80))

# 创建Socket时，AF_INET指定使用IPv4协议，
# 如果要用更先进的IPv6，就指定为AF_INET6。
# SOCK_STREAM指定使用面向流的TCP协议，
# 这样，一个Socket对象就创建成功，但是还没有建立连接。

# 客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。
# 新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址，
# 但是怎么知道新浪服务器的端口号呢？

# 答案是作为服务器，提供什么样的服务，端口号就必须固定下来。
# 由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，
# 因为80端口是Web服务的标准端口。
# 其他服务都有对应的标准端口号，
# 例如SMTP服务是25端口，FTP服务是21端口，等等。
# 端口号小于1024的是Internet标准服务的端口，
# 端口号大于1024的，可以任意使用。

# 因此，我们连接新浪服务器的代码如下：

# s.connect(('www.sina.com.cn',80))

# 注意参数是一个tuple，包含地址和端口号。
