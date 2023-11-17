import pandas as pd
import pandas

df_covid = pd.read_csv("AI research by institution.csv")
df_covid = df_covid.pivot(index="Year", columns="Organization", values="publications").fillna(0)
df_covid.plot_animated("covid-19-h-bar.gif", period_fmt="%Y", title="Covid-19 Cases")