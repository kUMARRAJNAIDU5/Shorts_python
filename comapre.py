def format_sd_algo_data_dev(sd_stepid_algo_data):
    algo_keys_list = []
    for val in sd_stepid_algo_data.values():
        if val in algo_keys_list:
            continue
        else:
            algo_keys_list.append(val)
    print("algo_keys_list :", algo_keys_list)
    lst_algo_data_convert = ['[]', "['cats']"]

    # lst_algo_data_convert=json.loads(algo_list_data)
    print("lst_algo_data_convert", lst_algo_data_convert)
    algo_keys_list = lst_algo_data_convert
    new_dict = {}
    alsgos = ""
    # Result data from SD with searching for keys algo's
    for key in lst_algo_data_convert:
        alsgos = key
        print("key", key)
        d2 = {k: v for k, v in sd_stepid_algo_data.items() if v in [key]}
        new_dict[key] = d2.keys()
    print("new_dict", new_dict)
    print('******************************')
    # initialize dictionary
    dict_sd_format_adt = {}
    # display data in tuple format...
    for k, v in new_dict.items():
        dict_sd_format_adt[k] = tuple(v)
    print('******************************')
    data_formatter_stepids_algo = ""
    stepid_algo_result_data = {}
    for i in lst_algo_data_convert:
        stepid_data_algo = {key: set(value) for key, value in dict_sd_format_adt.items() if key == i}
        # print('key--',i)
        # print('lst_algo_data_convert--', lst_algo_data_convert)
        # print("data_algo_stepid", stepid_data_algo)
        data_formatter_stepids_algo += str(stepid_data_algo).replace("('", "[").replace("')", "]")
        stepid_algo_result_data[i] = data_formatter_stepids_algo

    Result = data_formatter_stepids_algo.replace(": {", ": [").replace("}}{", "],").replace("}}", "]}")
    print("Result", Result)
    return Result
