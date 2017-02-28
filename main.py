#dictionary that gives the index into the energy list for
#that energy type
index_dict = {'solar': 0, 'wind': 1, 'coal': 2, 'nuclear': 3, 
'gas': 4, 'hydroelectric': 5, 'biomass': 6}

#list of dictionaries holding k:v pairs of all info for that energy
energy_list = [
{'front': 109.8, 'total_sys': 125.3, 'total_with_sub': 114.3, 'external': 9.9},
{'front': 57.7, 'total_sys': 196.9, 'external': 21.3},
{'front': 60.4, 'total_sys': 95.1, 'external': 120.7},
{'front': 70.1, 'total_sys': 95.2},
{'front':40.7, 'total_sys': 141.5, 'external': 94.6},
{'front': 70.7, 'total_sys': 83.5},
{'front': 47.1, 'total_sys': 100.5, 'external': 13}
]

class DTE:
	#dict of {type: percent}
	energy_dict = {'coal': .7419, 'nuclear': .1725, 'gas':.0372, 'hydroelectric':.0026, 'biomass':.0115, 'solar':.0013, 'wind':.0330}
	total_energy = 500000

class MyScenario:
	#dict of {type: percent}
	energy_dict = {'wind': .0115, 'solar': .9885}
	backup_energy = 41666.67

	def __init__(self, energy = None):
		if energy is None:
			self.total_energy = 652000
		else:
			self.total_energy = energy

def calcCostOfStr(scenario, str):
	cost = 0
	for k in scenario.energy_dict:
		energy = scenario.total_energy * scenario.energy_dict[k]
		if str in energy_list[index_dict[k]]:
			cost += energy_list[index_dict[k]][str] * energy
		else:
			cost += energy_list[index_dict[k]]['total_sys'] * energy
	return cost

def calcSocietalCost(scenario):
	cost = calcCostOfStr(scenario, 'total_with_sub')
	for k in scenario.energy_dict:
		energy = scenario.total_energy * scenario.energy_dict[k]
		if 'external' in energy_list[index_dict[k]]:
			cost += energy_list[index_dict[k]]['external'] * energy
	return cost

def calcBackUp(scenario, str):
	cost = 0
	energy = scenario.backup_energy
	cost += energy_list[index_dict[str]]['total_sys'] * energy
	if 'external' in energy_list[index_dict[str]]:
		cost += energy_list[index_dict[str]]['external'] * energy
	if str == 'hydroelectric':
		cost *= 2
	return cost

def main():
	solarwind = MyScenario()
	print 'total_energy: {0}'.format(solarwind.total_energy)
	print 'my up_front = {0}'.format(calcCostOfStr(solarwind, 'front'))
	print 'my total_sys = {0}'.format(calcCostOfStr(solarwind,'total_sys'))
	print 'my sys_with_sub = {0}'.format(calcCostOfStr(solarwind,'total_with_sub'))
	print 'my societal_total = {0}\n'.format(calcSocietalCost(solarwind))

	adj_solar = MyScenario(500000)
	print 'total_energy: {0}'.format(adj_solar.total_energy)
	print 'adj up_front = {0}'.format(calcCostOfStr(adj_solar, 'front'))
	print 'adj total_sys = {0}'.format(calcCostOfStr(adj_solar, 'total_sys'))
	print 'adj sys_with_sub = {0}'.format(calcCostOfStr(adj_solar, 'total_with_sub'))
	print 'adj societal_total = {0}\n'.format(calcSocietalCost(adj_solar))


	dte = DTE()
	print 'dte up_front = {0}'.format(calcCostOfStr(dte, 'front'))
	print 'dte total_sys = {0}'.format(calcCostOfStr(dte, 'total_sys'))
	print 'dte sys_with_sub = {0}'.format(calcCostOfStr(dte, 'total_with_sub'))
	print 'dte societal_total = {0}\n'.format(calcSocietalCost(dte))

	#backup info
	print 'Cost of hydroelectric backup = {0}'.format(calcBackUp(solarwind, 'hydroelectric'))
	print 'Cost of natural gas backup = {0}'.format(calcBackUp(solarwind, 'gas'))

if __name__ == '__main__':
	main()