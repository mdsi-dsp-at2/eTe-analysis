import pandas as pd
  
def find_all_age_suicide_rate(dataframe):
    # Calculate the total suicide rate of all different ages
    dataframe["all_age"] = dataframe["80_above"]+ dataframe["70to79"] + dataframe["60to69"]+ dataframe["50to59"]+ dataframe["40to49"]+ dataframe["30to39"]+ dataframe["20to29"] + dataframe["10to19"]
    return dataframe

def pivot_longer_age_columns_to_one(dataframe, is_include_allage = False):
    # Do Melting - Tranform/Combine the multiple  column names of different age groups into one column "Age"
    value_vars_list = ["80_above","70to79", "60to69", "50to59", "40to49", "30to39", "20to29", "10to19"]

    if is_include_allage :
        value_vars_list = value_vars_list.append("all_age")
     
    dataframe = pd.melt(dataframe, id_vars=["Country", "Sex"], value_vars=value_vars_list, var_name="Age",value_name="Suicide_rate")
    return dataframe
