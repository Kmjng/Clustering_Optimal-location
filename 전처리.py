# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:00:52 2024

@author: itwill
"""
#########
## 전처리 
#########
file1 = r"C:\Users\itwill\Downloads\전국_어린이_대상_문화공간(키즈카페)_위치(2022).csv"
file2 = r"C:\Users\itwill\Downloads\전국초중등학교위치표준데이터.csv"
file3 = r"C:\Users\itwill\Downloads\어린이집기본정보조회(정기)-기준일(20240531).csv"

import pandas as pd 
df_kc = pd.read_csv(file1, encoding = 'utf-8')
df_sch = pd.read_csv(file2, encoding = 'EUC-KR')
df_chi = pd.read_csv(file3, encoding = 'utf-8')


df_kc.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1959 entries, 0 to 1958
Data columns (total 20 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   FLAG_NM           1959 non-null   object 
 1   FCLTY_NM          1959 non-null   object 
 2   RDNMADR_NM        1959 non-null   object 
 3   CTPRVN_KLANG_NM   1959 non-null   object 
 4   SIGNGU_KLANG_NM   1959 non-null   object 
 5   CTPRVN_ENG_NM     1959 non-null   object 
 6   SIGNGU_ENG_NM     1959 non-null   object 
 7   CTPRVN_CHNLNG_NM  1959 non-null   object 
 8   SIGNGU_CHNLNG_NM  1959 non-null   object 
 9   CTPRVN_JLANG_NM   1959 non-null   object 
 10  SIGNGU_JLANG_NM   1959 non-null   object 
 11  CTPRVN_CD         1959 non-null   int64  
 12  SIGNGU_CD         1959 non-null   int64  
 13  FCLTY_LO          1959 non-null   float64
 14  FCLTY_LA          1959 non-null   float64
 15  HMPG_URL          784 non-null    object 
 16  OPER_TIME         1382 non-null   object 
 17  UTILIIZA_CN       1057 non-null   object 
 18  TEL_NO            0 non-null      float64
 19  REGIST_DE         1959 non-null   int64  
dtypes: float64(3), int64(3), object(14)
memory usage: 306.2+ KB
'''
# 31130 # 남양주시 SIGNGU_CD
df_kc= df_kc[['SIGNGU_CD','RDNMADR_NM','FCLTY_NM','FCLTY_LA','FCLTY_LO']]
df_kc= df_kc[df_kc['SIGNGU_CD']==31130]
df_kc.SIGNGU_CD.unique()
df_kc.columns = ['시군구코드','지역명','시설명','위도','경도']

df_kc.isnull().sum()



df_sch.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11992 entries, 0 to 11991
Data columns (total 20 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   학교ID      11992 non-null  object   ★ 
 1   학교명       11992 non-null  object   ★
 2   학교급구분     11992 non-null  object   ★
 3   설립일자      11992 non-null  object 
 4   설립형태      11992 non-null  object 
 5   본교분교구분    11992 non-null  object 
 6   운영상태      11992 non-null  object 
 7   소재지지번주소   11992 non-null  object 
 8   소재지도로명주소  11992 non-null  object   ★
 9   시도교육청코드   11992 non-null  int64  
 10  시도교육청명    11992 non-null  object 
 11  교육지원청코드   11992 non-null  int64     ★ 
 12  교육지원청명    11992 non-null  object 
 13  생성일자      11992 non-null  object 
 14  변경일자      11992 non-null  object 
 15  위도        11992 non-null  float64  ★ 
 16  경도        11992 non-null  float64   ★
 17  데이터기준일자   11992 non-null  object 
 18  제공기관코드    11992 non-null  object 
 19  제공기관명     11992 non-null  object 
dtypes: float64(2), int64(2), object(16)
memory usage: 1.8+ MB
'''

# 남양주 교육지원청코드 7652000
df_sch = df_sch[['학교ID','학교명','학교급구분','소재지도로명주소','위도','경도']]
con = df_sch['소재지도로명주소'].str.contains('경기도 남양주시')
df_sch = df_sch[con]

df_sch.소재지도로명주소.unique()

df_sch.isnull().sum()


# 
df_chi.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 940 entries, 0 to 939
Data columns (total 24 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   시도        940 non-null    object 
 1   시군구       940 non-null    object    ★  
 2   어린이집명     940 non-null    object    ★ 
 3   어린이집유형구분  940 non-null    object    ★ 
 4   운영현황      940 non-null    object    ★ 
 5   우편번호      940 non-null    int64  
 6   주소        940 non-null    object 
 7   어린이집전화번호  940 non-null    object 
 8   어린이집팩스번호  940 non-null    object 
 9   보육실수      940 non-null    int64  
 10  보육실면적     940 non-null    int64  
 11  놀이터수      940 non-null    int64  
 12  CCTV설치수   940 non-null    int64  
 13  보육교직원수    940 non-null    int64  
 14  정원수       940 non-null    int64  
 15  현원수       940 non-null    int64  
 16  위도        898 non-null    float64   ★ 
 17  경도        898 non-null    float64   ★ 
 18  통학차량운영여부  893 non-null    object 
 19  홈페이지주소    159 non-null    object 
 20  인가일자      937 non-null    object 
 21  휴지시작일자    47 non-null     object 
 22  휴지종료일자    47 non-null     object 
 23  폐지일자      410 non-null    object 
dtypes: float64(2), int64(8), object(14)
memory usage: 176.4+ KB
'''

df_chi = df_chi[df_chi['운영현황'] != '폐지']
# '시군구','어린이집명','어린이집유형구분','위도','경도'
df_chi = df_chi[['시군구','어린이집명','어린이집유형구분','위도','경도']]

df_chi.시군구.unique() # 남양주시
df_chi.isnull().sum()

df_chi[df_chi['위도'].isnull()] # 지금동꿈동산어린이집
# 제거 
df_chi = df_chi[df_chi['어린이집명'] != '지금동꿈동산어린이집']


df_kc.to_csv('C:\ITWILL\문화_공모전\남양주_키즈카페(전처리).csv', index = False)
df_sch.to_csv('C:\ITWILL\문화_공모전\남양주_초중등학교(전처리).csv', index = False)
df_chi.to_csv('C:\ITWILL\문화_공모전\남양주_어린이집(전처리).csv', index = False)









