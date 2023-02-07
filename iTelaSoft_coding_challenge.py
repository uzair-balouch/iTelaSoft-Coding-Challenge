import networkx as nx
import matplotlib.pyplot as plt
graphlml_file = nx.read_graphml('problem.graphml')

# Problem statement says if pot connected with cabinet via 10m cable then in verge then chambe rwould cost £1800 and £2000 from card A nd B respectively.
items = ['Cabinet', 'Trench/m (verge)', 'Trench/m (road)', 'Chamber', 'Pot']

# Card-A
cost_A = ['1000', '50', '100', '200', '100']

# Card-B
cost_B = ['1200', '40', '80', '200', '20'] # Pot is 20x trench length from Cabinet
def correct_cost():
    correccct_cost_list = []
    total_chamber_with_Newcost = 0
    total_Chamber = 0
    for node in graphlml_file.nodes(data=True):
        neighbors = [n for n in graphlml_file.neighbors(node[0])]
        for k,v in graphlml_file[node[0]].items():
            pass

        if node[1]['type'] == "Chamber":
            total_Chamber = total_Chamber + 1

        if node[1]['type'] == "Pot" and v['material'] == "verge" and v['length'] > 10:

            total_chamber_with_Newcost = total_chamber_with_Newcost + 1
            new_chamber_cost = 1800 # for card-A
            v['length'] = new_chamber_cost
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print(node[0],"is of type of", node[1]['type'], 'and connected with', neighbors ,'in', v['material'], 'with length of', v['length'], "===> Cost of Cabinet would increase £1,800 and £2,000 respectively from card A nd B")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            correccct_cost_list.append(v['length'])
        else:
            print(node[0],"is of type of", node[1]['type'], 'in', v['material'], 'with length of', v['length'])
            correccct_cost_list.append(v['length'])
    print("Total number of chamber connected with pot with greater than 10m of cable are: ", total_chamber_with_Newcost, '/', total_Chamber)
    print("New Cost of iTems: ",correccct_cost_list) # Cost for every Chamber is now increased to 1800 for Card-A
    cost_summation = sum(correccct_cost_list)
    return cost_summation


