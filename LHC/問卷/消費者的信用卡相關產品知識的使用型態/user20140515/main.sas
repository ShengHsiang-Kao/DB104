/*資料簡介
計畫名稱：消費者的信用卡相關產品知識與使用型態
計畫執行單位：國立政治大學企業管理學系
計畫主持人：別蓮蒂副教授
本資料樣本數303筆*/

/*讀取資料檔及欄位定義*/
data aa;
  infile 'd:\temp\work2\letters\credcard\new\main.txt';
  input #1 id year month day ampm hour1 minute1 hour2 minute2 place sub_id worker
           hour3 minute3 second3 hour4 minute4 second4
           hour5 minute5 second5 hour6 minute6 second6 special family hhmember
        #2 hhhead taipei relate1 relate2 friend1 friend2 income1
           income2 expense1 expense2 s1-s9
        #3 percent borrow1-borrow19 reason1
        #4 hold1-hold7 b_att1-b_att18
        #5 factor1-factor10 beh1-beh6
        #6 k1-k22
        #7 afterb1-afterb11 a_att1-a_att10 afterb12 afterb13;


options nocenter;
/*宣告選項數值說明*/
proc format;
    value ampmf 1='早上'  2='下午'  3='夜間';
    value placef 1='訪員家中'  2='受訪者家中或辦公室'  3='其他';
    value specialf 0='正常'  1='過長或過短';
    value taipeif 1='台北市'  2='台北縣';
    value incomef 999999='未填答';
    value moneyf 1='5,000元以下'  2='5,001-10,000元'
                3='10,001-20,000元'  4='20,001-30,000元'
                5='30,001-50,000元'  6='50,001-75,000元'
                7='75,001-100,000元'  8='100,001-150,000元'
                9='150,001-200,000元'  10='200,001-300,000元'
                11='300,001-500,000元'  12='500,000元以上';
    value factorf 1='第一重要'  2='第二重要'  3='第三重要'
            4='第四重要'  5='第五重要'  6='第六重要'
            7='第七重要'  8='第八重要'  9='第九重要'  0='未選答';
    value percentf 1='0%'  2='0-10%'  3='11-20%'  4='21-40%'
                5='41-60%'  6='61-80%'  7='81-99%'  8='100%';
    value have1f 0='不曾'  1='曾經';
    value have2f 1='目前無'  2='目前有';
    value have3f 0='無'  1='有';
    value borro10f 1='強迫儲蓄'  2='投資理財'  3='借貸、財務融通';
    value reason1f 1='方便'  2='不欠人情'  3='免利息'  4='不用償還'
                5='划算(利息較低)'  6='其他理由';
    value hold5f 1='自行取消'  2='被銀行取消'  3='被正卡持有者取消'
                 0='無被取消之信用卡';
    value hold6f 1='不需要'  2='過度消費'  3='欠款未繳'  9='其他'
                 0='無被取消之信用卡' ;
    value hold7f 0="確認";
    value agreef 1='非常不同意'  2='不同意'  3='普通'  4='同意'  5='非常同意';
    value preferf 1='卡種'  2='發卡銀行'  3='免年費或年費低'
               4='人情'  5='卡面設計'  6='循環信用利息低'
               7='申請贈品'  8='快還發卡'  9='預借現金利息低'
               10='失卡零風險'  11='信用額度'
               12='起息日計算方式有利'  13='特約商店折扣'
               14='服務態度'  15='紅利回饋(或集點贈送)'
               16='道路救援服務'  17='郵購專利'
               18='二十四小時電話服務'  19='理念相同'
               20='方便取得信用卡相關資料及服務'  21='各類保險'
               22='其他' 0='missing value' 99='missing value';
    value yesnof 0='否'  1='是';
    value probf 1='非常有可能'  2='有可能'  3='微乎其微的可能性'  4='絕對不可能';
    value beh 0='本題不適用';
    value beh6f 1='較低'  2='差不多'  3='較高' 4='不知道';
    value after12f 1='過高'  2='稍高'  3='尚可'  4='偏低'  5='極低廉';
    value after13f 1='會避免使用'  2='會更謹慎小心'  3='會考慮增加使用'  4='沒有影響';
    value k1f 0="未選" 1="有選";
    value k9f 1="＄2000以下" 2="＄2001-＄4000" 3="＄4000以上" 4="不知道";
    value k10f 1="對" 2="錯" 3="不知道";
    value k13f 1="＄125" 2="＄150" 3="＄152.08" 4="＄182.5" 5="不知道";
    value k15f 1="會被拒絕使用" 2="會被計入欠款的本金部分，一併計算利息"
               3="完全沒有影響，不需支付任何利息" 4="不知道";
    value k16f 1="入帳日次日" 2="結帳日次日" 3="繳款截止日次日" 4="都一樣" 5="不知道";
    value k17f 1="顧客消費日起" 2="自各筆帳款入帳日起" 3="自當期結帳日起"
               4="繳款截止日次日起" 5="都一樣" 6="不知道";

