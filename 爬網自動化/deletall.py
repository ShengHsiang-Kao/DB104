from hdfs import *
client.delete('/user/hdfs/news/udn.csv')
client.delete('/user/hdfs/news/UdnNsignal.txt')
client.delete('/user/hdfs/news/Nsignal.txt')
client.delete('/user/hdfs/news/ptt.csv')
client.delete('/user/hdfs/news/ENsignal.txt')
client.delete('/user/hdfs/news/Etoday.csv')

print(done)