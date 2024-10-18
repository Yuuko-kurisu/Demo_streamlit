''' 

按照规划的界面展开输出，从最简单的开始

'''


## 导入库
import json
import streamlit as st
# from streamlit_tags import st_tags, st_tags_sidebar

## 数据录入
path_data = './data/static_data_6_test.json'
name_data = 'static_data_6.json'
path_query_data = path_data + name_data
path_query_data = path_data
with open(path_query_data, 'r',encoding='utf-8') as f:
    data = json.load(f)

# print(data)
## 数据处理

query_index = 0
index2query_dict = {}
query2index_dict = {}
for static_result in data:
    # print(static_result)
    query_ = static_result['query']
    index2query_dict[query_index] = query_
    query2index_dict[query_] = query_index
    query_index += 1

query_select = '如果我带宠物入住，房间会有什么额外的清洁服务吗？'

query_select_index = query2index_dict[query_select]
output_label = data[query_select_index]['output_label']
intent_type = data[query_select_index]['intent_type']
response_dict = data[query_select_index]['response_dict']
sub_intent_type_list = list(response_dict.keys())
sub_intent_type = sub_intent_type_list[0]
response_sub = response_dict[sub_intent_type]

intent_type_intro_dict = {
    'Answer': '答案类查询，言简意赅的回答问题',
    'Recommend': '推荐类查询，推荐相关的内容并尽可能多元',
    'Execute': '执行类查询，尽可能返回调用步骤和所需信息',
}

## UI布置

## ================== Part 0 输入栏 ==================

st.markdown("# 用户意图识别——静态演示页面 🎈")

st.markdown("## 输入栏")

st.text_input("直接输入查询", key="query_select_1")

# You can access the value at any point with:
st.session_state.query_select_1

query_select_2 = st.selectbox('或者选择一个已有查询', list(query2index_dict.keys()), index=query_select_index)

# 优先考虑直接输入的query
if st.session_state.query_select_1:
    query_select = st.session_state.query_select_1
else:
    query_select = query_select_2

# query_select_index = query2index_dict[query_select]

st.write(f'目前选择的查询是：{query_select}')

# st.button('查询')

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('意图识别', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')

    # import time

    # '识别用户意图标签'

    # # Add a placeholder
    # # 设置进度条，次数为20
    # latest_iteration = st.empty()
    # bar = st.progress(0)

    # for i in range(100):
    #     # Update the progress bar with each iteration.
    #     time_sleep = 0.01
    #     # latest_iteration.text(f'{(i+1)*time_sleep}秒')
    #     latest_iteration.text(f'{(i+1)}%')
    #     bar.progress(i + 1)
    #     time.sleep(time_sleep)


    ## ================== Part 1 意图标签展示 ==================

    st.markdown("## 意图标签展示")

    query_select_index = query2index_dict[query_select]
    output_label = data[query_select_index]['output_label']
    intent_type = data[query_select_index]['intent_type']
    response_dict = data[query_select_index]['response_dict']
    sub_intent_type_list = list(response_dict.keys())
    sub_intent_type = sub_intent_type_list[0]
    response_sub = response_dict[sub_intent_type]

    # query2index_dict

    # st.write(f'该查询的意图标签index是：{query_select_index}')
    st.write(f'该查询的意图标签是：{output_label}')

    # st.write(f'该查询的意图标签如下，可人为调整：')

    # 设置可编辑的标签
    # keywords_label = st_tags(
    #     label='该查询的意图标签如下，可人为调整：',
    #     text='Press enter to add more',
    #     value=output_label,
    #     suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    #     # maxtags=maxtags,
    #     key="label")


    # st.write(keywords)


    ## 用可编辑的标签展示意图类型（待定）


    ## ================== Part 2 意图类型展示 ==================

    st.markdown("## 意图类型展示")

    st.write(f'该查询的意图类型是：{intent_type}')

    # keywords_intent = st_tags(
    #     label='该查询的意图类型如下，可人为调整：',
    #     text='Press enter to add more',
    #     value=[intent_type],
    #     # suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    #     # maxtags=maxtags,
    #     key="intent")
    
    # intent_type = keywords_intent[0]
    intent_type_intro = intent_type_intro_dict[intent_type]
    st.write(f'意图类型为{intent_type}:{intent_type_intro}')

    ## 解释几类意图类型（待定，先给一个字典）

    ## ================== Part 3 回答展示 ==================

    st.markdown("## 回答展示")

    ## 1个按钮或者2排按钮。

    nums_sub_intent = len(sub_intent_type_list)

    if nums_sub_intent == 1:
        # 做一个按钮
        sub_intent_type = sub_intent_type_list[0]
        st.write(f'通过{sub_intent_type}方式回答')

        if st.button('展开回答'):
            st.write(f'该查询的回答是：\n\n {response_sub}')
        # st.write(f'该查询的回答是：{response_sub}')
    else:
        # 做两排按钮
        sub_intent_type_str = '、'.join(sub_intent_type_list)
        st.write(f'可通过以下方式回答：{sub_intent_type_str}')

        sub_intent_type = st.selectbox('选择回答方式', sub_intent_type_list)



        if st.button('展开回答'):
            st.write(f'该查询的回答是：\n\n {response_dict[sub_intent_type]}')
        # st.write(f'该查询的回答是：{response_dict[sub_intent_type]}')
else:
    st.write('Button is off!')




