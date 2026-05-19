import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from prompt import SYSTEM_PROMPT


class SalesDataAgent:

    def __init__(self, api_key):
        self.llm = ChatOpenAI(
            api_key=api_key,
            model="gpt-4o-mini",
            temperature=0
        )

    def analyze_dataframe(self, df: pd.DataFrame):

        sample_data = df.head(20).to_markdown()

        numeric_summary = df.describe(include='all').to_markdown()

        prompt = f'''
数据样例：

{sample_data}

统计信息：

{numeric_summary}

请对该销售数据进行完整商业分析。
'''

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=prompt)
        ]

        response = self.llm.invoke(messages)

        return response.content

    def ask_question(self, df: pd.DataFrame, question: str):

        sample_data = df.head(30).to_markdown()

        prompt = f'''
数据：

{sample_data}

用户问题：
{question}

请根据数据回答。
'''

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=prompt)
        ]

        response = self.llm.invoke(messages)

        return response.content
