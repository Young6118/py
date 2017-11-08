import socket

s = socket.socket()

host = 'blog.youngchou.cn'
port = 80

# 参数是一个元组
# 建立一个 tcp ipv4 连接
s.connect((host, port))

# 本机的 ip 和 端口 元组
print(s.getsockname())
ip, port = s.getsockname()
print('本机 ip 和使用的 port 为： %s %d' % (ip ,port))
print('本机 ip 和使用的 port 为： {} {}'.format(ip, port))

# 构造一个 HTTP 请求
http_request = 'GET / HTTp/1.1\r\nhost:{}\r\n\r\n'.format(host)
request = http_request.encode('utf-8')
print('查看请求', request, type(request))

# 发送请求
s.send(request)

# 接收响应
response = s.recv(1024*1024)

# 输出响应参数 bytes 类型
print('响应',response)
# bytes 转为 string后输出
print('响应的 str 格式', response.decode('utf-8'))







