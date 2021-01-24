from skiros2_common.core.primitive import *
from skiros2_skill.core.skill import *
from skiros2_common.core.params import ParamTypes

# from descriptions import TestPrimitive


# from skiros2_common.core.params import ParamTypes
from skiros2_common.core.world_element import Element
# from skiros2_common.core.primitive import PrimitiveBase
from skiros2_common.core.conditions import ConditionProperty, ConditionHasProperty, ConditionRelation

import rospy
# from std_msgs.msg import String
# import turtlesim.msg as ts
# from geometry_msgs.msg import Twist
# from turtlesim.srv import Spawn as SpawnSrv
import threading, numpy
import json
import roslib
import time
import sys, os
sys.path.append('/home/johansson/catkin_ws/src/skills/skills_dorna2/src/skills_dorna2')
from help_cmds import *
from control_primitives import *

import numpy as np
import math

############################
### Move robot primitives
############################


class MOVE_r3(SkillDescription):
    def createDescription(self):
        #=======Params=========
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)

class r3_pre_take(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r3(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r3", "pre_take")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r3_act_pos").value
        if curr_pos == "pre_take":
            return self.success("r3 in pre_take")
        return self.step("r3 moving to pre_take")

class r3_leave(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r3(), self.__class__.__name__)


    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r3", "leave")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r3_act_pos").value
        if curr_pos == "leave":
            return self.success("r3 in leave")
        return self.step("r3 moving to leave")

