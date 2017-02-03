# coding=utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr( s ):
    name,addr = parseaddr( s )
    return formataddr((\
            Header(name, 'utf-8').encode(),\
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# 输入Email地址和口令
from_addr = 'yangyoucun@lsh123.com'
password  = 'sq_qzj521'

# 输入SMTP服务器地址
smtp_server = 'smtp.qiye.163.com'

# 输入收件人地址
to_addr = 'yangyoucun@lsh123.com'

msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者,{0}'.format(from_addr))
msg['To'] = _format_addr('管理员：{0}'.format(to_addr))
msg['Subject'] = Header('来自SMTP的问候.....', 'utf-8').encode()

server = smtplib.SMTP( smtp_server, 25 ) # smtp协议的默认端口号是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
