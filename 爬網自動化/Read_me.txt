指令執行corontab -e 可以執行排成：
  方式為：* * * * * bash /user/path/scrawler.sh

會遇到的狀況：
  1.permission denine
    解決方式：開權限chmod 777 /user/path/scrawler.sh
  2.no shuch path
    解決方式：* * * * * bash /user/path/scrawler.sh 確定加bash(網路上有些例子不加bash)
  3.no modul ....example no module requests:
    解決方式：
      1.pip install module
      2.如果還不行確定是否同一個python (使用whitch python指令)
      3.改shell執行python路徑... example(/user/path/annaconda3/python /user/path/scrawler01.py)
