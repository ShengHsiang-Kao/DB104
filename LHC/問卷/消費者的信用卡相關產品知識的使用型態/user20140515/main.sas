/*���²��
�p�e�W�١G���O�̪��H�Υd�������~���ѻP�ϥΫ��A
�p�e������G��߬F�v�j�ǥ��~�޲z�Ǩt
�p�e�D���H�G�O�����Ʊб�
����Ƽ˥���303��*/

/*Ū������ɤ����w�q*/
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
/*�ŧi�ﶵ�ƭȻ���*/
proc format;
    value ampmf 1='���W'  2='�U��'  3='�]��';
    value placef 1='�X���a��'  2='���X�̮a���ο줽��'  3='��L';
    value specialf 0='���`'  1='�L���ιL�u';
    value taipeif 1='�x�_��'  2='�x�_��';
    value incomef 999999='����';
    value moneyf 1='5,000���H�U'  2='5,001-10,000��'
                3='10,001-20,000��'  4='20,001-30,000��'
                5='30,001-50,000��'  6='50,001-75,000��'
                7='75,001-100,000��'  8='100,001-150,000��'
                9='150,001-200,000��'  10='200,001-300,000��'
                11='300,001-500,000��'  12='500,000���H�W';
    value factorf 1='�Ĥ@���n'  2='�ĤG���n'  3='�ĤT���n'
            4='�ĥ|���n'  5='�Ĥ����n'  6='�Ĥ����n'
            7='�ĤC���n'  8='�ĤK���n'  9='�ĤE���n'  0='���ﵪ';
    value percentf 1='0%'  2='0-10%'  3='11-20%'  4='21-40%'
                5='41-60%'  6='61-80%'  7='81-99%'  8='100%';
    value have1f 0='����'  1='���g';
    value have2f 1='�ثe�L'  2='�ثe��';
    value have3f 0='�L'  1='��';
    value borro10f 1='�j���x�W'  2='���z�]'  3='�ɶU�B�]�ȿĳq';
    value reason1f 1='��K'  2='����H��'  3='�K�Q��'  4='�����v��'
                5='�E��(�Q�����C)'  6='��L�z��';
    value hold5f 1='�ۦ����'  2='�Q�Ȧ����'  3='�Q���d�����̨���'
                 0='�L�Q�������H�Υd';
    value hold6f 1='���ݭn'  2='�L�׮��O'  3='��ڥ�ú'  9='��L'
                 0='�L�Q�������H�Υd' ;
    value hold7f 0="�T�{";
    value agreef 1='�D�`���P�N'  2='���P�N'  3='���q'  4='�P�N'  5='�D�`�P�N';
    value preferf 1='�d��'  2='�o�d�Ȧ�'  3='�K�~�O�Φ~�O�C'
               4='�H��'  5='�d���]�p'  6='�`���H�ΧQ���C'
               7='�ӽ��ث~'  8='���ٵo�d'  9='�w�ɲ{���Q���C'
               10='���d�s���I'  11='�H���B��'
               12='�_����p��覡���Q'  13='�S���ө��馩'
               14='�A�ȺA��'  15='���Q�^�X(�ζ��I�ذe)'
               16='�D���ϴ��A��'  17='�l�ʱM�Q'
               18='�G�Q�|�p�ɹq�ܪA��'  19='�z���ۦP'
               20='��K���o�H�Υd������ƤΪA��'  21='�U���O�I'
               22='��L' 0='missing value' 99='missing value';
    value yesnof 0='�_'  1='�O';
    value probf 1='�D�`���i��'  2='���i��'  3='�L�G��L���i���'  4='���藍�i��';
    value beh 0='���D���A��';
    value beh6f 1='���C'  2='�t���h'  3='����' 4='�����D';
    value after12f 1='�L��'  2='�y��'  3='�|�i'  4='���C'  5='���C�G';
    value after13f 1='�|�קK�ϥ�'  2='�|���ԷV�p��'  3='�|�Ҽ{�W�[�ϥ�'  4='�S���v�T';
    value k1f 0="����" 1="����";
    value k9f 1="�C2000�H�U" 2="�C2001-�C4000" 3="�C4000�H�W" 4="�����D";
    value k10f 1="��" 2="��" 3="�����D";
    value k13f 1="�C125" 2="�C150" 3="�C152.08" 4="�C182.5" 5="�����D";
    value k15f 1="�|�Q�ڵ��ϥ�" 2="�|�Q�p�J��ڪ����������A�@�֭p��Q��"
               3="�����S���v�T�A���ݤ�I����Q��" 4="�����D";
    value k16f 1="�J�b�馸��" 2="���b�馸��" 3="ú�ںI��馸��" 4="���@��" 5="�����D";
    value k17f 1="�U�Ȯ��O��_" 2="�ۦU���b�ڤJ�b��_" 3="�۷�����b��_"
               4="ú�ںI��馸��_" 5="���@��" 6="�����D";

