#-*- coding:utf-8 -*-
import hmac, os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
def create_pwd(date):
    # 获取当前UTC时间
    time_min = date
    # time_min = '2020-04-03'
    # print(time_min)
 
    # K 共享密钥（令牌种子）
    k = "3132333435363738393031323334353637383930"\
        "5232333435363738393031323334353637383930"\
        "6432333435363738393031323334353637383930"\
        "75323334" # 正使用的密钥
 
 
    #string->bytes
    b_k = bytes(k, encoding='utf-8')
    b_m = bytes(time_min, encoding='utf-8')

    #加密算法
    digestmod = "MD5"
    h = hmac.new(b_k, b_m, digestmod)
    # print(h.hexdigest())
 
 
    #将返回的16进制摘要截取6位
    hex_final = str(h.hexdigest())[0:6]
    # print(hex_final)
 
 
    #转为10进制
    final = str(int(hex_final.upper(), 16))[0:6]
    passwd = 'Windit' + final
    # print(passwd)
    # os.system('net user administrator %s'%passwd)
    return passwd


def pwdlist():
    yesterday = (datetime.datetime.now()+datetime.timedelta(-1)).strftime('%Y-%m-%d')
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    tomorrow = (datetime.datetime.now()+datetime.timedelta(1)).strftime('%Y-%m-%d')
    ret = {
        yesterday: create_pwd(yesterday),
        today: create_pwd(today),
        tomorrow: create_pwd(tomorrow),
    }
    pwdfile = os.path.join(BASE_DIR, 'tools','passwd.txt')
    f = open(pwdfile, 'w')
    for key, value in ret.items():
        f.writelines('%s:%s\n' % (key, value))
    f.close()
    print(ret)
    return ret

if __name__ == '__main__':
    pwdlist()
	
