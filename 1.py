import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 한글 폰트 설정 (윈도우용)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

mpg= pd.read_csv("mpg.csv")
  

# cat.jpg 이미지 표시 (경로를 이미지 위치에 맞게 수정)
st.sidebar.image("cat1.jpg", caption="고양이 사진", use_container_width=True)

#1. 사이드 바를 활용 
company = st.sidebar.selectbox('원하는 자동차회사를 선택하세요.', 
                              mpg['manufacturer'].unique().tolist())
mpg_selected_manufacturer = mpg.query('manufacturer == @company')
st.subheader("1. Sidebar 이용")
st.dataframe(mpg_selected_manufacturer)


#2. mpg 데이터를 확인하는데, manufacturer로 filtering이 진행.
# 전체도 보고싶다. 

#c= "hyundai"
st.subheader("7번")
st.subheader(mpg['manufacturer'].unique().tolist())
l1 = mpg['manufacturer'].unique().tolist()
l1.append('전체')
st.subheader(l1)

#만약에 '전체'이 선택 -> mpg_selected = mpg.copy()
#만약에 '전체 '빼고 나머지 => mpg_selected =mpg.query('manufacturer == @c')
c=st.selectbox("회사를 선택하세요",l1)
if c == "전체" :
    #참일때 실행하는 코드
    mpg_selected = mpg.copy()    
else:
    #거짓일때 실행하는 코드
    mpg_selected =mpg.query('manufacturer == @c')    

st.dataframe(mpg_selected)


#6.  
# 1) 그룹핑을 할것을 정하고 싶어. 
# - manufacturer, model, drv, category
# 2) 연비 - cty, hwy
# 3) 함수 - min, max, count, mean, sum
st.title("6번")
var1 = st.selectbox('분석하고 싶은 그룹을 선택', 
                    ['manufacturer','model', 'drv', 'category'])
var2 = st.selectbox('연비종류를 선택', ['cty','hwy'])
var3 = st.selectbox('통계 종류 선택',['min', 'max', 'mean', 'count','sum'])
st.title("당신이 선택한 그룹은 : " + var1 + " 연비는:  " +var2 +  " 통계는 : " +var3)
mpg7 = mpg.groupby(var1)\
            .agg(value = (var2, var3))
st.dataframe(mpg7)


#5. multiselect를 한다. 
st.title("5번 multi-select")
multi_selected_manufacturer = st.multiselect('여러개의 자동차회사를 선택하세요.', 
               mpg['manufacturer'].unique().tolist())
st.title(multi_selected_manufacturer)
#mpg.query('manufacturer in ["honda", "audi"]')
mpg_multi = mpg.query('manufacturer in @multi_selected_manufacturer')
st.dataframe(mpg_multi)
#manufacture별로 city 평균연비 구해서 dataframe 프린트 하고, 
# x축 manufaucturer, y축 - city 평균 연비 , bargraph 그리기

mpg_multi = mpg_multi.groupby('manufacturer')\
            .agg(mean_city = ('cty', 'mean'))

st.dataframe(mpg_multi)

fig1 = plt.figure()
sns.barplot(data =mpg_multi, x="manufacturer", y="mean_city" )
st.pyplot(fig1)
  

#4. mpg['manufacturer'] 모든 값을 select box에 넣고 싶다.
st.title("4번")
company = st.selectbox('원하는 자동차회사를 선택.',
                       mpg['manufacturer'].unique().tolist())
mpg_selected_manufacturer = mpg.query('manufacturer == @company')
st.dataframe(mpg_selected_manufacturer)

#3. 사용자가 회사명을 입력하도록 설정
st.title("3번 selectbox 이용한것입니다.")
company = st.selectbox('원하는 자동차회사를 선택하세요.', 
                              ['audi', 'hyundai','honda','dodge'])
mpg_selected_manufacturer = mpg.query('manufacturer == @company')
st.dataframe(mpg_selected_manufacturer)


#2. 회사명을 따로 변수로 분리
company ="hyundai"
st.title("2번")
mpg_hyundai = mpg.query('manufacturer == @company')
st.dataframe(mpg_hyundai)

#1. query문에 직접 회사명을 쓴다.
mpg_hyundai = mpg.query('manufacturer == "hyundai"')
st.title("1번")
st.dataframe(mpg_hyundai)
 