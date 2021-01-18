import pymel.core as pm

def getJoints(node, joint_list):
    for child in node.getChildren():
        joint_list.append(child)
        if child.numChildren() > 0:
            getJoints(child, joint_list)
            
def parentSkeletons(s_joint_list, t_joint_list):
	i = 0
	
	while i < len(s_joint_list):
		pm.parentConstraint(s_joint_list[i], t_joint_list[i])
		i += 1
            
def main():
    selection = pm.selected()
    root = selection[0]  # First selection
    target_root = selection[1]  # Second selection

    s_jnt_list = []  # List of source joints
    t_jnt_list = []  # List of target joints

    s_jnt_list.append(root) #Adds source root joint to source joint list
    t_jnt_list.append(target_root) #Adds target root joint to target joint list
    getJoints(root, s_jnt_list) #Attends children source joints to source joint list
    getJoints(target_root, t_jnt_list) #Appends children target joints to target joint list
    parentSkeletons(t_jnt_list, s_jnt_list)