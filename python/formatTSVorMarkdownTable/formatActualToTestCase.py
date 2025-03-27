import re

def parse_row(row_str):
    """
    Parse a single Row string and extract its key-value pairs as a dictionary.
    """
    row_str = row_str.strip().replace("Row(", "").replace(")", "")
    items = re.split(r",\s*", row_str)
    
    row_dict = {}
    for item in items:
        key, value = item.split("=")
        row_dict[key.strip()] = value.strip("'")
    
    return row_dict

def format_table(rows, listHeaders):
    """
    Format the list of rows into the desired table pattern.
    """
    # Need Handler manual change column names
    header = (
        "| store_id | store_size | effective_dt_of_store_size | start_date          | end_date            | source_dt  |"
    )
    
    table = [header]
    
    formatted_row = ""
    for row in rows:
        for header in listHeaders:
            formatted_row += (f"| {row[header]:{len(header)}}")
        formatted_row += "|\n"
    table.append(formatted_row)
    
    # print(table)
    return "\n".join(table)

def main():
    # Need Handler manual change column names
    listHeaders = ["store_id", "store_size", "effective_dt_of_store_size", "start_date", "end_date", "source_dt" ]

    with open("actualLog.txt", "r") as file:
        content = file.readlines()
    
    rows = []
    for line in content:
        line = line.strip()
        if line.startswith("! Row") or line.startswith("Row"):
            line = line.replace("! Row", "Row")
            rows.append(parse_row(line))
    
    table = format_table(rows, listHeaders)
    
    print(table)

if __name__ == "__main__":
    main()