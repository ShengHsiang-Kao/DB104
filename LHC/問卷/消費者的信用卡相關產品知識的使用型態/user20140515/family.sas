/*���²��
�p�e�W�١G���O�̪��H�Υd�������~�Φ��P�ϥΫ��A
�p�e������G��߬F�v�j�ǥ��~�޲z�Ǩt
�p�e�D���H�G�O�����Ʊб�
����Ƽ˥��ơG303��*/

options nocenter ;

/*Ū������ɤ����w�q*/
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


/*�ŧi�ﶵ�ƭ�*/
proc format;
    value $rf '0'='�ۤv'
              '1'='����'
              '2'='�t��'
              '3'='�l�k'
              '4'='�S�̩j�f�B�A�B�s��'
              '5'='������'
              '6'='���B�B�B�h�B��'
              '7'='��B��S�̩j�f'
              '8'='�]�l�k'
              '9'='�L���H'
              'a'='��L'
              'b'='���l�k'
              '.'='missing value';
    value sexf 1='�k'
               2='�k';
    value eduf 1='�����Ш|'
               2='���X��'
               3='�p��'
               4='�ꤤ�B�줤'
               5='�����B��¾'
               6='���M'
               7='�T�M�B�G�M'
               8='�j��'
               9='��s�ҤΥH�W';
    value $edu_f '0'='�P�����Ƿ~�L��'
                 'a'='�b��'
                 'b'='�w�~'
                 'c'='���~'
                 '.'='missing value';
    value marryf 1='�w�B'
                 2='�P�~'
                 3='���~'
                 4='���B'
                 5='�స'
                 6='�q�����B';
    value jobf 01='���h�޲z'
               02='���h�޲z'
               03='�C���D��'
               04='��L��¾��'
               05='�M�~�H��'
               06='���p���~�t�d�H'
               07='����Ӯa�Ω��E���t�d�H�B�}��'
               08='�x�H'
               09='�u�H'
               10='�Юv'
               11='�ۥѷ~'
               12='�a��'
               13='�ǥ�'
               14='�ȵL�u�@�B�Ȯɥ��~��'
               15='�h��'
               16='���A�ΡA����Ϋĵ�'
               17='�A'
               18='��L'
               88='missing value'
               99='�L���H';
value $job_f '01'='���h�޲z'
             '02'='���h�޲z'
             '03'='�C���D��'
             '04'='��L��¾��'
             '05'='�M�~�H��'
             '06'='���p���~�t�d�H'
             '07'='����Ӯa�Ω��E���t�d�H�B�}��'
             '08'='�x�H'
             '09'='�u�H'
             '10'='�Юv'
             '11'='�ۥѷ~'
             '12'='�a��'
             '13'='�ǥ�'
             '14'='�ȵL�u�@�B�Ȯɥ��~��'
             '15'='�h��'
             '16'='���A�ΡA����Ϋĵ�'
             '17'='�A'
             '18'='��L'
             '77'='missing value'
             '00'='�Юv����ұмh��'
             'aa'='�Х��X��'
             'bb'='�Фp��'
             'cc'='�аꤤ'
             'dd'='�а���'
             'ee'='�бM��'
             'ff'='�Фj��'
             'gg'='�иɲ߯Z';
    value outf 999999='����';
    value out_f 0='�C��T�wú�浹�a�H'
                1='�C��T�w�ۮa�H��o�����ػP';

    value livef 0='�_' 1='�O' 9='�L���H';


