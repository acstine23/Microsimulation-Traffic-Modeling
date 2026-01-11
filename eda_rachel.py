# Rachel's EDA file

import pandas as pd
import plotly_express as px

instances_df = pd.read_csv('Instances.csv')
radar_points_df = pd.read_csv('Radar_Points.csv')
runs_df = pd.read_csv('Runs.csv')

# Q1: Does gender of driver impact results? Do men drive faster? Women?
# Q2: Is the type of vehicle significant?

# merging data
joined_radar_instance_df = instances_df.merge(radar_points_df,on='global_instance_id')
joined_radar_instance_run_df = joined_radar_instance_df.merge(runs_df,on='run_id')
# create datetime field (date of run + timestamp of radar point)
joined_radar_instance_run_df['date_formatted'] = joined_radar_instance_run_df['date'].str.split('/')
joined_radar_instance_run_df['date_formatted'] = joined_radar_instance_run_df['date_formatted'].str.join('-')
joined_radar_instance_run_df['datetime'] = joined_radar_instance_run_df['date_formatted'] + ' ' + joined_radar_instance_run_df['timestamp']
joined_radar_instance_run_df['datetime'] = pd.to_datetime(joined_radar_instance_run_df['datetime'])

# Exploring gender
# more men or women test drivers? 
print(runs_df.groupby('sex')['run_id'].count())