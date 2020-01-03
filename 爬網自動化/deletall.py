from hdfs import *
client = Client("http://namenode:9870",root="/",timeout=100,session=False)

client.delete('/user/hdfs/news/udn.csv')
client.delete('/user/hdfs/news/UdnNsignal.txt')
client.delete('/user/hdfs/news/Nsignal.txt')
client.delete('/user/hdfs/news/ptt.csv')
client.delete('/user/hdfs/news/ENsignal.txt')
client.delete('/user/hdfs/news/Etoday.csv')

print(done)
