''' 

    1.  所提方法
    2. 消融实验的比较方法
    3. 对比实验的比较方法

'''

import streamlit as st

st.set_page_config(layout="wide")

st.markdown("# 方法介绍 🎈")

st.markdown("## 1. 所提方法")

st.markdown('''
    总体思路见主页。
            ''')

st.markdown("## 2. 消融实验的比较方法")

st.markdown('''
    （1）和多意图标签的消融（多分类模型+意图扩展策略，组合消融）

    （2）和多意图类型的消融（意图路由机制）

    （3）和是否使用LLM的消融（去掉所有LLM有关内容）
            ''')

st.markdown("## 3. 对比实验的比较方法")

st.markdown('''
    （1） Query向量相似性匹配推荐内容

    （2）根据多标签分类模型得到的标签计算向量相似性匹配推荐内容

    （3）直接问大模型匹配内容
            ''')