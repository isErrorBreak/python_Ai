import pandas as pd
import matplotlib.pyplot as plt
import platform

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')

# 그래프에 마이너스 표시가 되도록 변경
plt.rcParams['axes.unicode_minus'] = False

acci = pd.read_csv('acci.csv', encoding='cp949')#euc-kr
print(acci.head())
print(acci.mean(axis=0))
print(acci.columns)
print(platform.system())

#ax = acci.plot(kind='bar',title = "교통사고", figsize=(12,4), legend = True,fontsize =12)
#ax.index = acci['법규위반']

# def add_value_label(x_list, y_list):
#     for i in range(1, len(x_list)+1):
#         plt.text(i,y_list[i-1], y_list[i-1])

acci.index = acci['법규위반']+'/'+acci['주야']
ax = acci['사망자수'].plot(
    kind = 'bar',
    title = '교통사고 사망자수',
    figsize=(12,12),
    legend = True
    )

#add_value_label(acci['사망자수'],acci['법규위반'])
ax.set_xlabel('법규위반', fontsize =12)
ax.set_ylabel('사망자수', fontsize = 12)
plt.xticks(rotation = 45)
plt.show()

a = acci['부상자수']
plt.plot(acci.index,a,marker = 'o',label = "부상자수")
b = acci['중상']
plt.plot(acci.index,b,marker = 'o',label = "중상자수")
c = acci['경상']
plt.plot(acci.index,c,marker = 'o',label = "경상자수")
plt.xticks(rotation = 90)
plt.legend(loc='upper left',ncol = 1)

plt.show()