### 搭建wukong-robot

- 这里讲述如何在云主机上搭建
```
# 参考https://github.com/wzpan/wukong-robot
# 下载docker image
docker pull wzpan/wukong-robot:latest

# 不带声卡启动，如果启动后监听在ipv6地址，可以替换localhost为你所在机器的IP地址
docker run -itv /home/gyw/:/var/gyw/ -p locahost:5000:5000 wzpan/wukong-robot:latest # 不启动声卡支持

# pull到最新代码
cd ~/wukong-robot
git pull

# 配置文件在/root/.wukong/config.yml
```

### wukong-itchat搭建

- 启动wukong-robot
```
# 可选使用nohup启动
nohup ... &
```
- 下载wukong-itchat
```
git clone https://github.com/wzpan/wukong-itchat.git
cd wukong-itchat
pip3 install -r requirements.txt
```
- 启动wukong-itchat
```
python3 bot.py
```
