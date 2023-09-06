import os
from datetime import datetime
from netmiko import ConnectHandler
import encodings.idna  # 添加这行
import encodings.utf_8  # 添加这行

# 定义SSH连接信息
username = "xxx"
password = "xxx"

# 获取所有交换机的主机名，如用ip改为ip即可
hosts = ["sw%d" % i for i in range(2, 49)]

# 创建备份文件夹
backup_file=r'\\xxx'
backup_folder = backup_file + datetime.now().strftime("%Y-%m-%d")
os.mkdir(backup_folder)

# 定义备份文件名和保存路径
backup_path = os.path.join(os.getcwd(), backup_folder)

def backup_switch(host):
    try:
        # 创建SSH连接并连接设备
        dev = {
            'device_type': 'huawei',
            'ip': host,
            'username': username,
            'password': password,
        }
        conn = ConnectHandler(**dev)
        conn.enable()

        # 发送命令导出配置到本地
        output = conn.send_command('dis current-configuration')
        file_name =  host + '_conf_bak.txt'
        with open(os.path.join(backup_path, file_name), mode='w', encoding='utf8') as f:
            print('Backing:', host)
            f.write(output)
            print('Backup completed:', file_name)

        # 关闭SSH连接
        conn.disconnect()
    except Exception as e:
        print("Backup fail:%s (%s)" % (host, str(e)))

# 多线程备份
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for host in hosts:
        futures.append(executor.submit(backup_switch, host))

    # 等待所有任务完成
    concurrent.futures.wait(futures)
