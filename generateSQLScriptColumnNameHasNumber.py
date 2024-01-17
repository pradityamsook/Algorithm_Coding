def generateSQLScriptColumnNameHasNumberUpperSnakeCaseToUpperCase() -> None:

    strUpperSnakeCase = []

    with open("column_name.txt") as file:
        [strUpperSnakeCase.append(line.strip("\n")) for line in file.readlines()]
        file.close()

    with open("file_code_generate_from_column_name.txt", "w") as file:
        for tempIndex in range(0, len(strUpperSnakeCase)):
            res = ""
            finalScriptLine = ""
            checkIsNumeric = False
            for char in strUpperSnakeCase[tempIndex]:
                if char.isnumeric():
                    checkIsNumeric = True
                    break
            if checkIsNumeric is True:
                res = strUpperSnakeCase[tempIndex].replace("_", "")
                finalScriptLine = f"{strUpperSnakeCase[tempIndex]} AS {str(res)},"
            else:
                finalScriptLine = f"{strUpperSnakeCase[tempIndex]},"    
            file.writelines(f"{finalScriptLine}\n")
            # file.writelines(f"itemBusinessOwner.set{str(res)}(StringUtils.convNullToEmptyStr(String.valueOf(row.get(\"{strUpperSnakeCase[tempStr]}\"))));\n")
            
        file.close()
    print("\n\nDone!\n")

if __name__ == '__main__':
    generateSQLScriptColumnNameHasNumberUpperSnakeCaseToUpperCase()