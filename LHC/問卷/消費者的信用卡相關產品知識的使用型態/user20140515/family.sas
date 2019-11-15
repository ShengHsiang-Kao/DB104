/*資料簡介
計畫名稱：消費者的信用卡相關產品形式與使用型態
計畫執行單位：國立政治大學企業管理學系
計畫主持人：別蓮蒂副教授
本資料樣本數：303筆*/

options nocenter ;

/*讀取資料檔及欄位定義*/
data bb;
  infile 'd:\temp\work2\letters\credcard\new\family.txt';
  input #1 id
        #2 fmid1 r1 $  sex1 year1 month1 day1 edu1 edu_1 $ marry1 job1 job_1 $ in1 out_1 out1 live1
        #3 fmid2 r2 $ sex2 year2 month2 day2 edu2 edu_2 $ marry2 job2 job_2 $ in2 out_2 out2 live2
        #4 fmid3 r3 $ sex3 year3 month3 day3 edu3 edu_3 $ marry3 job3 job_3 $ in3 out_3 out3 live3
        #5 fmid4 r4 $ sex4 year4 month4 day4 edu4 edu_4 $ marry4 job4 job_4 $ in4 out_4 out4 live4
        #6 fmid5 r5 $ sex5 year5 month5 day5 edu5 edu_5 $ marry5 job5 job_5 $ in5 out_5 out5 live5
        #7 fmid6 r6 $ sex6 year6 month6 day6 edu6 edu_6 $ marry6 job6 job_6 $ in6 out_6 out6 live6
        #8 fmid7 r7 $ sex7 year7 month7 day7 edu7 edu_7 $ marry7 job7 job_7 $ in7 out_7 out7 live7
        #9 fmid8 r8 $ sex8 year8 month8 day8 edu8 edu_8 $ marry8 job8 job_8 $ in8 out_8 out8 live8
        #10 fmid9 r9 $ sex9 year9 month9 day9 edu9 edu_9 $ marry9 job9 job_9 $ in9 out_9 out9 live9
        #11 fmid10 r10 $ sex10 year10 month10 day10 edu10 edu_10 $ marry10 job10 job_10 $ in10 out_10 out10 live10;


/*宣告選項數值*/
proc format;
    value $rf '0'='自己'
              '1'='父母'
              '2'='配偶'
              '3'='子女'
              '4'='兄弟姐妹、嫂、連襟'
              '5'='祖父母'
              '6'='叔、伯、姑、姨'
              '7'='堂、表兄弟姐妹'
              '8'='孫子女'
              '9'='無此人'
              'a'='其他'
              'b'='姪子女'
              '.'='missing value';
    value sexf 1='男'
               2='女';
    value eduf 1='未受教育'
               2='幼稚園'
               3='小學'
               4='國中、初中'
               5='高中、高職'
               6='五專'
               7='三專、二專'
               8='大學'
               9='研究所及以上';
    value $edu_f '0'='與完成學業無關'
                 'a'='在學'
                 'b'='肄業'
                 'c'='畢業'
                 '.'='missing value';
    value marryf 1='已婚'
                 2='同居'
                 3='分居'
                 4='離婚'
                 5='喪偶'
                 6='從未結婚';
    value jobf 01='高層管理'
               02='中層管理'
               03='低階主管'
               04='其他類職員'
               05='專業人員'
               06='中小企業負責人'
               07='自營商家或店舖之負責人、開店'
               08='軍人'
               09='工人'
               10='教師'
               11='自由業'
               12='家管'
               13='學生'
               14='暫無工作、暫時失業中'
               15='退休'
               16='不適用，嬰兒或孩童'
               17='農'
               18='其他'
               88='missing value'
               99='無此人';
value $job_f '01'='高層管理'
             '02'='中層管理'
             '03'='低階主管'
             '04'='其他類職員'
             '05'='專業人員'
             '06'='中小企業負責人'
             '07'='自營商家或店舖之負責人、開店'
             '08'='軍人'
             '09'='工人'
             '10'='教師'
             '11'='自由業'
             '12'='家管'
             '13'='學生'
             '14'='暫無工作、暫時失業中'
             '15'='退休'
             '16'='不適用，嬰兒或孩童'
             '17'='農'
             '18'='其他'
             '77'='missing value'
             '00'='教師未填所教層級'
             'aa'='教幼稚園'
             'bb'='教小學'
             'cc'='教國中'
             'dd'='教高中'
             'ee'='教專科'
             'ff'='教大學'
             'gg'='教補習班';
    value outf 999999='未填答';
    value out_f 0='每月固定繳交給家人'
                1='每月固定自家人獲得金錢贈與';

    value livef 0='否' 1='是' 9='無此人';


