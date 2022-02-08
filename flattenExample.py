
sample_dict = {"class": "comp490",
               "cap":24,
               "outcomes":[
                   {"number":1,
                       "name": "work in groups",
                    "origen": "alumni"},
                   {"number":2,
                       "name": "Ethical Dilemmas",
                    "origen": "Local Hiring Managers"}
               ]}

def flatten_dict(dictionary_with_list):
    flat_dict = {}
    flat_dict['class'] = dictionary_with_list['class']
    flat_dict['cap']= dictionary_with_list['cap']
    for outcome_val in dictionary_with_list["outcomes"]:
        new_key_base = f"outcome {outcome_val['number']}"
        name_key = f"{new_key_base}_name"
        flat_dict[name_key]=outcome_val["name"]
        origen_key = f"{new_key_base}_origen"
        flat_dict[origen_key] = outcome_val["origen"]
    return flat_dict

def main():
    new_flat_version = flatten_dict(sample_dict)
    print(new_flat_version)

if __name__ == '__main__':
    main()
