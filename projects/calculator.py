
while True:
    operation = str(input())

    if '+' in operation:
        element_list = operation.split('+')
        var1 = float(element_list[0].strip())
        var2 = float(element_list[1].strip())
        result = var1 + var2
        print(result)
    elif '-' in operation:
        element_list = operation.split('-')
        var1 = float(element_list[0].strip())
        var2 = float(element_list[1].strip())
        result = var1 - var2
        print(result)
    elif '/' in operation:
        element_list = operation.split('/')
        var1 = float(element_list[0].strip())
        var2 = float(element_list[1].strip())
        result = var1 / var2
        print(result)
    elif '*' in operation:
        element_list = operation.split('*')
        var1 = float(element_list[0].strip())
        var2 = float(element_list[1].strip())
        result = var1 * var2
        print(result)
