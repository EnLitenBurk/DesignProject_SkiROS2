from skiros2_common.core.primitive import *
from skiros2_skill.core.skill import *
from skiros2_common.core.params import ParamTypes

import sys, os
sys.path.append('/home/johansson/catkin_ws/src/skills/skills_dorna2/src/skills_dorna2')
from primitives import *

class Compound(SkillDescription):
    def createDescription(self):
        #=======Params=========
        pass

class drop_off(SkillBase):
    def createDescription(self):
        self.setDescription(Compound(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(SerialStar()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
              self.skill("MOVE_r3_and_update","r3_TAKE3", ""),
              self.skill("cubes_and_update()","GEN_cube", ""),
              self.skill("MOVE_r3_and_update", "r3_PRE_TAKE", ""),
              self.skill("MOVE_r3_and_update","r3_LEAVE", "")
        )

class scan_cube(SkillBase):
    def createDescription(self):
        self.setDescription(Compound(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(SerialStar()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(self.skill(ParallelFf())(
                    self.skill("MOVE_r1_and_update","r1_LEAVE", ""),
                    self.skill("Compound","drop_off", "")
                ),
                self.skill("grip_and_update", "CLOSE_gripper", ""),
                self.skill("MOVE_r1_and_update", "r1_SCAN", ""),
                self.skill("Compound", "SCAN", "")
    
        )

class SCAN(SkillBase):
    def createDescription(self):
        self.setDescription(Compound(), self.__class__.__name__)

    def expand(self, skill):
        skill.setProcessor(SerialStar()) #SerialStar, Selector, ParallelFf, ParallelFs
        skill(
                  self.skill("scan_and_update", "light_and_update","", specify = {"On/Off":True}),
                  self.skill("scan_and_update", "camera_and_update", ""),
                  self.skill("scan_and_update", "light_and_update", "", specify = {"On/Off":False})
        )
