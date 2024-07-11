import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
data = pd.read_csv(r"E:\MY DICTIONARY\virat.csv")
print("Average Runs Score by Virat Kohli from 18-Aug-08 Till 22-Jan-17 -> ",
      data["Runs"].mean())
matches = data.index
figure = px.line(data, x=matches, y="Runs",
                 title='Runs Scored by Virat Kohli Between 18-Aug-08 - 22-Jan-17')
figure.show()
# Analysis of Virats Batting Positions
# Batting Positions
data["Pos"] = data["Pos"].map({3.0: "Batting At 3", 4.0: "Batting At 4", 2.0: "Batting At 2",
                               1.0: "Batting At 1", 7.0: "Batting At 7", 5.0: "Batting At 5",
                               6.0: "batting At 6"})
Pos = data["Pos"].value_counts()
label = Pos.index
counts = Pos.values
colors = ['gold', 'lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(
    title_text='Number of Matches At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()
# Centurties Analysis Of Virat Kohli
centuries = data.query("Runs >= 100")
figure = px.bar(centuries, x=centuries["Inns"], y=centuries["Runs"],
                color=centuries["Runs"],
                title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
figure.show()
# Score Against Teams
figure = px.bar(data, x=data["Opposition"], y=data["Runs"], color=data["Runs"],
                title="Most Runs Against Teams")
figure.show()
