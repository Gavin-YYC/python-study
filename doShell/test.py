# coding=utf-8
import os
import json
import shutil
import paramiko
import time


# JSON文件
JSON_DATA = {
    "name": "大转盘",
    "content": {
        "begin_at": 23456789,
        "end_at": 567890,
        "banner_url": "http://baidu.com",
        "play_count": 4,
        "user_info": {
            "uid": "45936298693",
            "username": "杨友存"
        }
    }
}

# 当前目录
HOME_PATH = './'

# 本地cms_data目录
CMS_DATA_PATH = '/home/work/cms_data'


# 用户信息
USER_INFO = {
    "uid": "125587"
}


# 远程服务器列表
REMOTE_LIST = [
    {
        "host": "192.168.60.59",
        "user": "work",
        "pass": "1qazMKO)",
        "port": "22"
    }, {
        "host": "192.168.60.59",
        "user": "work",
        "pass": "1qazMKO)",
        "port": "22"
    }
]


class CmsModel( object ):

    def __init__( self, remote_list=[] ):
        self.remote_list = remote_list


    # json写入文件
    def save_json_to_file( self, path, data, uid ):
        # 创建临时文件夹
        res = self.createPath( path )
        if not res:
            return None

        # 写入文件
        data_path = os.path.join(path, 'data.' + uid + '.json')
        with open(data_path, 'w') as f:
            f.write(json.dumps( data ))

        return data_path


    # 创建目录
    def createPath( self, path ):
        if not os.path.exists( path ):
            os.makedirs( path )
            return True
        return True


    # 预览
    def preview( self, page_path ):
        # 创建目标文件夹
        target_path = os.path.join(CMS_DATA_PATH, page_path) 
        if not self.createPath( target_path ):
            return False
    
        # 生成临时文件
        temp_path = os.path.join(os.path.abspath( HOME_PATH ), 'data') 
        temp_data_path = self.save_json_to_file( 
            temp_path, 
            JSON_DATA, 
            USER_INFO["uid"]
        )
        if temp_data_path is None:
            return False

        # 将临时文件移动到目标目录下
        os.rename( temp_data_path, target_path + '/data.json' ) 
        return True


    # 发布
    def publish( self, page_path ):
        # 生成临时文件
        temp_path = os.path.join(os.path.abspath( HOME_PATH ), 'data') 
        temp_data_path = self.save_json_to_file( 
            temp_path, 
            JSON_DATA, 
            USER_INFO["uid"]
        )
        if temp_data_path is None:
            return False
    
        # 目标路径
        target_path = os.path.join(CMS_DATA_PATH, page_path)   

        # 文件传送
        res = self.send_file_to_remote( temp_data_path, target_path )

        # 上传成功 or 失败
        if res:
            os.remove( temp_data_path )
            return True
        else:
            return False


    # 建立连接
    def conn_ssh( self, hostname, username, password, port=22 ):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname, port=port, username=username, password=password)
            return ssh
        except Exception as e:
            print e
            return None


    # 发送文件
    # 分多个机器发送
    def send_file_to_remote( self, temp_data_path, target_path ):
        if temp_data_path is None or target_path is None:
            return False
        
        for remote in self.remote_list:
            # 建立连接
            ssh = self.conn_ssh(remote["host"], remote["user"], remote["pass"], remote["port"])

            if ssh is None:
                return False

            # 服务器上创建文件
            stdin, stdout, stderr = ssh.exec_command('mkdir -p ' + target_path)

            # 先备份原有数据
            file_path = target_path + '/data.json'
            file_path_back = file_path + '.' + str(int(time.time()))
            stdin, stdout, stderr = ssh.exec_command('cp ' + file_path + ' ' + file_path_back)

            # 拷贝文件
            sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
            sftp = ssh.open_sftp()
            sftp.put(temp_data_path, file_path)

            # 关闭连接
            ssh.close()
        return True



cms_model = CmsModel( REMOTE_LIST )
# cms_model.preview('yangyoucun/test/gavin')
cms_model.publish('yangyoucun/test/gavin')