/*變項註解*/
label id='流水編'
      fmid1='家庭成員代碼'
      fmid2='家庭成員代碼'
      fmid3='家庭成員代碼'
      fmid4='家庭成員代碼'
      fmid5='家庭成員代碼'
      fmid6='家庭成員代碼'
      fmid7='家庭成員代碼'
      fmid8='家庭成員代碼'
      fmid9='家庭成員代碼'
      fmid10='家庭成員代碼'
      r1='關係'
      r2='關係'
      r3='關係'
      r4='關係'
      r5='關係'
      r6='關係'
      r7='關係'
      r8='關係'
      r9='關係'
      r10='關係'
      sex1='性別'
      sex2='性別'
      sex3='性別'
      sex4='性別'
      sex5='性別'
      sex6='性別'
      sex7='性別'
      sex8='性別'
      sex9='性別'
      sex10='性別'
      year1='出生年'
      year2='出生年'
      year3='出生年'
      year4='出生年'
      year5='出生年'
      year6='出生年'
      year7='出生年'
      year8='出生年'
      year9='出生年'
      year10='出生年'
      month1='出生月'
      month2='出生月'
      month3='出生月'
      month4='出生月'
      month5='出生月'
      month6='出生月'
      month7='出生月'
      month8='出生月'
      month9='出生月'
      month10='出生月'
      day1='出生日'
      day2='出生日'
      day3='出生日'
      day4='出生日'
      day5='出生日'
      day6='出生日'
      day7='出生日'
      day8='出生日'
      day9='出生日'
      day10='出生日'
      edu1='教育程度'
      edu2='教育程度'
      edu3='教育程度'
      edu4='教育程度'
      edu5='教育程度'
      edu6='教育程度'
      edu7='教育程度'
      edu8='教育程度'
      edu9='教育程度'
      edu10='教育程度'
      edu_1='完成'
      edu_2='完成'
      edu_3='完成'
      edu_4='完成'
      edu_5='完成'
      edu_6='完成'
      edu_7='完成'
      edu_8='完成'
      edu_9='完成'
      edu_10='完成'
      marry1='婚姻狀況'
      marry2='婚姻狀況'
      marry3='婚姻狀況'
      marry4='婚姻狀況'
      marry5='婚姻狀況'
      marry6='婚姻狀況'
      marry7='婚姻狀況'
      marry8='婚姻狀況'
      marry9='婚姻狀況'
      marry10='婚姻狀況'
      job1='職業'
      job2='職業'
      job3='職業'
      job4='職業'
      job5='職業'
      job6='職業'
      job7='職業'
      job8='職業'
      job9='職業'
      job10='職業'
      job_1='退休前職業'
      job_2='退休前職業'
      job_3='退休前職業'
      job_4='退休前職業'
      job_5='退休前職業'
      job_6='退休前職業'
      job_7='退休前職業'
      job_8='退休前職業'
      job_9='退休前職業'
      job_10='退休前職業'
      in1='每月薪資'
      in2='每月薪資'
      in3='每月薪資'
      in4='每月薪資'
      in5='每月薪資'
      in6='每月薪資'
      in7='每月薪資'
      in8='每月薪資'
      in9='每月薪資'
      in10='每月薪資'
      out_1='進出'
      out_2='進出'
      out_3='進出'
      out_4='進出'
      out_5='進出'
      out_6='進出'
      out_7='進出'
      out_8='進出'
      out_9='進出'
      out_10='進出'
      out1='每月交予家人或自家人處獲得贈與金額'
      out2='每月交予家人或自家人處獲得贈與金額'
      out3='每月交予家人或自家人處獲得贈與金額'
      out4='每月交予家人或自家人處獲得贈與金額'
      out5='每月交予家人或自家人處獲得贈與金額'
      out6='每月交予家人或自家人處獲得贈與金額'
      out7='每月交予家人或自家人處獲得贈與金額'
      out8='每月交予家人或自家人處獲得贈與金額'
      out9='每月交予家人或自家人處獲得贈與金額'
      out10='每月交予家人或自家人處獲得贈與金額'
      live1='同住一處'
      live2='同住一處'
      live3='同住一處'
      live4='同住一處'
      live5='同住一處'
      live6='同住一處'
      live7='同住一處'
      live8='同住一處'
      live9='同住一處'
      live10='同住一處';

/*宣告遺失值*/
 array edu(10) edu1-edu10;
 array marry(10) marry1-marry10;
 array job(10) job1-job10;
 array job_(10) job_1-job_10;
  do i=1 to 10;
    if edu(i)=9 and marry(i)=9 then edu(i)=.;
    if job(i)<>99 and job_(i)='99' then job_(i)='77';
 end;

/*原計畫提供之計算程式--不執行*/

/* To Group Marital Status */
/*    if marry(i)=1 or marry(i)=2 then marry(i)=2;
       else if marry(i)>=3 and marry(i)<=6 then marry(i)=1; */

