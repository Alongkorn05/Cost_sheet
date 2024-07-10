def convert(w):
    records = []
    for rec in w['data']:
        rec["input_data"] = { item["key"]: item["value"] for item in rec["input_data"] }
        records += [rec]
    return records

def super_ai(w):
    lis = []
    results = []
    for index, element in enumerate(w['data']):
        green = 0
        yel = 0
        red = 0
        salefactor = float(element["input_data"]["SaleFactors"])
        external = float(element["input_data"]["External"])

        if external < 0.30 and (salefactor > 1 or 1.00 <= salefactor <= 1.14):
            green = 1

        if (external < 0.30 or 0.90 <= salefactor <= 0.99) and (0.30 <= external <= 0.49 or salefactor >= 0.90):
            yel = 1

        if red + green + yel < 2:
            if external >= 0.50 or salefactor <= 0.89:
                red = 1

        if red + green + yel >= 2:
            print(f"Record {index}")
            result = 1
            print("Pass : ", result, " /Green = ", green, "/Yellow = ", yel, "/Red = ", red)
            print("")
        else:
            lis.append(w['data'][index])
            result = 0
            print(f"Record {index}")
            print("didn't Pass: ", result, " /Green = ", green, "/Yellow = ", yel, "/Red = ", red)
            print("")
            if green == 1:
                status = "Green"
            elif yel == 1:
                status = "Yellow"
            elif red == 1:
                status = "Red"
            else:
                status = "null"

            record_dict = {
                "id": lis[-1]["_id"],
                "External": lis[-1]["input_data"]["External"],
                "SaleFactors": lis[-1]["input_data"]["SaleFactors"],
                "State": status
            }

            results.append(record_dict)

    return results