/*變項說明註解*/
label id='流水編'  year='訪談年'  month='訪談月'  day='訪談日'
      ampm='時段'  hour1='起始時'  minute1='起始分'
      hour2='結束時'  minute2='結束分'  place='地點'
      sub_id='受訪者編號'  worker='訪員編號'
      hour3='回答知識問題起始時'  minute3='回答知識問題起始分'
      second3='回答知識問題起始秒'  hour4='回答知識問題終止時'
      minute4='回答知識問題終止分'  second4='回答知識問題終止秒'
      hour5='說明產品知識起始時'  minute5='說明產品知識起始分'
      second5='說明產品知識起始秒'  hour6='說明產品知識終止時'
      minute6='說明產品知識終止分'  second6='說明產品知識終止秒'
      special='時間過長或過短'
      family='家庭成員人數'  hhmember='共同居住人數'
      hhhead='戶長編號'  taipei='目前居住地'
      relate1='大台北地區親戚人數'  relate2='經常往來親戚人數'
      friend1='大台北地區朋友人數'  friend2='經常往來朋友人數'
      income1='家庭每月可支配所得'  income2='家庭每月可支配所得'
      expense1='家庭每月平均支出'  expense2='家庭每月平均支出'
      s1='家庭主要經濟來源：本人薪資'
      s2='家庭主要經濟來源：配偶薪資'
      s3='家庭主要經濟來源：子女薪資'
      s4='家庭主要經濟來源：父母薪資'
      s5='家庭主要經濟來源：兄弟姐妹薪資'
      s6='家庭主要經濟來源：投資所得'
      s7='家庭主要經濟來源：積蓄及利息'
      s8='家庭主要經濟來源：退休金、保險給付'
      s9='家庭主要經濟來源：其他'
      percent='個人收入佔家庭總收入'
      borrow1='曾向金融機構貸款'  borrow2='向金融機構貸款次數'
      borrow3='目前有向金融機構貸款'  borrow4='曾向親朋好友借貸'
      borrow5='向親朋好友借貸次數'  borrow6='目前有向親朋好友借貸'
      borrow7='曾參加過互助會(標會)'  borrow8='參加互助會次數'
      borrow9='目前有參加互助會'  borrow10='對互助會態度'
      borrow11='急需小額短期融資來源：向家人親戚借貸'
      borrow12='急需小額短期融資來源：向朋友借貸'
      borrow13='急需小額短期融資來源：使用信用卡循環信用'
      borrow14='急需小額短期融資來源：標會'
      borrow15='急需小額短期融資來源：向銀行貸款'
      borrow16='急需小額短期融資來源：向地下錢莊借貸'
      borrow17='急需小額短期融資來源：典當'
      borrow18='急需小額短期融資來源：出售現有資產'
      borrow19='急需小額短期融資來源：其他'
      reason1='第一選擇急需小額短期融資來源的理由'
      hold1='持有信用卡'  hold2='持有信用卡張數'
      hold3='已取消之信用卡'  hold4='已取消之信用卡張數'
      hold5='取消者'  hold6='取消原因'  hold7='非無信用卡者'
      b_att1='信用卡省卻攜帶大量現金'
      b_att2='使用信用卡每月的花費比使用前增加許多'
      b_att3='每月付清信用卡帳單，不使用循環信用'
      b_att4='不曾刷爆信用額度'
      b_att5='信用卡的每月對帳單省去記帳的麻煩'
      b_att6='出國時才使用信用卡'
      b_att7='向來有計劃地使用信用卡'
      b_att8='卡面設計必須代表個性與個人風格'
      b_att9='信用卡增加了衝動購物的可能'
      b_att10='持有信用卡代表了個人的身份地位'
      b_att11='信用卡有重要的財務融通功用'
      b_att12='使用信用卡後物質生活品質提昇許多'
      b_att13='使用信用卡有機會購買一些過去買不起的東西'
      b_att14='信用卡是可有可無的東西'
      b_att15='信用卡是社會的罪惡淵藪之一'
      b_att16='信用卡最大的好處是「先消費，後付款」'
      b_att17='信用卡增加了消費者的物質欲望'
      b_att18='整體而言，信用卡的正面功能大於負面功能'
      factor1='申信用卡時第一重要考慮因素'
      factor2='申信用卡時第二重要考慮因素'
      factor3='申信用卡時第三重要考慮因素'
      factor4='申信用卡時第四重要考慮因素'
      factor5='申信用卡時第五重要考慮因素'
      factor6='申信用卡時第六重要考慮因素'
      factor7='申信用卡時第七重要考慮因素'
      factor8='申信用卡時第八重要考慮因素'
      factor9='申信用卡時第九重要考慮因素'
      factor10='申信用卡時第十重要考慮因素'
      beh1='曾否使用過循環信用'  beh2='使用循環信用原因及未使用原因'
      beh3='現在是否使用循環信用'  beh4='現在使用循環信用原因及未使用原因'
      beh5='將來是否可能使用循環信用'
      beh6='循環信用利息與小額無擔保貸款利息的比較'
      k1='VISA'  k2='MASTER'
      k3='JCB'  k4='大來'
      k5='聯合信用卡'  k6='中國信託'
      k7='花旗銀行'  k8='不知道'
      k9='信用卡普卡年費'  k10='主動調高持卡人的刷卡額度'
      k11='只繳付「最低付款額」及同意使用循環利率繳款'
      k12='各家發卡銀行所訂定的循環利率與起息日皆相同'
      k13='日息萬分之五，所需支付利息金額'  k14='年息18.25%，所需支付利息金額'
      k15='再刷卡新交易'  k16='「先消費，後付款」的期間最長'
      k17='「信用循環起息日」的規定對消費者最有利'
      k18='利息外還得加違約金'
      k19='不應包含年費、預借現金、掛失手續費等'
      k20='掛失後、發卡銀行必須負擔掛失前24小時遭冒用的損失'
      k21='當一張信用卡遭發卡銀行強制終止使用，其他罰卡銀行可不事先通知降低或暫停信用卡之使用'
      k22='信用卡定型化契約範本'
      afterb1='是否考慮再多申請幾張信用卡'
      afterb2='將來是否有可能使用循環信用'
      afterb3='說明後，小額短期融資向家人親戚借貸'
      afterb4='說明後，小額短期融資向朋友借貸'
      afterb5='說明後，小額短期融資則使用信用卡循環信用'
      afterb6='說明後，小額短期融資則標會'
      afterb7='說明後，小額短期融資向銀行貸款'
      afterb8='說明後，小額短期融資向地下錢莊借貸'
      afterb9='說明後，小額短期融資則典當'
      afterb10='說明後，小額短期融資來源會出售現有資產'
      afterb11='說明後，小額短期融資來源：其他'
      a_att1='說明後，信用卡除省卻帶現金麻煩外並無好處'
      a_att2='說明後，信用卡為一種重要的財務融通工具'
      a_att3='說明後，信用卡增加了社會浮華奢靡的風氣'
      a_att4='說明後，信用卡幫助提昇生活品質'
      a_att5='說明後，信用卡是現代生活中不可或缺的東西'
      a_att6='說明後，如教育有計劃使用信用卡則值得推廣'
      a_att7='說明後，擔心在使用信用卡後會增加每月消費'
      a_att8='說明後，聰明消費者會運用先消費後付款功能'
      a_att9='說明後，信用卡增加了消費者的物質欲望'
      a_att10='說明後，認為信用卡的正面功能多於負面功能'
      afterb12='說明後，對信用卡循環信用利率的看法'
      afterb13='說明後，日後使用循環信用的態度與方式';


