### �wukong-robot

- ���ｲ��������������ϴ
```
# �ο�https://github.com/wzpan/wukong-robot
# ����docker image
docker pull wzpan/wukong-robot:latest

# ����������������������������ipv6��ַ�������滻localhostΪ�����ڻ�����IP��ַ
docker run -itv /home/gyw/:/var/gyw/ -p locahost:5000:5000 wzpan/wukong-robot:latest # ����������֧��

# pull�����´���
cd ~/wukong-robot
git pull

# �����ļ���/root/.wukong/config.yml
```

### wukong-itchat�

- ����wukong-robot
```
# ��ѡʹ��nohup����
nohup ... &
```
- ����wukong-itchat
```
git clone https://github.com/wzpan/wukong-itchat.git
cd wukong-itchat
pip3 install -r requirements.txt
```
- ����wukong-itchat
```
python3 bot.py
```