/*�ܶ���������*/
label id='�y���s'  year='�X�ͦ~'  month='�X�ͤ�'  day='�X�ͤ�'
      ampm='�ɬq'  hour1='�_�l��'  minute1='�_�l��'
      hour2='������'  minute2='������'  place='�a�I'
      sub_id='���X�̽s��'  worker='�X���s��'
      hour3='�^�����Ѱ��D�_�l��'  minute3='�^�����Ѱ��D�_�l��'
      second3='�^�����Ѱ��D�_�l��'  hour4='�^�����Ѱ��D�פ��'
      minute4='�^�����Ѱ��D�פ��'  second4='�^�����Ѱ��D�פ��'
      hour5='�������~���Ѱ_�l��'  minute5='�������~���Ѱ_�l��'
      second5='�������~���Ѱ_�l��'  hour6='�������~���Ѳפ��'
      minute6='�������~���Ѳפ��'  second6='�������~���Ѳפ��'
      special='�ɶ��L���ιL�u'
      family='�a�x�����H��'  hhmember='�@�P�~��H��'
      hhhead='����s��'  taipei='�ثe�~��a'
      relate1='�j�x�_�a�Ͽ˱��H��'  relate2='�g�`���ӿ˱��H��'
      friend1='�j�x�_�a�ϪB�ͤH��'  friend2='�g�`���ӪB�ͤH��'
      income1='�a�x�C��i��t�ұo'  income2='�a�x�C��i��t�ұo'
      expense1='�a�x�C�륭����X'  expense2='�a�x�C�륭����X'
      s1='�a�x�D�n�g�٨ӷ��G���H�~��'
      s2='�a�x�D�n�g�٨ӷ��G�t���~��'
      s3='�a�x�D�n�g�٨ӷ��G�l�k�~��'
      s4='�a�x�D�n�g�٨ӷ��G�����~��'
      s5='�a�x�D�n�g�٨ӷ��G�S�̩j�f�~��'
      s6='�a�x�D�n�g�٨ӷ��G���ұo'
      s7='�a�x�D�n�g�٨ӷ��G�n�W�ΧQ��'
      s8='�a�x�D�n�g�٨ӷ��G�h����B�O�I���I'
      s9='�a�x�D�n�g�٨ӷ��G��L'
      percent='�ӤH���J���a�x�`���J'
      borrow1='���V���ľ��c�U��'  borrow2='�V���ľ��c�U�ڦ���'
      borrow3='�ثe���V���ľ��c�U��'  borrow4='���V�˪B�n�ͭɶU'
      borrow5='�V�˪B�n�ͭɶU����'  borrow6='�ثe���V�˪B�n�ͭɶU'
      borrow7='���ѥ[�L���U�|(�з|)'  borrow8='�ѥ[���U�|����'
      borrow9='�ثe���ѥ[���U�|'  borrow10='�郎�U�|�A��'
      borrow11='��ݤp�B�u���ĸ�ӷ��G�V�a�H�˱��ɶU'
      borrow12='��ݤp�B�u���ĸ�ӷ��G�V�B�ͭɶU'
      borrow13='��ݤp�B�u���ĸ�ӷ��G�ϥΫH�Υd�`���H��'
      borrow14='��ݤp�B�u���ĸ�ӷ��G�з|'
      borrow15='��ݤp�B�u���ĸ�ӷ��G�V�Ȧ�U��'
      borrow16='��ݤp�B�u���ĸ�ӷ��G�V�a�U�����ɶU'
      borrow17='��ݤp�B�u���ĸ�ӷ��G���'
      borrow18='��ݤp�B�u���ĸ�ӷ��G�X��{���겣'
      borrow19='��ݤp�B�u���ĸ�ӷ��G��L'
      reason1='�Ĥ@��ܫ�ݤp�B�u���ĸ�ӷ����z��'
      hold1='�����H�Υd'  hold2='�����H�Υd�i��'
      hold3='�w�������H�Υd'  hold4='�w�������H�Υd�i��'
      hold5='������'  hold6='������]'  hold7='�D�L�H�Υd��'
      b_att1='�H�Υd�٫o��a�j�q�{��'
      b_att2='�ϥΫH�Υd�C�몺��O��ϥΫe�W�[�\�h'
      b_att3='�C��I�M�H�Υd�b��A���ϥδ`���H��'
      b_att4='�������z�H���B��'
      b_att5='�H�Υd���C���b��٥h�O�b���·�'
      b_att6='�X��ɤ~�ϥΫH�Υd'
      b_att7='�V�Ӧ��p���a�ϥΫH�Υd'
      b_att8='�d���]�p�����N��өʻP�ӤH����'
      b_att9='�H�Υd�W�[�F�İ��ʪ����i��'
      b_att10='�����H�Υd�N��F�ӤH�������a��'
      b_att11='�H�Υd�����n���]�ȿĳq�\��'
      b_att12='�ϥΫH�Υd�᪫��ͬ��~�责�@�\�h'
      b_att13='�ϥΫH�Υd�����|�ʶR�@�ǹL�h�R���_���F��'
      b_att14='�H�Υd�O�i���i�L���F��'
      b_att15='�H�Υd�O���|���o�c�W�����@'
      b_att16='�H�Υd�̤j���n�B�O�u�����O�A��I�ڡv'
      b_att17='�H�Υd�W�[�F���O�̪��������'
      b_att18='����Ө��A�H�Υd�������\��j��t���\��'
      factor1='�ӫH�Υd�ɲĤ@���n�Ҽ{�]��'
      factor2='�ӫH�Υd�ɲĤG���n�Ҽ{�]��'
      factor3='�ӫH�Υd�ɲĤT���n�Ҽ{�]��'
      factor4='�ӫH�Υd�ɲĥ|���n�Ҽ{�]��'
      factor5='�ӫH�Υd�ɲĤ����n�Ҽ{�]��'
      factor6='�ӫH�Υd�ɲĤ����n�Ҽ{�]��'
      factor7='�ӫH�Υd�ɲĤC���n�Ҽ{�]��'
      factor8='�ӫH�Υd�ɲĤK���n�Ҽ{�]��'
      factor9='�ӫH�Υd�ɲĤE���n�Ҽ{�]��'
      factor10='�ӫH�Υd�ɲĤQ���n�Ҽ{�]��'
      beh1='���_�ϥιL�`���H��'  beh2='�ϥδ`���H�έ�]�Υ��ϥέ�]'
      beh3='�{�b�O�_�ϥδ`���H��'  beh4='�{�b�ϥδ`���H�έ�]�Υ��ϥέ�]'
      beh5='�N�ӬO�_�i��ϥδ`���H��'
      beh6='�`���H�ΧQ���P�p�B�L��O�U�ڧQ�������'
      k1='VISA'  k2='MASTER'
      k3='JCB'  k4='�j��'
      k5='�p�X�H�Υd'  k6='����H�U'
      k7='��X�Ȧ�'  k8='�����D'
      k9='�H�Υd���d�~�O'  k10='�D�ʽհ����d�H����d�B��'
      k11='�uú�I�u�̧C�I���B�v�ΦP�N�ϥδ`���Q�vú��'
      k12='�U�a�o�d�Ȧ�ҭq�w���`���Q�v�P�_����ҬۦP'
      k13='�鮧�U�������A�һݤ�I�Q�����B'  k14='�~��18.25%�A�һݤ�I�Q�����B'
      k15='�A��d�s���'  k16='�u�����O�A��I�ڡv�������̪�'
      k17='�u�H�δ`���_����v���W�w����O�̳̦��Q'
      k18='�Q���~�ٱo�[�H����'
      k19='�����]�t�~�O�B�w�ɲ{���B��������O��'
      k20='������B�o�d�Ȧ楲���t�᱾���e24�p�ɾD�_�Ϊ��l��'
      k21='��@�i�H�Υd�D�o�d�Ȧ�j��פ�ϥΡA��L�@�d�Ȧ�i���ƥ��q�����C�μȰ��H�Υd���ϥ�'
      k22='�H�Υd�w���ƫ����d��'
      afterb1='�O�_�Ҽ{�A�h�ӽдX�i�H�Υd'
      afterb2='�N�ӬO�_���i��ϥδ`���H��'
      afterb3='������A�p�B�u���ĸ�V�a�H�˱��ɶU'
      afterb4='������A�p�B�u���ĸ�V�B�ͭɶU'
      afterb5='������A�p�B�u���ĸ�h�ϥΫH�Υd�`���H��'
      afterb6='������A�p�B�u���ĸ�h�з|'
      afterb7='������A�p�B�u���ĸ�V�Ȧ�U��'
      afterb8='������A�p�B�u���ĸ�V�a�U�����ɶU'
      afterb9='������A�p�B�u���ĸ�h���'
      afterb10='������A�p�B�u���ĸ�ӷ��|�X��{���겣'
      afterb11='������A�p�B�u���ĸ�ӷ��G��L'
      a_att1='������A�H�Υd���٫o�a�{���·Х~�õL�n�B'
      a_att2='������A�H�Υd���@�ح��n���]�ȿĳq�u��'
      a_att3='������A�H�Υd�W�[�F���|�B�ذ���������'
      a_att4='������A�H�Υd���U���@�ͬ��~��'
      a_att5='������A�H�Υd�O�{�N�ͬ������i�ίʪ��F��'
      a_att6='������A�p�Ш|���p���ϥΫH�Υd�h�ȱo���s'
      a_att7='������A��ߦb�ϥΫH�Υd��|�W�[�C����O'
      a_att8='������A�o�����O�̷|�B�Υ����O��I�ڥ\��'
      a_att9='������A�H�Υd�W�[�F���O�̪��������'
      a_att10='������A�{���H�Υd�������\��h��t���\��'
      afterb12='������A��H�Υd�`���H�ΧQ�v���ݪk'
      afterb13='������A���ϥδ`���H�Ϊ��A�׻P�覡';


/*��p�e����--������*/
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

/*�M�οﶵ�ƭȻ���*/
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

/*���榸�Ƥ��t*/
proc freq;

run;