/* To Group Occupations */
/*    if job(i)=1 or job(i)=2 or job(i)=5 or job(i)=6 or job(i)=7 or (job(i)=10 and job_(i)='ff')
       then job(i)=2;
       else if (job(i)>=13 and job(i)<=16) or job(i)=8 then job(i)=0;
       else if job(i)=3 or job(i)=4 or job(i)=88 or job(i)=9 or job(i)=10
            or job(i)=11 or job(i)=12 or job(i)=17 or job(i)=18 then job(i)=1;
       else if job(i)=99 then job(i)=.;
   end;*/

 i=1;
 array miss9(*) sex2-sex10 marry2-marry10 out_2-out_10 live2-live10;
  do i=1 to dim(miss9);
    if miss9(i)=9 then miss9(i)=.;
  end;
 i=1;
 array miss99(*) year2-year10 month2-month10 day2-day10;
  do i=1 to dim(miss99);
    if miss99(i)=99 then miss99(i)=.;
  end;
 i=1;
 array miss999(*) in2-in10 out2-out10;
  do i=1 to dim(miss999);
    if miss999(i)=999999 then miss999(i)=.;
  end;
 i=1;
 array miss9999(*) r2-r10 edu_2-edu_10 job_2-job_10;
  do i=1 to dim(miss9999);
    if miss9999(i)='9' or miss9999(i)='99' then miss9999(i)='.';
  end;

/*原計畫提供不執行*/
/* To Calculate Age, Dependents, Children Number */
/* i=1; depend=0; children=0;
 array y(*) year1-year10;
 array m(*) month1-month10;
 array d(*) day1-day10;
 array in(*) in1-in10;
 array live(*) live1-live10;
 array age(*) age1-age10;
  do i=1 to 10;
    age(i)=(98-y(i))+(7-m(i))/12+(31-d(i))/365;
    if in(i)=0 and live(i)=1 then depend=depend+1;
    if age(i)<=18 and age(i)>=0 and in(i)=0 then children=children+1;
  end;*/

/*原計畫提供不執行*/
/* To Calculate Educational Years */
/* array edu_(*) edu_1-edu_10;
 array eduyear(*) eduyr1-eduyr10;
  do i=1 to 10;
    if edu(i)=1 then eduyear(i)=0;
       else if edu(i)=2 then eduyear(i)=1;
       else if edu(i)=3 and (edu_(i)='a' or edu_(i)='b') then eduyear(i)=4;
       else if edu(i)=3 and edu_(i)='c' then eduyear(i)=6;
       else if edu(i)=4 and (edu_(i)='a' or edu_(i)='b') then eduyear(i)=7.5;
       else if edu(i)=4 and edu_(i)='c' then eduyear(i)=9;
       else if edu(i)=5 and (edu_(i)='a' or edu_(i)='b') then eduyear(i)=10.5;
       else if edu(i)=5 and edu_(i)='c' then eduyear(i)=12;
       else if edu(i)=6 and (edu_(i)='a' or edu_(i)='b') then eduyear(i)=13;
       else if edu(i)=6 and edu_(i)='c' then eduyear(i)=14;
       else if edu(i)=7 and (edu_(i)='a' or edu_(i)='b') then eduyear(i)=14;
       else if edu(i)=7 and edu_(i)='c' then eduyear(i)=15;
       else if edu(i)=8 and (edu_(i)='a' or edu_(i)='b') then eduyear(i)=14;
       else if edu(i)=8 and edu_(i)='c' then eduyear(i)=16;
       else if edu(i)=9 and (edu_(i)='a' or edu_(i)='b') then eduyear(i)=17;
       else if edu(i)=9 and edu_(i)='c' then eduyear(i)=18;
  end;*/

/*原計畫提供不執行*/
/* To Identify Family Structure */
/* array r(9) r2-r10;
  do i=1 to 9;
    if r(i)='1' then l1=1;
    if r(i)='3' then l2=1;
    if r(i)='5' then l3=1;
    if r(i)='8' then l4=1;
  end;
 i=1;
 level=sum (of i, l1, l2, l3, l4);

drop i year1-year10 month1-month10 day1-day10 live1-live10 l1-l4;*/

/*原計畫提供不執行*/
/*To Calculate 受訪者年齡分佈*/
/*if age1<=20 then agegroup=1;
   else if age1>20 and age1<=30 then agegroup=2;
   else if age1>30 and age1<=40 then agegroup=3;
   else if age1>40 and age1<=50 then agegroup=4;
   else if age1>50 then agegroup=5; */


/*套用選項數值說明*/
    format r1-r10 $rf.
           sex1-sex10 sexf.
           edu1-edu10 eduf.
           edu_1-edu_10 $edu_f.
           marry1-marry10 marryf.
           job1-job10 jobf.
           job_1-job_10 $job_f.
           out_1-out_10 out_f.
           out1-out10 outf.
           live1-live10 livef.;;

/*執行次數分配*/
proc freq;
run;
