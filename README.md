# DesignProject_SkiROS2

Instructions:

Install SkiROS2 accoriding to instructions found at https://github.com/RVMI/skiros2

Overwrite original launch-file found in .../catkin_ws/src/skiros2/skiros2/launch with the file in this repository found in the folder "To_launch_folder"

Add the folder "Skills" to .../catkin_ws/src

Update "sys.path.append" paths in primitives.py and skills.py, found in skills/skills_dorna2/src/skills_dorna2/

Add the folder "dorna2" to .../catkin_ws

Set up simulation with bridge in separate VM

Launch (according to SkiROS2 instructions found at https://github.com/RVMI/skiros2):

cd catkin_ws

catkin_make

source ./devel/setup.bash

roslaunch skiros2 skiros.launch

Note:
This code is incomplete. There are not enough conditions and parameter properties for the planner to solve the planning, since we discovered it did not function proprerly anyway. The compound skill which scans the cube only works provided the gripper does not fail.
