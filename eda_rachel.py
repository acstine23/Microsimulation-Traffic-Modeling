# Rachel's EDA file

import pandas as pd
import plotly_express as px

instances_df = pd.read_csv('Instances.csv')
radar_points_df = pd.read_csv('Radar_Points.csv')
runs_df = pd.read_csv('Runs.csv')

""" SECTION 1 """
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
px.scatter(joined_radar_instance_run_df,x='leader_accel',y='follower_accel',color='sex',opacity=.2).show()
px.scatter(joined_radar_instance_run_df,x='leader_vel',y='follower_vel',color='sex',opacity=.2).show()

# follow up q's
    # observations of velocity and acceleration where the driver was female have a larger spread than those where the driver was male. 
    # Why?
    # More observations by women? Was one gender driving in more congested/uncongested traffic?

print(runs_df.groupby('sex')['run_id'].count())
print(joined_radar_instance_run_df.groupby('sex')['global_instance_id'].count())
px.histogram(joined_radar_instance_run_df,x='congestion',color='sex').show()

# Answers
    # while there only 26 runs made by female drivers as opposed to 32 by male drivers,
    # the total number of radar points created on female-driver runs was female 318679- 
    # 37,146 more radar points than recorded by men. Women made up over half of the observations 
    # recorded for congested traffic, while male and female drivers were nearly evenly responsible
    # for observations in uncongested traffic.

""" SECTION 2 """
# Using PowerBI to draft visualizations, what can we hypothesize about road_type and safety?

''' 
when we compare the variance and standard deviation in follower_vel and leader_vel with the road_type, 
we find that there is a greater variation in velocity in instances where the road_type is aw (advanced warning) 
and wz2 (work zone without lane closure). 

This may indicate that not all drivers adjust their acceleration until A) they reach the work zone (tz)
or B) a lane closure restricts their driving options (wz1).

Follow up q's:
- how significant is the variance of velocity / speed?
- what is the distribution of velocity / acceleration for each road type?
- how long does it take a vehicle to pass through the work zone in congested traffic? uncongested? with lane closure? without?
    - is there a real difference in time or a perceived difference in time to traverse the work zone?


'''