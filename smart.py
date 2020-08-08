import string

nums = string.digits


variables = {}


def check_nums(str1):

    for x in str1:
        if x in nums:
            return False

    return True


def var_input(str1):
    if '=' in str1:
        var = str1.split("=")
        var = [x.strip(" ") for x in var]

        if str1.count("=") > 1:
            return "Invalid assignment"

        elif var[0].isalpha() == False:
            return "Invalid identifier"

        elif var[0] not in variables:
            if var[1].isdigit():
                variables[var[0]] = int(var[1])

            elif var[1] in variables:
                variables[var[0]] = variables[var[1]]

            else:
                return "Invalid assignment"

        elif var[0] in variables:
            if var[1].isdigit():
                variables[var[0]] = int(var[1])

            elif var[1] in variables:
                variables[var[0]] = variables[var[1]]

        else:
            return "Unknown Variable"

    elif "+" in str1 or "-" in str1 or "/" in str1 or "*" in str1 or "^" in str1:

        ans = operations(str1)
        return ans

    else:
        try:
            return variables[str1]

        except:
            return "Unknown Variable"


def operations(s1):

    global variables
    try:
        if "//" in s1:
            return 'Invalid expression'
        else:
            s_ = eval(s1, variables)

    except NameError as e:

        return "Invalid expression"

    except SyntaxError as e:

        return "Invalid expression"

    return s_


flag = True

while flag:

    num = input()
    if num == "/exit":
        flag = False

    elif num == "/help":
        print("+ means addition , -- means addition , --- means substraction")

    elif num == "":
        pass

    elif num.isalpha() == False and num.isdigit() == False:
        if num[0] == "/":
            print("Unknown Command")

        elif num != "/exit" or num != "/help":
            ans = var_input(num)
            if ans != None:
                if ans == "Invalid expression" or ans == "Unknown Variable" or ans == "Invalid identifier" or ans == "Invalid assignment":
                    print(ans)
                elif ans == int(ans) or ans == float(ans):
                    print(round(ans))
                else:
                    print(ans)

    elif num.isalpha() == False:

        if "/" in num:
            ans = var_input(num)
            if ans != None:
                if ans == "Invalid expression" or ans == "Unknown Variable" or ans == "Invalid identifier" or ans == "Invalid assignment":
                    print(ans)
                elif ans == int(ans) or ans == float(ans):
                    print(round(ans))
                else:
                    print(ans)

        elif num != "/exit" or num != "/help":
            ans = var_input(num)
            if ans != None:
                if ans == "Invalid expression" or ans == "Unknown Variable" or ans == "Invalid identifier" or ans == "Invalid assignment":
                    print(ans)
                elif ans == int(ans) or ans == float(ans):
                    print(round(ans))
                else:
                    print(ans)

        else:
            print("Unknown Command")

    elif num.isalpha() == True:

        ans = var_input(num)

        if ans != None:
            if ans == "Invalid expression" or ans == "Unknown Variable" or ans == "Invalid identifier" or ans == "Invalid assignment":
                print(ans)
            elif ans == int(ans) or ans == float(ans):
                print(round(ans))
            else:
                print(ans)

    elif len(num) == 1:
        print(int(num[0]))


print("Bye!")