/*原計畫提供--不執行*/
/* To Calculate Time */
/*anstime=(hour4-hour3)*3600+(minute4-minute3)*60+(second4-second3);
exptime=(hour6-hour5)*3600+(minute6-minute5)*60+(second6-second5);*/

/* To Calculate Number of Relatives */
/*network=sum (of relate2 friend2);*/

/* To Calculate Knowledge Score */
/* answer1=1; answer2=1; answer3=0; answer4=0; answer5=0; answer6=0;
 answer7=0; answer8=0; answer9=1; answer10=1; answer11=1; answer12=2;
 answer13=2; answer14=2; answer15=2; answer16=2; answer17=4; answer18=1;
 answer19=1; answer20=2; answer21=1; answer22=1;
 array k(22) k1-k22;
 array answer(22) answer1-answer22;
 array correct(22) c1-c8 ck2-ck15;
 do i=1 to 22;
   if k(i)=answer(i) then correct(i)=1;
   else correct(i)=0;
 end;
 ck1 = sum (of c1-c8);
 if ck1<8 then ck1=0;
   else if ck1=8 then ck1=1;
 k_score = sum (of ck1-ck15);
 drop answer1-answer22 i; */

/* To Calculate Income and Expenditure */
/* income=income1;
 if income1=999999 then do;
    if income2=01 then income=2500;
    else if income2=02 then income=7500;
    else if income2=03 then income=15000;
    else if income2=04 then income=25000;
    else if income2=05 then income=40000;
    else if income2=06 then income=62500;
    else if income2=07 then income=87500;
    else if income2=08 then income=125000;
    else if income2=09 then income=175000;
    else if income2=10 then income=250000;
    else if income2=11 then income=400000;
    else if income2=12 then income=600000;
    else income=.;
    end;
 expense=expense1;
 if expense1=999999 then do;
    if expense2=01 then expense=2500;
    else if expense2=02 then expense=7500;
    else if expense2=03 then expense=15000;
    else if expense2=04 then expense=25000;
    else if expense2=05 then expense=40000;
    else if expense2=06 then expense=62500;
    else if expense2=07 then expense=87500;
    else if expense2=08 then expense=125000;
    else if expense2=09 then expense=175000;
    else if expense2=10 then expense=250000;
    else if expense2=11 then expense=400000;
    else if expense2=12 then expense=600000;
    else expense=.;
    end;  */

