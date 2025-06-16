import json

def merge_lists_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)


    list1 = data['list1']
    list2 = data['list2']
    i, j = 0, 0
    merged_list = []
    
    while i < len(list1) and j < len(list2):
        if list1[i]['year'] <= list2[j]['year']:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1


    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    

    result = {
        "list0": merged_list
    }

    print(json.dumps(result, indent=2))





    


