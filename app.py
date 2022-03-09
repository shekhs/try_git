#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.graph_objects as go


df = pd.read_csv("dataset.csv")

df.head()

df.shape

st.dataframe(df)

cols = df.columns

pick_cols = st.selectbox("Count by column: ",cols)

df["number"] = 0
df_count = df.groupby(pick_cols).count()
df_count = pd.DataFrame(df_count["number"])
df_count["percent"] = (df_count.number/df_count.number.sum())*100

df_count.head()

st.dataframe(df_count)

multi_cols  = st.multiselect("Multiple columns ofr correlation",cols,default=["sex"])
multi_sel_col_df = df[multi_cols]

st.dataframe(multi_sel_col_df)

multi_cols2 = st.multiselect("multi select grouped by:",cols,default=["sex"])
multi_group=df[multi_cols2].groupby(multi_cols2).size().reset_index(name="number")
multi_group["Pc"] = (multi_group.number/multi_group.number.sum())*100

st.dataframe(multi_group)

viz = st.selectbox("Viz by column",cols)

df_viz = df.groupby(viz).count()
df_viz = pd.DataFrame(df_viz["number"])
df_viz["percent"] = (df_viz.number/df_viz.number.sum())*100

df_viz.head()

df_viz["X-axis"] = df_viz.index

fig = go.Figure(data=[go.Pie(labels=df_viz["X-axis"],values=df_viz["number"])])

st.plotly_chart(fig)







