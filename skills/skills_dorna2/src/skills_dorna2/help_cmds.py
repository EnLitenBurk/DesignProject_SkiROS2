# cmd = rostopic pub /cmd std_msgs/String "data: '{\"r1\":{\"ref_pos\": \"pre_take\"},\"r3\":{\"ref_pos\": \"pre_take\"},\"control_box\":{\"blue_light\": false},\"camera\":{\"do_scan\": false},\"gripper\":{\"close\": false},\"cubes\":{\"make_cube\": true,\"remove_cube\": false}}'" 
from std_msgs.msg import String
import json
import rospy


ros_cmd = String()
ros_pub = rospy.Publisher('/cmd',String,queue_size=1)
ros_cmd.data = '{\"r1\":{\"ref_pos\": \"unknown"},\"r3\":{\"ref_pos\": \"unknown\"},\"control_box\":{\"blue_light\": false},\"camera\":{\"do_scan\": false},\"gripper\":{\"close\": false},\"cubes\":{\"make_cube\": false,\"remove_cube\": false}}'

def update_cmd(last_cmd, update_device, update_act):
    new_cmd_str =  json.loads(last_cmd)

    if update_device in ['r1' , 'r3']:
        new_cmd_str[update_device]["ref_pos"] = update_act
    elif update_device == 'camera':
        new_cmd_str[update_device]["do_scan"] = update_act
    elif update_device == 'control_box':
        new_cmd_str[update_device]["blue_light"] = update_act
    elif update_device == 'gripper':
        new_cmd_str[update_device]["close"] = update_act
    elif update_device == 'cubes':
        if update_act == 'generate':
            new_cmd_str[update_device]["make_cube"] = True
        if update_act == 'stop_generate':
            new_cmd_str[update_device]["make_cube"] = False
        if update_act == 'remove':
            new_cmd_str[update_device]["remove_cube"] = True
        if update_act == 'stop_remove':
            new_cmd_str[update_device]["remove_cube"] = False
    else:
        print('Incorrect device')
        return json.dumps(new_cmd_str)
    new_cmd = json.dumps(new_cmd_str)
    ros_pub.publish(new_cmd)
    return new_cmd

def check_state(device, sensor, desired_state):
    with open('/home/johansson/catkin_ws/src/skiros2_examples/src/skiros2_examples/turtlesim_example/msg.json') as json_file:
        curr_state = json.load(json_file)
        return curr_state[device][sensor] == desired_state

# # print(ros_cmd.data)
# ros_cmd.data = update_cmd(ros_cmd.data, "control_box", "True")
# test = check_state("control_box","blue_light_on", True)






# # print(ros_cmd.data)

