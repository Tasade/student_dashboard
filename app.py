import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

df = pd.read_csv("train.csv")

st.title("🎓 Öğrenci Başarı Analiz Paneli")

# Sidebar filtreler
st.sidebar.header("Filtreler")
gender = st.sidebar.multiselect("Cinsiyet", df["gender"].unique(), df["gender"].unique())
course = st.sidebar.multiselect("Bölüm", df["course"].unique(), df["course"].unique())

filtered = df[df["gender"].isin(gender) & df["course"].isin(course)]

st.metric("Öğrenci Sayısı", len(filtered))
st.metric("Ortalama Puan", round(filtered["exam_score"].mean(),2))

# ---- Grafik 1
st.subheader("Yaş – Başarı")
fig1, ax1 = plt.subplots()
filtered.groupby("age")["exam_score"].mean().plot(ax=ax1)
st.pyplot(fig1)

# ---- Grafik 2
st.subheader("Çalışma Saati – Başarı")
fig2, ax2 = plt.subplots()
ax2.scatter(filtered["study_hours"], filtered["exam_score"])
st.pyplot(fig2)

# ---- Grafik 3
st.subheader("Cinsiyet – Başarı")
fig3, ax3 = plt.subplots()
filtered.groupby("gender")["exam_score"].mean().plot(kind="bar", ax=ax3)
st.pyplot(fig3)

# ---- Grafik 4
st.subheader("Uyku Kalitesi – Başarı")
fig4, ax4 = plt.subplots()
filtered.groupby("sleep_quality")["exam_score"].mean().plot(kind="bar", ax=ax4)
st.pyplot(fig4)

# ---- Grafik 5
st.subheader("Çalışma Yöntemi – Başarı")
fig5, ax5 = plt.subplots()
filtered.groupby("study_method")["exam_score"].mean().plot(kind="bar", ax=ax5)
st.pyplot(fig5)
