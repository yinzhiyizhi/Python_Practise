#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SMTP是发送邮件的协议，Python内置对SMTP的支持，
# 可以发送纯文本邮件、HTML邮件以及带附件的邮件。

# Python对SMTP支持有smtplib和email两个模块，
# email负责构造邮件，smtplib负责发送邮件。

# 首先，我们来构造一个最简单的纯文本邮件：

from email.mime.text import MIMEText
msg=MIMEText('hello, send by Python...','plain','utf-8')
