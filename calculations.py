def calcUpFrontCost(energy, type_list):
	up_front_cost = 0
	for type in type_list:
		up_front_cost += energy * type
	return up_front_cost

def calcTotalSystemCost(energy, sys_cost_list):
	total_sys_cost = 0
	for sys_cost in sys_cost_list:
		total_sys_cost += energy * sys_cost
	return total_sys_cost

def calcTotalSystemWithSubsidies(energy, sys_cost_list, subs_list):
	total_sys_cost = calcTotalSystemCost(energy, sys_cost_list)
	for sub in subs_list:
		total_sys_cost -= energy * sub
	return total_sys_cost