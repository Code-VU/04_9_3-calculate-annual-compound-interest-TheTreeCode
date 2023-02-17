def getACompoundInterest():
    while True:
        try:
            client_one_principal = float(input("Principle (amount): "))
            break
        except:
            print("Please enter only numeric values without any text or special charachters.")
            continue
    while True:
        try:
            client_one_time = float(input("Time:               "))
            break
        except:
            print("Please enter only numeric values without any text or special charachters.")
            continue
    while True:
        try:
            client_one_rate = float(input("Rate:               "))
            break
        except:
            print("Please enter only numeric values without any text or special charachters.")
            continue
    return [client_one_principal, client_one_time, client_one_rate]

def calculateCompoundInterest():
    #Amount=PrincipalAmount(1+InterestRate/100)**Time
    #CompoundInterest=Amount-PrincipalAmount
    principal_time_rate_LIST = getACompoundInterest()
    #The fuction being passed to the principal_time... variable returns a list with [principal, time, rate].
    a = principal_time_rate_LIST[0]*(1+principal_time_rate_LIST[2]/100)**principal_time_rate_LIST[1]
    ci = round(a - principal_time_rate_LIST[0],2)
    print("Compound Interest: "+str(ci))

calculateCompoundInterest()
print("---")
calculateCompoundInterest()
print("---")
calculateCompoundInterest()
    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
