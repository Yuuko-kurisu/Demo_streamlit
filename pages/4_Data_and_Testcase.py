''' 

样例：给个图

表格：给个表

推荐内容

评价标准：话就行

'''

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.markdown("# 数据样例和表格展示 🎈")

st.markdown("## 数据样例")

st.write(f"""
    本研究将用户查询分为三类：答案类查询、推荐类查询和执行类查询。
    
    对旅游助手回复的期待如下：（1）操作类查询，尽可能返回调用步骤和所需信息（2）答案类查询，言简意赅的回答问题，（3）推荐类查询，推荐相关的内容并尽可能全面
         
    下面是数据集中的一些样例：
""")

st.markdown("- 答案类查询样例：")

st.markdown('''
    ![](https://raw.githubusercontent.com/Yuuko-kurisu/Kurisu-pic-bed/master/pic/202410172357880.png)
''')

st.markdown("- 推荐类查询样例：")

st.markdown('''
    ![](https://raw.githubusercontent.com/Yuuko-kurisu/Kurisu-pic-bed/master/pic/202410172358771.png)
''')

st.markdown("- 执行类查询样例：")

st.markdown('''
    ![](https://raw.githubusercontent.com/Yuuko-kurisu/Kurisu-pic-bed/master/pic/202410172358508.png)
''')

st.markdown("## 意图样例表格展示")

# 路径设置
path_base_data = './data/source_data/'
path_test_case = path_base_data + 'test_case/'
path_resource = path_base_data + 'knowledge_base/resource/'

# 读取excel 都好
name_test_case = '意图.csv'
test_case = pd.read_csv(path_test_case + name_test_case)

# 按照type进行分类，分别放到不同的dict中
test_case_dict = {}
query_type_list_ = test_case['type'].unique()

test_case_Answer = test_case[test_case['type'] == 'Answer']
test_case_Execute = test_case[test_case['type'] == 'Execute']
test_case_Recommend = test_case[test_case['type'] == 'Recommend']

st.markdown("- 答案类查询")

st.write(test_case_Answer.head())

st.markdown("- 执行类查询")

st.write(test_case_Execute.head())

st.markdown("- 推荐类查询")

st.write(test_case_Recommend.head())


st.markdown("### 推荐项")

# Execute 类型
query_type = 'Execute'
path_Execute_item = path_resource + query_type + '/'
name_Execute_item = 'module_list.csv'
Execute_item = pd.read_csv(path_Execute_item + name_Execute_item)

st.markdown("- 执行类查询的推荐项")

st.write(Execute_item.head())

# Recommend 类型
query_type = 'Recommend'
path_Recommend_item = path_resource + query_type + '/'
name_Recommend_item = 'hotel_list.csv'
Recommend_item = pd.read_csv(path_Recommend_item + name_Recommend_item)

st.markdown("- 推荐类查询的推荐项")

st.write(Recommend_item.head())

st.markdown("- 答案类查询的推荐项")

st.write("从向量数据库中查询")

st.markdown("## 源数据集和标签介绍")

st.write(f"""
    xxx
""")