/*�ܶ�����*/
label id='�y���s'
      fmid1='�a�x�����N�X'
      fmid2='�a�x�����N�X'
      fmid3='�a�x�����N�X'
      fmid4='�a�x�����N�X'
      fmid5='�a�x�����N�X'
      fmid6='�a�x�����N�X'
      fmid7='�a�x�����N�X'
      fmid8='�a�x�����N�X'
      fmid9='�a�x�����N�X'
      fmid10='�a�x�����N�X'
      r1='���Y'
      r2='���Y'
      r3='���Y'
      r4='���Y'
      r5='���Y'
      r6='���Y'
      r7='���Y'
      r8='���Y'
      r9='���Y'
      r10='���Y'
      sex1='�ʧO'
      sex2='�ʧO'
      sex3='�ʧO'
      sex4='�ʧO'
      sex5='�ʧO'
      sex6='�ʧO'
      sex7='�ʧO'
      sex8='�ʧO'
      sex9='�ʧO'
      sex10='�ʧO'
      year1='�X�ͦ~'
      year2='�X�ͦ~'
      year3='�X�ͦ~'
      year4='�X�ͦ~'
      year5='�X�ͦ~'
      year6='�X�ͦ~'
      year7='�X�ͦ~'
      year8='�X�ͦ~'
      year9='�X�ͦ~'
      year10='�X�ͦ~'
      month1='�X�ͤ�'
      month2='�X�ͤ�'
      month3='�X�ͤ�'
      month4='�X�ͤ�'
      month5='�X�ͤ�'
      month6='�X�ͤ�'
      month7='�X�ͤ�'
      month8='�X�ͤ�'
      month9='�X�ͤ�'
      month10='�X�ͤ�'
      day1='�X�ͤ�'
      day2='�X�ͤ�'
      day3='�X�ͤ�'
      day4='�X�ͤ�'
      day5='�X�ͤ�'
      day6='�X�ͤ�'
      day7='�X�ͤ�'
      day8='�X�ͤ�'
      day9='�X�ͤ�'
      day10='�X�ͤ�'
      edu1='�Ш|�{��'
      edu2='�Ш|�{��'
      edu3='�Ш|�{��'
      edu4='�Ш|�{��'
      edu5='�Ш|�{��'
      edu6='�Ш|�{��'
      edu7='�Ш|�{��'
      edu8='�Ш|�{��'
      edu9='�Ш|�{��'
      edu10='�Ш|�{��'
      edu_1='����'
      edu_2='����'
      edu_3='����'
      edu_4='����'
      edu_5='����'
      edu_6='����'
      edu_7='����'
      edu_8='����'
      edu_9='����'
      edu_10='����'
      marry1='�B�ê��p'
      marry2='�B�ê��p'
      marry3='�B�ê��p'
      marry4='�B�ê��p'
      marry5='�B�ê��p'
      marry6='�B�ê��p'
      marry7='�B�ê��p'
      marry8='�B�ê��p'
      marry9='�B�ê��p'
      marry10='�B�ê��p'
      job1='¾�~'
      job2='¾�~'
      job3='¾�~'
      job4='¾�~'
      job5='¾�~'
      job6='¾�~'
      job7='¾�~'
      job8='¾�~'
      job9='¾�~'
      job10='¾�~'
      job_1='�h��e¾�~'
      job_2='�h��e¾�~'
      job_3='�h��e¾�~'
      job_4='�h��e¾�~'
      job_5='�h��e¾�~'
      job_6='�h��e¾�~'
      job_7='�h��e¾�~'
      job_8='�h��e¾�~'
      job_9='�h��e¾�~'
      job_10='�h��e¾�~'
      in1='�C���~��'
      in2='�C���~��'
      in3='�C���~��'
      in4='�C���~��'
      in5='�C���~��'
      in6='�C���~��'
      in7='�C���~��'
      in8='�C���~��'
      in9='�C���~��'
      in10='�C���~��'
      out_1='�i�X'
      out_2='�i�X'
      out_3='�i�X'
      out_4='�i�X'
      out_5='�i�X'
      out_6='�i�X'
      out_7='�i�X'
      out_8='�i�X'
      out_9='�i�X'
      out_10='�i�X'
      out1='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out2='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out3='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out4='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out5='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out6='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out7='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out8='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out9='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      out10='�C��椩�a�H�Φۮa�H�B��o�ػP���B'
      live1='�P��@�B'
      live2='�P��@�B'
      live3='�P��@�B'
      live4='�P��@�B'
      live5='�P��@�B'
      live6='�P��@�B'
      live7='�P��@�B'
      live8='�P��@�B'
      live9='�P��@�B'
      live10='�P��@�B';

/*�ŧi�򥢭�*/
 array edu(10) edu1-edu10;
 array marry(10) marry1-marry10;
 array job(10) job1-job10;
 array job_(10) job_1-job_10;
  do i=1 to 10;
    if edu(i)=9 and marry(i)=9 then edu(i)=.;
    if job(i)<>99 and job_(i)='99' then job_(i)='77';
 end;

/*��p�e���Ѥ��p��{��--������*/

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

/*��p�e���Ѥ�����*/
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

/*��p�e���Ѥ�����*/
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

/*��p�e���Ѥ�����*/
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

/*��p�e���Ѥ�����*/
/*To Calculate ���X�̦~�֤��G*/
/*if age1<=20 then agegroup=1;
   else if age1>20 and age1<=30 then agegroup=2;
   else if age1>30 and age1<=40 then agegroup=3;
   else if age1>40 and age1<=50 then agegroup=4;
   else if age1>50 then agegroup=5; */


/*�M�οﶵ�ƭȻ���*/
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

/*���榸�Ƥ��t*/
proc freq;
run;
