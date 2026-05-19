import os
import streamlit as st
from dotenv import load_dotenv

from data_loader import load_excel, basic_info
from charts import sales_by_product, sales_trend
from agent import SalesDataAgent

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="AI 销售数据分析 Agent",
    layout="wide"
)

st.title("AI 销售数据分析 Agent")

uploaded_file = st.file_uploader(
    "上传 Excel 销售数据",
    type=["xlsx", "xls"]
)

if uploaded_file:

    df = load_excel(uploaded_file)

    st.success("文件上传成功")

    st.subheader("数据预览")
    st.dataframe(df.head())

    info = basic_info(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("总行数", info["rows"])
    col2.metric("总字段数", info["columns"])
    col3.metric("缺失字段", sum(info["missing_values"].values()))

    st.subheader("字段信息")
    st.write(info["column_names"])

    st.subheader("AI 自动分析")

    if st.button("开始 AI 分析"):

        with st.spinner("AI 正在分析数据..."):

            agent = SalesDataAgent(OPENAI_API_KEY)

            analysis = agent.analyze_dataframe(df)

            st.markdown(analysis)

    st.subheader("自动图表分析")

    columns = list(df.columns)

    product_col = st.selectbox("选择产品字段", columns)
    sales_col = st.selectbox("选择销售字段", columns)

    fig1 = sales_by_product(df, product_col, sales_col)
    st.plotly_chart(fig1, use_container_width=True)

    date_col = st.selectbox("选择日期字段", columns)

    fig2 = sales_trend(df, date_col, sales_col)
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("AI 数据问答")

    user_question = st.text_input("请输入你的问题")

    if st.button("提交问题"):

        with st.spinner("AI 正在思考..."):

            agent = SalesDataAgent(OPENAI_API_KEY)

            answer = agent.ask_question(df, user_question)

            st.markdown(answer)
