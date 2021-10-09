def reverse_dictionary(d):
    new_dict = {}
    
    for i in d:
        for j in d[i]:
            try:
                new_dict[j].append(i)
            except:
                new_dict[j] = [i]

    return(new_dict)