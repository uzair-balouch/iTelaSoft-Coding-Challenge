import networkx as nx
import matplotlib.pyplot as plt
graphlml_file = nx.read_graphml('problem.graphml')

# print("------------Detail about Graph--------------")
# # print(graphlml_file)
# print("-----------------------------------------")

# print("*************** Node ******************")
# print(list(graphlml_file.nodes))
# print(graphlml_file['A']['F'])
# print(graphlml_file['B']['F'])
# print(graphlml_file['C']['G'])
# print(graphlml_file['D']['H'])
# print(graphlml_file['E']['H'])
# print(graphlml_file['F'])
# # print(graphlml_file['B'])
# print("***************************************")


# print("++++++++++++++ Edges ++++++++++++++++++")
# print(list(graphlml_file.edges))
# print(list(graphlml_file.adj['F']))  # or 
# # print(list(graphlml_file.neighbors(1)))
# print("++++++++++++++++++++++++++++++++++++++")

for node in graphlml_file.nodes(data=True):
    # print(graphlml_file[node[0]])
    for k,v in graphlml_file[node[0]].items():
        pass
    # print(k,v)
    print(node[0],"is of type of", node[1]['type'], 'in', v['material'], 'with length of', v['length'])
    # print(node[0]," is of type ", node[1]['type'] ,graphlml_file[node[0]])

# nx.draw(graphlml_file, with_labels = True )
# plt.show()


# Rate Card A
# Item	Cost (£)
# Cabinet	1000
# Trench/m (verge)	50
# Trench/m (road)	100
# Chamber	200
# Pot	100


	# Rate Card B
	# Item	Cost (£)
	# Cabinet	1200
	# Trench/m (verge)	40
	# Trench/m (road)	80
	# Chamber	200
	# Pot	20x trench length from Cabinet


























import networkx as nx
import matplotlib.pyplot as plt
graphlml_file = nx.read_graphml('problem.graphml')

# Problem statement says if pot connected with cabinet via 10m cable then in verge then chambe rwould cost £1800 and £2000 from card A nd B respectively.
items = ['Cabinet', 'Trench/m (verge)', 'Trench/m (road)', 'Chamber', 'Pot']

# Card-A
cost_A = ['1000', '50', '100', '200', '100']

# Card-B
cost_B = ['1200', '40', '80', '200', '20'] # P0t is 20x trench length from Cabinet
def correct_cost():
    correccct_cost_list = []
    total_chamber_with_Newcost = 0
    total_pot = 0
    total_Cabinet = 0
    total_Chamber = 0
    for node in graphlml_file.nodes(data=True):
        neighbors = [n for n in graphlml_file.neighbors(node[0])]
        for k,v in graphlml_file[node[0]].items():
            pass
        if node[1]['type'] == "Pot":
            total_pot = total_pot + 1
        if node[1]['type'] == "Cabinet":
            total_Cabinet = total_Cabinet + 1
        if node[1]['type'] == "Chamber":
            total_Chamber = total_Chamber + 1

        if node[1]['type'] == "Pot" and v['material'] == "verge" and v['length'] > 10:

            total_chamber_with_Newcost = total_chamber_with_Newcost + 1
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print(node[0],"is of type of", node[1]['type'], 'and connected with', neighbors ,'in', v['material'], 'with length of', v['length'], "===> Cost of Cabinet would increase £1,800 and £2,000 respectively from card A nd B")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            correccct_cost_list.append(v['length'])
        else:
            print(node[0],"is of type of", node[1]['type'], 'in', v['material'], 'with length of', v['length'])
            correccct_cost_list.append(v['length'])
    print("Total number of chamber connected with pot with greater than 10m of cable are: ", total_chamber_with_Newcost, '/', total_Chamber)
    # print("Total number of Pots are: ", total_pot)
    # print("Total number of Cabinets are: ", total_Cabinet)
    # print("Total number of Chamber are: ", total_Chamber)
    # print(correccct_cost_list)
    # print('*********************** New Cost of Table **************************************')
    print(" Items -------- Costs")
    print(items, '--------', cost_A)
    cost_summation = sum(correccct_cost_list)
    # print("Total Cost would be", cost_summation)
    return cost_summation
print(correct_cost())

# nx.draw(graphlml_file, with_labels = True )
# plt.show()


# Rate Card A
# Item	Cost (£)
# Cabinet	1000
# Trench/m (verge)	50
# Trench/m (road)	100
# Chamber	200
# Pot	100


	# Rate Card B
	# Item	Cost (£)
	# Cabinet	1200
	# Trench/m (verge)	40
	# Trench/m (road)	80
	# Chamber	200
	# Pot	20x trench length from Cabinet