/* To Defind Revolvers */
/* if beh1=1 and (beh2=1 or beh2=2) then revolve3=2;  */        /* revolver */
/*  else if beh1=1 and (beh2=3 or beh2=9) then revolve3=1;*/  /* partial revolver */
/*  else if beh1=0 then revolve3=0;*/                         /* non-revolver */
/*    else revolve3=.;*/
/* if beh1=1 then revolve2=1; */        /* revolver */
/*    else if beh1=0 then revolve2=0;*/   /* non-revolver */
/*    else revolve2=.;  */

/*套用選項數值說明*/
    format ampm ampmf.
           place placef.
           special specialf.
           taipei taipeif.
           income1 expense1 incomef.
           income2 expense2 moneyf.
           s1 s2 s3 s4 s5 s6 s7 s8 s9 borrow11 borrow12 borrow13 borrow14 borrow15
           borrow16 borrow17 borrow18 borrow19 afterb3 afterb4 afterb5 afterb6
           afterb7 afterb8 afterb9 afterb10 afterb11 factorf.
           percent percentf.
           borrow1 borrow4 borrow7 have1f.
           borrow3 borrow6 borrow9 have3f.
           borrow10 borro10f.
           reason1 reason1f.
           hold1 hold3 beh1 beh3 yesnof.
           hold5 hold5f.
           hold6 hold6f.
           hold7 hold7f.
           b_att1 b_att2 b_att3 b_att4 b_att5 b_att6 b_att7 b_att8 b_att9 b_att10
           b_att11 b_att12 b_att13 b_att14 b_att15 b_att16 b_att17 b_att18 a_att1
           a_att2 a_att3 a_att4 a_att5 a_att6 a_att7 a_att8 a_att9 a_att10 agreef.
           factor1 factor2 factor3 factor4 factor5 factor6 factor7 factor8
           factor9 factor10 preferf.
           beh2 beh4 beh.
           beh5 afterb1 afterb2 probf.
           beh6 beh6f.
           afterb12 after12f.
           afterb13 after13f.
           K1 K2 K3 K4 K5 K6 K7 K8 K1f.
           k9 k9f.
           k10 k11 k12 k18 k19 k20 k21 k22 k10f.
           k13 k14 k13f.
           k15 k15f.
           k16 k16f.
           k17 k17f.;

/*執行次數分配*/
proc freq;

run;
