def generateScriptPatternFromUpperSnakeCaseToCamelCase() -> None:
    print("## You can use '@' is variable of code generate. ##")
    print("## Example try '@' is word: String varStr = \"@\"")
    print("\t\tString varStr = word\n")
    scriptPattern = input("Input your script: ")

    listScriptPattern = scriptPattern.split("@")

    strUpperSnakeCase = []

    with open("column_name.txt") as file:
        [strUpperSnakeCase.append(line.strip("\n")) for line in file.readlines()]
        file.close()

    with open("file_code_generate_from_column_name.txt", "w") as file:
        for tempStr in range(0, len(strUpperSnakeCase)):
            temp = strUpperSnakeCase[tempStr].split("_")
            for index in range(0, len(temp)):
                temp[index] = temp[index].lower()
            res = ''.join(ele.title() for ele in temp[0:])
            finalScriptLine = listScriptPattern[0] + str(res) + listScriptPattern[1] + strUpperSnakeCase[tempStr] + listScriptPattern[2]
            file.writelines(f"{finalScriptLine}\n")
            # file.writelines(f"itemBusinessOwner.set{str(res)}(StringUtils.convNullToEmptyStr(String.valueOf(row.get(\"{strUpperSnakeCase[tempStr]}\"))));\n")
            
        file.close()
    print("\n\nDone!\n")

if __name__ == '__main__':
    generateScriptPatternFromUpperSnakeCaseToCamelCase()