def getValue(x):
    a = 36
    b = 38
    if x <= a:
        return {"value":0, "message":"Tidak Demam"}
    elif x >= b:
        return {"value":1, "message":"Demam"}
    else:
        return {"value":abs(round(x-a/b-a, 2)), "message":"Probabilitas pasien terkena demam: "}

def showMessage():
    result = getValue(37)
    if result["value"]:
        print(f"{result['message']} {result['value']}")
    else:
        print(f"{result['message']}")

if __name__ == "__main__":
    showMessage()
    
def getValue(x):
    a = 36
    b = 38
    if x <= a:
        return "Tidak Demam"
    elif x >= b:
        return "Demam"
    else:
        return abs(round(x-a/b-a, 2))