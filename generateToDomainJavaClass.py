def generateScriptPatternFromUpperSnakeCaseToCamelCase() -> None:

    strUpperSnakeCase = []

    with open("column_name.txt") as file:
        [strUpperSnakeCase.append(line.strip("\n")) for line in file.readlines()]
        file.close()

    with open("file_code_generate_from_column_name.txt", "w") as file:
        for tempStr in range(0, len(strUpperSnakeCase)):
            temp = strUpperSnakeCase[tempStr].split("_")
            for index in range(0, len(temp)):
                temp[index] = temp[index].lower()
            resCamelCase = temp[0] + ''.join(ele.title() for ele in temp[1:])
            resUpperCamelCase = ''.join(ele.title() for ele in temp[0:])
            finalScriptLine = f"param.put(\"{resCamelCase}\", oneTouchPmaSaleInput.get{resUpperCamelCase}());"
            file.writelines(f"{finalScriptLine}\n")
            # file.writelines(f"itemBusinessOwner.set{str(res)}(StringUtils.convNullToEmptyStr(String.valueOf(row.get(\"{strUpperSnakeCase[tempStr]}\"))));\n")
            
        file.close()
    print("\n\nDone!\n")

if __name__ == '__main__':
    generateScriptPatternFromUpperSnakeCaseToCamelCase()