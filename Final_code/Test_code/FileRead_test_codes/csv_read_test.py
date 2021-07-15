import pandas as pd

data = pd.read_csv(r'/home/pi/Desktop/Final_code/Waypoints/SU_Library_longway.csv')
waypoints = []
for row in range(len(data)):
    waypoints.append([data.iloc[row,0],data.iloc[row,1]])
print(waypoints)