from skiros2_skill.core.skill import SkillDescription, ParamOptions
from skiros2_common.core.params import ParamTypes
from skiros2_common.core.world_element import Element
from skiros2_common.core.primitive import PrimitiveBase
import rospy
from std_msgs.msg import String
import turtlesim.msg as ts
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn as SpawnSrv
import threading
import numpy

import numpy as np
import math

import roslib
import json


ros_sub = String()
ros_sub.data = '{\"r1\":{\"act_pos\": \"unknown\"},\"r3\":{\"act_pos\": \"unknown\"},\"control_box\":{\"blue_light_on\": false},\"camera\":{\"scanning\": false, \"done\": false},\"gripper\":{\"closed\": false, \"part_sensor\":false},\"cubes\":{\"sensor\": false}}'


msg_dir = {"r1":{"ref_pos": "scan"},"r3":{"ref_pos": "leave"},"control_box":{"blue_light": True},"camera":{"do_scan": False},"gripper":{"close": False},"cubes":{"make_cube": True,"remove_cube": False}}

def _ros_state_callback(msg):
    ros_sub.data = msg.data

ros_sub_node = rospy.Subscriber("state", String, _ros_state_callback)

def get_state():
    return ros_sub.data

#################################################################################
# Listen
#################################################################################
class Listen(SkillDescription):
    def createDescription(self):
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)


class listen(PrimitiveBase):
    def createDescription(self):
        self.setDescription(Listen(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Preempted")

    def onEnd(self):
        return True

    def onStart(self):
        #self.pose_pub = rospy.Publisher('/test', String, queue_size=1)
        return True



    def execute(self):
        Robot = self.params["Robot"].value
        state_cmd = json.loads(get_state())
        
        r1_act_pos = state_cmd["r1"]["act_pos"]
        r3_act_pos = state_cmd["r3"]["act_pos"]
        blue_light = state_cmd["control_box"]["blue_light_on"]
        cam_scanning = state_cmd["camera"]["scanning"]
        cam_done_scanning = state_cmd["camera"]["done"]
        gripper_closed = state_cmd["gripper"]["closed"]
        gripper_part_sensor = state_cmd["gripper"]["part_sensor"]
        cube_sensor = state_cmd["cubes"]["sensor"]

        Robot.setProperty("owl_name:r1_act_pos", r1_act_pos)
        Robot.setProperty("owl_name:r3_act_pos", r3_act_pos)
        Robot.setProperty("owl_name:blue_light",blue_light)
        Robot.setProperty("owl_name:cam_scanning",cam_scanning)
        Robot.setProperty("owl_name:cam_done_scanning",cam_done_scanning)
        Robot.setProperty("owl_name:gripper_closed",gripper_closed)
        Robot.setProperty("owl_name:gripper_part_sensor",gripper_part_sensor)
        Robot.setProperty("owl_name:cube_sensor",cube_sensor)
        
        self.params["Robot"].value = Robot
        return self.step("New pos updated")
        
        
        
#################################################################################
# Listen_ones
#################################################################################
class Listen_once(SkillDescription):
    def createDescription(self):
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)


class listen_once(PrimitiveBase):
    def createDescription(self):
        self.setDescription(Listen_once(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Preempted")

    def onEnd(self):
        return True

    def onStart(self):
        return True

    def execute(self):
        Robot = self.params["Robot"].value
        state_cmd = json.loads(get_state())
        
        r1_act_pos = state_cmd["r1"]["act_pos"]
        r3_act_pos = state_cmd["r3"]["act_pos"]
        blue_light = state_cmd["control_box"]["blue_light_on"]
        cam_scanning = state_cmd["camera"]["scanning"]
        cam_done_scanning = state_cmd["camera"]["done"]
        gripper_closed = state_cmd["gripper"]["closed"]
        gripper_part_sensor = state_cmd["gripper"]["part_sensor"]
        cube_sensor = state_cmd["cubes"]["sensor"]

        Robot.setProperty("owl_name:r1_act_pos", r1_act_pos)
        Robot.setProperty("owl_name:r3_act_pos", r3_act_pos)
        Robot.setProperty("owl_name:blue_light",blue_light)
        Robot.setProperty("owl_name:cam_scanning",cam_scanning)
        Robot.setProperty("owl_name:cam_done_scanning",cam_done_scanning)
        Robot.setProperty("owl_name:gripper_closed",gripper_closed)
        Robot.setProperty("owl_name:gripper_part_sensor",gripper_part_sensor)
        Robot.setProperty("owl_name:cube_sensor",cube_sensor)
        
        self.params["Robot"].value = Robot
        
        return self.success("execute finished")

 
# #################################################################################
# # Talk_R1 (can scan)
# #################################################################################


# class Talk_R1(SkillDescription):
#     def createDescription(self):
#         self.addParam("r1_ref_pos", str, ParamTypes.Required)
#         self.addParam("blue_light", bool, ParamTypes.Required)
#         self.addParam("do_scan", bool, ParamTypes.Required)
#         self.addParam("gripper", bool, ParamTypes.Required)


# class talk_R1(PrimitiveBase):
#     def createDescription(self):
#         self.setDescription(Talk_R1(), self.__class__.__name__)

#     def _send_command(self, r1_pos, blue_light, do_scan, gripper):
#         msg = String()
#         msg_dir["r1"]["ref_pos"] = r1_pos
#         msg_dir["control_box"]["blue_light"] = blue_light
#         msg_dir["camera"]["do_scan"] = do_scan
#         msg_dir["gripper"]["close"] = gripper
#         msg.data = json.dumps(msg_dir)
#         self.pose_pub.publish(msg)

#     def onPreempt(self):
#         return self.success("Preempted")

#     def onEnd(self):
#         # self._send_command()
#         return True

#     def onStart(self):
#         self.pose_pub = rospy.Publisher('/cmd', String, queue_size=1)
#         return True

#     def execute(self):
#         self._send_command(self.params["r1_ref_pos"].value, self.params["blue_light"].value, self.params["do_scan"].value, self.params["gripper"].value)
#         return self.step("sending message")

# #################################################################################
# # Talk_R3 (can spawn)
# #################################################################################


# class Talk_R3(SkillDescription):
#     def createDescription(self):
#         self.addParam("r3_ref_pos", str, ParamTypes.Required)
#         self.addParam("make_cube", bool, ParamTypes.Required)
#         self.addParam("remove_cube", bool, ParamTypes.Required)


# class talk_R3(PrimitiveBase):
#     def createDescription(self):
#         self.setDescription(Talk_R3(), self.__class__.__name__)

#     def _send_command(self, r3_pos, make_cube, remove_cube):
#         msg = String()
#         msg_dir["r3"]["ref_pos"] = r3_pos
#         msg_dir["cubes"]["make_cube"] = make_cube
#         msg_dir["cubes"]["remove_cube"] = remove_cube
#         msg.data = json.dumps(msg_dir)
#         self.pose_pub.publish(msg)

#     def onPreempt(self):
#         return self.success("Preempted")

#     def onEnd(self):
#         # self._send_command()
#         return True

#     def onStart(self):
#         self.pose_pub = rospy.Publisher('/cmd', String, queue_size=1)
#         return True

#     def execute(self):
#         self._send_command(self.params["r3_ref_pos"].value, self.params["make_cube"].value, self.params["remove_cube"].value)
#         return self.step("Test step")


