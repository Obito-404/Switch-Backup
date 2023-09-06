
# 🖥️  定时备份华为交换机

一个能自动备份华为交换机的配置的程序。


## 📋 步骤

使用该工具的步骤如下：

1. 修改 `Switch Backup.py`的变量。
```shell
 # 定义SSH连接信息
username = "xxx"
password = "xxx"
# 获取所有交换机的主机名，如用ip改为ip即可
hosts = ["sw%d" % i for i in range(2, 49)]
# 创建备份文件夹
backup_file=r'\\xxx'
```
2. 添加定时运行任务，周备或月备自定。

**⚠️ 说明: 运行时，请先安装对应python依赖。根据自身所需要信息更改脚本里的变量。**

## 🛠️ Requirements

- Python


## 📝 License

本项目采用 MIT 许可，详情请参见 [LICENSE](LICENSE) 文件。