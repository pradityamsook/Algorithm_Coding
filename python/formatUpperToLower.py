def UpperToLower(listString: list) -> list:
    """
    Convert a list of strings to lowercase.
    """
    return [string.lower() for string in listString]

if __name__ == "__main__":
    listString = [
        "STORE_LSM_REGN",
        "STORE_LSM_REGN_NAME",
        "STORE_LSM_REGN_SEQUENCE"
    ]
    listString = UpperToLower(listString)
    # sql_insert_stg_config1 = f"""insert into "{"pipeline_process_schema"}".stg_configuration values """
    # for i in range(len(listString)):
    #     sql_insert_stg_config1 += f""" ('"{"table_n"}"_stg',{i},'{listString[i]}'                ,'string'),"""
    #     if (i == len(listString)-1):
    #         sql_insert_stg_config1 += f""" ('"{"table_n"}"_stg',{i},'{listString[i]}'                ,'string');"""
    print(listString) 