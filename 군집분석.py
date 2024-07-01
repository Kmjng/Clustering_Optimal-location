# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:51:49 2024

@author: itwill
"""
file1 = r"C:\ITWILL\문화_공모전\남양주_어린이집(전처리).csv"
file2 = r"C:\ITWILL\문화_공모전\남양주_초중등학교(전처리).csv"
file3 = r"C:\ITWILL\문화_공모전\남양주_키즈카페(전처리).csv"
file4 = r"C:\ITWILL\문화_공모전\남양주_주차장(전처리).csv"
file5 = r"C:\ITWILL\문화_공모전\남양주_공원(전처리).csv"
import pandas as pd 

df_chi = pd.read_csv(file1)
df_sch = pd.read_csv(file2)
df_kc = pd.read_csv(file3)

df_park = pd.read_csv(file5)
df_parking = pd.read_csv(file4)


df_chi.columns
df_sch.columns

df_sch = df_sch.rename(columns = {'학교명':'시설명'})
df_chi = df_chi.rename(columns = {'어린이집명':'시설명'})

df_kc.columns
df_sch.columns


from sklearn.cluster import KMeans # model 
import matplotlib.pyplot as plt # 군집결과 시각화 
import numpy as np # array 


df1 = df_chi[['시설명','위도','경도']]
df2 = df_sch[['시설명','위도','경도']]
df3 = df_kc[['시설명','위도','경도']]

df4 = df_kc[['시설명','위도','경도']]
df5 = df_kc[['시설명','위도','경도']]

df1['Category'] = 'kids_cafe'
df2['Category'] = 'schools'
df3['Category'] = 'daycares'
df4['Category'] = 'park'
df5['Category'] = 'parking_lot'

combined_df = pd.concat([df1,df2,df3,df4,df5], ignore_index=True)

kmeans = KMeans(n_clusters = 6, random_state = 42 )

# 모델링 및 클러스터링 기록
clusters  = kmeans.fit_predict(combined_df[['위도','경도']])

combined_df['cluster'] = clusters
print(combined_df)

centers = kmeans.cluster_centers_
print("Cluster centers:\n", centers)
''' 
 [[ 37.63330483 127.14644152]
 [ 37.71455742 127.18736231]
 [ 37.65207225 127.24032737]
 [ 37.6552297  127.30913889]
 [ 37.57960102 127.22242202]
 [ 37.58364887 126.97163815]]
'''
colors = {'kids_cafe': 'red', 'schools': 'blue', 'daycares': 'green'
          , 'park':'yellow','parking_lot':'purple'}

plt.figure(figsize=(10, 6))

for cat, color in colors.items():
    subset = combined_df[combined_df['Category'] == cat]
    plt.scatter(subset['경도'], subset['위도'], c=color, label=cat, s=100, alpha=0.6, edgecolors='w')

plt.scatter(centers[:, 1], centers[:, 0], marker='x', c='black', label='Centers', s=200)

plt.xlabel('경도')
plt.ylabel('위도')
plt.title('K-means Clustering of Geographic Coordinates')
plt.legend()
plt.show()


#############################
# KMeans 평가지표 (실루엣계수; 높을수록 좋음, 엘보우; 급감 지점)
#############################


# KMeans 클러스터링 수행
k_values = range(1, 10)
sse = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(combined_df[['위도', '경도']])
    sse.append(kmeans.inertia_)

# 엘보우 메서드 그래프
plt.figure(figsize=(10, 6))
plt.plot(k_values, sse, 'bo-')
plt.xlabel('Number of clusters')
plt.ylabel('Sum of Squared Errors (SSE)')
plt.title('Elbow Method for Optimal K')
plt.xticks(k_values)
plt.grid(True)

########################
# 기울기가 가장 큰 지점 표시
########################
# 기울기(변화율) 계산
gradient = np.diff(sse)  # SSE 값의 변화율 계산

# 변화율이 가장 큰 인덱스 찾기
optimal_k_index = np.argmax(gradient) + 1  # 인덱스를 클러스터 수로 변환

plt.axvline(x=optimal_k_index, color='r', linestyle='--', label=f'Optimal K: {optimal_k_index}')

plt.legend()
plt.show()

print(f"Optimal number of clusters (K): {optimal_k_index}")
