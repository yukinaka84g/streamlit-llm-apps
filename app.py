#from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

import streamlit as st

# .env ファイルを読み込む
#load_dotenv()

# 環境変数から API キーを取得
# APIキーを Streamlit secrets から取得
openaiapikey = st.secrets["OPENAI_API_KEY"]

# ChatOpenAI インスタンスを作成
llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0,
    openai_api_key=openaiapikey
)



st.title("プロフェッショナルAI質問システム")

st.write("##### Aモード: 理科の教師")
st.write("理科の教師として質問に答えます。")
st.write("##### Bモード: 国語の教師")
st.write("国語の教師として質問に答えます。")


selected_item = st.radio(
    "動作モードを選択してください。",
    ["Aモード", "Bモード"]
)

st.divider()

input_message = st.text_input(label="質問を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "Aモード":
        if input_message:

            messages = [
                SystemMessage(content="あなたは理科の教師です"),
                HumanMessage(content=input_message),
                ]

                
            result = llm(messages)
            st.write(result)

        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")

    else:
        if input_message:

            messages = [
                SystemMessage(content="あなたは国語の教師です"),
                HumanMessage(content=input_message),
                ]

                
            result = llm(messages)
            st.write(result)

        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")