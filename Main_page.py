import streamlit as st

# 主页名字

st.set_page_config(layout="wide")
st.markdown("# Main page —— 用户意图识别 🎈")
# st.sidebar.markdown("# Main page 🎈")


# st.write("所有streamlit相关的尝试可以在子页面下进行.")

st.write(f"""
         
        本研究开展意图查询和推荐工作，研究背景如下：希望手机软件的智能旅游助手，帮助对接酒店、预定、取消和请求服务、回答一些基础问题

        - 首先基于酒店、预定领域的数据集开展多标签分类工作，识别用户意图标签。
        - 对于某个特定的用户查询语句，在识别得到的用户多意图基础上，先后设计意图扩展策略和意图路由机制，补全用户意图，并链接到合适的数据源输出内容。
            - 意图扩展策略：主要指得到意图类别均为通用意图时，或者判断缺少关键领域意图时，进行扩展。
            - 意图路由机制：主要指在得到用户意图后，根据意图类别，路由到合适的数据源。

         """)

st.write("整体流程如下：")

# 上传图片，图床

st.markdown('''
    ![](https://raw.githubusercontent.com/Yuuko-kurisu/Kurisu-pic-bed/master/pic/202410091056708.png)
''')

# st.markdown('
#     ![](https://raw.githubusercontent.com/Yuuko-kurisu/Kurisu-pic-bed/master/pic/202410091056708.png')
# )