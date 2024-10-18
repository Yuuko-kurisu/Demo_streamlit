''' 

    1.  实验流程介绍
    2.  实验指标
    3.  实验结果展示

'''

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.markdown("# 实验介绍 🎈")

st.markdown("## 1. 实验流程介绍")



st.markdown('''
    （1） 用旅游领域的数据集开展多标签分类工作，识别用户意图标签，训练得到模型。
    
    （2） 对于某个特定的用户查询语句，在识别得到的用户多意图基础上，先后设计意图扩展策略和意图路由机制，补全用户意图，并链接到合适的数据源输出内容。
            
    （3） 选取Test Case (三类查询各20个)，进行消融实验和对比实验。
''')

st.markdown("## 2. 实验指标")

st.markdown('''
            
    三种类型
            
        - 答案型
        - 执行型
        - 推荐型
            
    三个维度：

        - 意图标签分类
        - 意图类型判断
        - 回复内容合格

    三个重要指标：
    
        - 1. 准确率
        - 2. 召回率
        - 3. F1值
''')

st.markdown("## 3. 实验结果展示-消融实验")



st.markdown('''
    目前结果还没出来，用的是随机数据
''')

st.markdown('### 意图标签分类结果')


# 定义方法列表和指标
method_list = ['核心方法','多分类模型+意图扩展策略', '意图路由机制', '是否使用LLM']
metrics = ['准确率', '召回率', 'F1值']
intent_types = ['答案型', '执行型', '推荐型', '总体']

# 创建多级索引的列
columns = pd.MultiIndex.from_product([intent_types, metrics], names=['Intent Type', 'Metric'])

# 创建DataFrame并填充数据
data = np.random.rand(len(method_list), len(columns))  # 使用随机数据作为示例
intent_label_df = pd.DataFrame(data, index=method_list, columns=columns)

# 在Streamlit中展示DataFrame
st.write(intent_label_df)

st.markdown('### 意图类型判断结果')

data_type = np.random.rand(len(method_list), len(columns))  # 使用随机数据作为示例
intent_type_df = pd.DataFrame(data, index=method_list, columns=columns)

# 在Streamlit中展示DataFrame
st.write(intent_type_df)

st.markdown('### 回复内容合格结果')

data_response = np.random.rand(len(method_list), len(columns))  # 使用随机数据作为示例
response_df = pd.DataFrame(data, index=method_list, columns=columns)

# 在Streamlit中展示DataFrame
st.write(response_df)