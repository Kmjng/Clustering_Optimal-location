# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 12:20:30 2024

@author: itwill
"""

file1 = r"C:\Users\itwill\Downloads\국내_문화체육관광_분야_국립도군립_및_도시내_공원_데이터_2023.csv"
file2 = r"C:\Users\itwill\Downloads\전국주차장정보표준데이터.csv"

import pandas as pd 

df_park = pd.read_csv(file1, encoding = 'utf-8')
df_parking = pd.read_csv(file2, encoding = 'EUC-KR')

df_park.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10343 entries, 0 to 10342
Data columns (total 27 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   ID            10343 non-null  object 
 1   LCLAS_NM      10343 non-null  object 
 2   MLSFC_NM      10343 non-null  object 
 3   POI_ID        10343 non-null  int64  
 4   POI_NM        10343 non-null  object 
 5   BHF_NM        408 non-null    object 
 6   ASSTN_NM      0 non-null      float64
 7   CL_CD         10343 non-null  int64  
 8   CL_NM         10343 non-null  object 
 9   PNU           10343 non-null  int64  
 10  CTPRVN_NM     10343 non-null  object 
 11  SIGNGU_NM     10262 non-null  object 
 12  LEGALDONG_NM  10343 non-null  object 
 13  LI_NM         2599 non-null   object 
 14  LNBR_NO       10322 non-null  object 
 15  LEGALDONG_CD  10343 non-null  int64  
 16  ADSTRD_CD     10343 non-null  int64  
 17  RDNMADR_CD    5729 non-null   float64
 18  RDNMADR_NM    5730 non-null   object 
 19  BULD_NO       5730 non-null   object 
 20  LC_LO         10343 non-null  float64
 21  LC_LA         10343 non-null  float64
 22  GID_CD        10343 non-null  object 
 23  LAST_CHG_DE   10343 non-null  int64  
 24  ORIGIN_NM     10343 non-null  object 
 25  FILE_NM       10343 non-null  object 
 26  BASE_DE       10343 non-null  int64  
dtypes: float64(4), int64(7), object(16)
memory usage: 2.1+ MB
'''
df_park[df_park['SIGNGU_NM']=='남양주시']
df_park = df_park[['POI_NM','CL_NM','LC_LA','LC_LO']]

df_park.columns =['시설명','공원종류','위도','경도']
df_park.isnull().sum()

df_parking.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 16986 entries, 0 to 16985
Data columns (total 34 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   주차장관리번호        16986 non-null  object 
 1   주차장명           16986 non-null  object 
 2   주차장구분          16986 non-null  object 
 3   주차장유형          16986 non-null  object 
 4   소재지도로명주소       8300 non-null   object 
 5   소재지지번주소        15994 non-null  object 
 6   주차구획수          16986 non-null  int64  
 7   급지구분           16986 non-null  object 
 8   부제시행구분         16986 non-null  object 
 9   운영요일           16986 non-null  object 
 10  평일운영시작시각       16986 non-null  object 
 11  평일운영종료시각       16986 non-null  object 
 12  토요일운영시작시각      16986 non-null  object 
 13  토요일운영종료시각      16986 non-null  object 
 14  공휴일운영시작시각      16986 non-null  object 
 15  공휴일운영종료시각      16986 non-null  object 
 16  요금정보           16986 non-null  object 
 17  주차기본시간         16986 non-null  float64
 18  주차기본요금         12892 non-null  float64
 19  추가단위시간         6691 non-null   float64
 20  추가단위요금         6670 non-null   object 
 21  1일주차권요금적용시간    4649 non-null   float64
 22  1일주차권요금        5210 non-null   float64
 23  월정기권요금         5149 non-null   object 
 24  결제방법           5338 non-null   object 
 25  특기사항           3211 non-null   object 
 26  관리기관명          16986 non-null  object 
 27  전화번호           14578 non-null  object 
 28  위도             13958 non-null  float64
 29  경도             13954 non-null  float64
 30  장애인전용주차구역보유여부  4762 non-null   object 
 31  데이터기준일자        16986 non-null  object 
 32  제공기관코드         16986 non-null  object 
 33  제공기관명          16986 non-null  object 
dtypes: float64(7), int64(1), object(26)
memory usage: 4.4+ MB
'''
# '소재지지번주소','주차장명','위도','경도'
df_parking['소재지지번주소'].isnull().sum() # 992
df_parking = df_parking[df_parking['소재지지번주소'].notnull()]
df_parking= df_parking[df_parking['소재지지번주소'].str.contains('남양주')]
df_parking = df_parking[['소재지지번주소','주차장명','위도','경도']]


df_park.to_csv("C:\ITWILL\문화_공모전\남양주_공원(전처리).csv")
df_parking.to_csv("C:\ITWILL\문화_공모전\남양주_주차장(전처리).csv")