class r3_take1(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r3(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r3", "take1")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r3_act_pos").value
        if curr_pos == "take1":
            return self.success("r3 in take1")
        return self.step("r3 moving to take1")

class r3_take2(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r3(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r3", "take2")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r3_act_pos").value
        if curr_pos == "take2":
            return self.success("r3 in take2")
        return self.step("r3 moving to take2")

class r3_take3(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r3(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r3", "take3")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r3_act_pos").value
        if curr_pos == "take3":
            return self.success("r3 in take3")
        return self.step("r3 moving to take3")

class MOVE_r1(SkillDescription):
    def createDescription(self):
        #=======Params=========
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)

class r1_pre_take(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r1(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r1", "pre_take")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r1_act_pos").value
        if curr_pos == "pre_take":
            return self.success("r1 in pre_take")
        return self.step("r1 moving to pre_take")

class r1_leave(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r1(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r1", "leave")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r1_act_pos").value
        if curr_pos == "leave":
            return self.success("r1 in leave")
        return self.step("r1 moving to leave")

class r1_take1(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r1(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r1", "take1")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r1_act_pos").value
        if curr_pos == "take1":
            return self.success("r1 in take1")
        return self.step("r1 moving to take1")

class r1_take2(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r1(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r1", "take2")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r1_act_pos").value
        if curr_pos == "take2":
            return self.success("r1 in take2")
        return self.step("r1 moving to take2")

class r1_take3(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r1(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r1", "take3")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r1_act_pos").value
        if curr_pos == "take3":
            return self.success("r1 in take3")
        return self.step("r1 moving to take3")

class r1_scan(PrimitiveBase):
    def createDescription(self):
        self.setDescription(MOVE_r1(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "r1", "scan")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:r1_act_pos").value
        if curr_pos == "scan":
            return self.success("r1 in scan")
        return self.step("r1 moving to scan")

#####################################################3
#### MOVE and UPDATE pos
#####################################################
###### R1

class MOVE_r3_and_update(SkillDescription):
    def createDescription(self):
        #=======Params=========
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)


class r3_PRE_TAKE(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r3_and_update(), self.__class__.__name__)
        self.addPreCondition(ConditionProperty('Not in pre_take', 'owl_name:r3_act_pos', 'Robot', '=', 'pre_take', False))
        self.addPostCondition(ConditionProperty('In pre_take', 'owl_name:r3_act_pos', 'Robot', '=', 'pre_take', True))


    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r3","r3_pre_take",""),
              self.skill("Listen", "listen","")
        )

class r3_TAKE1(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r3_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r3","r3_take1",""),
              self.skill("Listen", "listen","")
        )
class r3_TAKE2(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r3_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r3","r3_take2",""),
              self.skill("Listen", "listen","")
        )
class r3_TAKE3(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r3_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r3","r3_take3",""),
              self.skill("Listen", "listen","")
        )
class r3_LEAVE(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r3_and_update(), self.__class__.__name__)
        self.addPreCondition(ConditionProperty('Not in leave', 'owl_name:r3_act_pos', 'Robot', '=', 'leave', False))
        self.addPostCondition(ConditionProperty('In Leave', 'owl_name:r3_act_pos', 'Robot', '=', 'leave', True))


    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r3","r3_leave",""),
              self.skill("Listen", "listen","")
        )


##### R1
class MOVE_r1_and_update(SkillDescription):
    def createDescription(self):
        #=======Params=========
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)


class r1_PRE_TAKE(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r1_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r1","r1_pre_take",""),
              self.skill("Listen", "listen","")
        )

class r1_TAKE1(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r1_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r1","r1_take1",""),
              self.skill("Listen", "listen","")
        )
class r1_TAKE2(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r1_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r1","r1_take2",""),
              self.skill("Listen", "listen","")
        )
class r1_TAKE3(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r1_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r1","r1_take3",""),
              self.skill("Listen", "listen","")
        )
class r1_LEAVE(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r1_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r1","r1_leave",""),
              self.skill("Listen", "listen","")
        )

class r1_SCAN(SkillBase):
    def createDescription(self):
        self.setDescription(MOVE_r1_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r1","r1_scan",""),
              self.skill("Listen", "listen","")
        )


###############
### Cube control
###############
class CUBES(SkillDescription):
    def createDescription(self):
        #=======Params=========
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)

class gen_cube(PrimitiveBase):
    def createDescription(self):
        self.setDescription(CUBES(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "cubes", "generate")
        return True

    def onEnd(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "cubes", "stop_generate")
        return True
    
    def onInit(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "cubes", "stop_generate")
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:cube_sensor").value
        if curr_pos is True:
            return self.success("new cube generated")
        return self.step("generating cube")

class del_cube(PrimitiveBase):
    def createDescription(self):
        self.setDescription(CUBES(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "cubes", "remove")
        return True

    def onInit(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "cubes", "stop_remove")
        return True

    def onEnd(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "cubes", "stop_generate")
        ros_cmd.data = update_cmd(ros_cmd.data, "cubes", "stop_remove")
        return True

    def execute(self):
        Robot = self.params["Robot"].value
        curr_pos = Robot.getProperty("owl_name:cube_sensor").value
        if curr_pos is False:
            return self.success("cube deleted")
        return self.step("deleting cube")

class cubes_and_update(SkillDescription):
    def createDescription(self):
        #=======Params=========
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)  
        self.addPreCondition(ConditionProperty('Not in pre_take', 'owl_name:r3_act_pos', 'Robot', '=', 'pre_take', False))
        # self.addPostCondition(ConditionProperty('In pre_take', 'owl_name:r3_act_pos', 'Robot', '=', 'pre_take', ))


class GEN_cube(SkillBase):
    def createDescription(self):
        self.setDescription(cubes_and_update(), self.__class__.__name__)


    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("CUBES","gen_cube",""),
              self.skill("Listen", "listen","")
        )

class DEL_cube(SkillBase):
    def createDescription(self):
        self.setDescription(cubes_and_update(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("CUBES","del_cube",""),
              self.skill("Listen", "listen","")
        )

##########################
# Gripper
##########################
class Gripper(SkillDescription):
    def createDescription(self):
        #=======Params=========
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)


class close_gripper(PrimitiveBase):
    def createDescription(self):
        self.setDescription(Gripper(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        self.index = 0
        ros_cmd.data = update_cmd(ros_cmd.data, "gripper", True)
        return True

    def onEnd(self):
        return True
    
    def onInit(self):
        return True


    def execute(self):
        Robot = self.params["Robot"].value
        # gripper_status = Robot.getProperty("owl_name:gripper_closed").value
        # part_status = Robot.getProperty("owl_name:gripper_part_sensor").value
        # if gripper_status == True and part_status == True:
            # return self.success("Gripper Succesfully picked up cube")
        # elif gripper_status == True and part_status == False:
        self.index += 1
        if self.index > 12:
            return self.success("Gripper attempted to close")
                # ros_cmd.data = update_cmd(ros_cmd.data, "gripper", False)
        return self.step("Closing Gripper") 


class open_gripper(PrimitiveBase):
    def createDescription(self):
        self.setDescription(Gripper(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "gripper", False)
        return True

    def onInit(self):
        return True

    def onEnd(self):
        return True

    def execute(self):
        Robot = self.params["Robot"].value
        gripper_status = Robot.getProperty("owl_name:gripper_closed").value
        if gripper_status == False:
            return self.success("Gripper is Open")
        return self.step("Opening Gripper")


class check_gripper(PrimitiveBase):
    def createDescription(self):
        self.setDescription(Gripper(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        # ros_cmd.data = update_cmd(ros_cmd.data, "gripper", False)
        return True

    def onInit(self):
        return True

    def onEnd(self):
        return True

    def execute(self):
        Robot = self.params["Robot"].value
        gripper_status = Robot.getProperty("owl_name:gripper_closed").value
        part_status = Robot.getProperty("owl_name:gripper_part_sensor").value
        if gripper_status == True and part_status == True:
            return self.success("Picked up cube sucessfully")
        ros_cmd.data = update_cmd(ros_cmd.data, "gripper", False)
        return self.fail("gripper failed",-1)


class grip_and_update(SkillDescription):
    def createDescription(self):
        # #=======Params=========
        pass
        # self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)  
        # self.addPreCondition(ConditionProperty('Not in pre_take', 'owl_name:r3_act_pos', 'Robot', '=', 'pre_take', False))
        # self.addPostCondition(ConditionProperty('In pre_take', 'owl_name:r3_act_pos', 'Robot', '=', 'pre_take', ))

class OPEN_gripper(SkillBase):
    def createDescription(self):
        self.setDescription(grip_and_update(), self.__class__.__name__)


    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("Gripper","open_gripper",""),
              self.skill("Listen", "listen","")
        )

class CLOSE_gripper(SkillBase):
    def createDescription(self):
        self.setDescription(grip_and_update(), self.__class__.__name__)


    def expand(self, skill):
        skill.setProcessor(Serial()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(self.skill(Serial())(
            self.skill("Listen_once", "listen_once",""),
            self.skill("Gripper","close_gripper",""),
            self.skill("Listen_once", "listen_once",""),
            self.skill("Gripper", "check_gripper","")
            )
        
        )
 



##########################
# # Camera and light
##########################
class Scanning(SkillDescription):
    def createDescription(self):
        #=======Params=========
        self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)
        self.addParam("On/Off", True, ParamTypes.Required)
        self.addPreCondition(ConditionProperty('r1 in scan', 'owl_name:r1_act_pos', 'Robot', '=', 'scan', True))

class camera(PrimitiveBase):
    def createDescription(self):
        self.setDescription(Scanning(), self.__class__.__name__)
        self.addPreCondition(ConditionProperty('light on', 'owl_name:blue_light', 'Robot', '=', 'True', True))

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "camera", True)
        return True

    def onEnd(self):
        ros_cmd.data = update_cmd(ros_cmd.data, "camera", False)
        return True
    
    def onInit(self):
        return True

    def execute(self):
        Robot = self.params["Robot"].value
        status = Robot.getProperty("owl_name:cam_scanning").value
        status_done = Robot.getProperty("owl_name:cam_done_scanning").value
        if status_done == True:
            return self.success("Scan complete")
        return self.step("Scanning") 


class blue_light(PrimitiveBase):
    def createDescription(self):
        self.setDescription(Scanning(), self.__class__.__name__)

    def onPreempt(self):
        return self.success("Stopped")

    def onStart(self):
        # self.params["On/Off"].value
        ros_cmd.data = update_cmd(ros_cmd.data, "control_box", self.params["On/Off"].value)
        return True

    def onEnd(self):
        # ros_cmd.data = update_cmd(ros_cmd.data, "blue_light", False)
        return True
    
    def onInit(self):
        return True

    def execute(self):
        Robot = self.params["Robot"].value
        status = Robot.getProperty("owl_name:blue_light").value
        # status_done = Robot.getProperty("owl_name:cam_done_scanning").value
        if status == self.params["On/Off"].value :
            return self.success("Light done")
        return self.step("Light on") 



class scan_and_update(SkillDescription):
    def createDescription(self):
        # #=======Params=========
        self.addParam("On/Off", True, ParamTypes.Required)
        # self.addParam("Robot", Element("cora:Robot"), ParamTypes.Required)  
        # self.addPreCondition(ConditionProperty('Not in pre_take', 'owl_name:r3_act_pos', 'Robot', '=', 'pre_take', False))
        # self.addPostCondition(ConditionProperty('In pre_take', 'owl_name:r3_act_pos', 'Robot', '=', 'pre_take', ))

class light_and_update(SkillBase):
    def createDescription(self):
        self.setDescription(scan_and_update(), self.__class__.__name__)


    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("Scanning","blue_light","", specify = {"On/Off":self.params["On/Off"].value}),
              self.skill("Listen", "listen","")
        )

class camera_and_update(SkillBase):
    def createDescription(self):
        self.setDescription(scan_and_update(), self.__class__.__name__)


    def expand(self, skill):
        skill.setProcessor(ParallelFs()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("Scanning","camera",""),
              self.skill("Listen", "listen","")
        )




















