import pandas as pd

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
df = pd.read_csv(url)
print(df.head())

columns = ["Team", "Yellow Cards", "Red Cards"]
print(df[columns])

number_teams_Euro2012 = df.Team.count()
print(f"The number of teams that participated in Euro-2012 is\
 {number_teams_Euro2012}.")

teams_more_than_6_goals = df[df.Goals > 6]
print(f"Teams that scored more than 6 goals:\n {teams_more_than_6_goals}")
