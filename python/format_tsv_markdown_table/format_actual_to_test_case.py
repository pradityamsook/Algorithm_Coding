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

def format_table(rows, list_headers):
    """
    Format the list of rows into the desired table pattern.
    """

    header = ""
    for header_column in list_headers:
        header += f"| {header_column}"
    header += " |"
    
    table = [header]
    
    formatted_row = ""
    for row in rows:
        for header in list_headers:
            formatted_row += (f"| {row[header]:{len(header)}}")
        formatted_row += "|\n"
    table.append(formatted_row)
    
    # print(table)
    return "\n".join(table)

def main():
    # Need Handler manual change column names following the order of data test case
    # list_headers = ["store_id", "status_type", "effective_dt_of_store_status", "start_date", "end_date", "source_dt" ]

    with open("D:/sources/Algorithm_Coding/python/format_tsv_markdown_table/input.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    
    rows = []
    for line in content:
        line = line.strip()
        if line.startswith("! Row") or line.startswith("Row"):
            line = line.replace("! Row", "Row")
            rows.append(parse_row(line))
        if line.startswith("- Row"):
            line = line.replace("- Row", "Row")
            rows.append(parse_row(line))

    list_headers = []
    for keys in rows[0].keys():
        list_headers.append(keys)
        
    table = format_table(rows, list_headers)

    with open("D:/sources/Algorithm_Coding/python/format_tsv_markdown_table/output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(table)
    
    # print(table)
    print("\n************************** Format completed **************************\n")

if __name__ == "__main__":
    main()