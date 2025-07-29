clients = [
{"name":"rem","age":35,"spend":5000},
{"name":"rem2","age":25,"spend":50},
{"name":"rem3","age":35,"spend":0},
{"name":"rem4","age":25,"spend":5000},
]
for client in clients:
    if client["age"] > 30 and client["spend"] > 1000:
        print (client["name"],"high value")
    elif  client["age"] < 30 and client["spend"] < 1000:
        print(client["name"],"low value")
    elif client["spend"] == 0:
        continue
    else:
        print(client["name"],"regular")