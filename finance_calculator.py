def calculate_finances(monthly_income:float, tax_rate:float, currency:str, house_rent:float, food_rent:float, coaching_membership:float, bpfc_rent:float) -> None:
    yearly_salary : float = monthly_income * 12
    monthly_tax : float = monthly_income * tax_rate / 100
    yearly_tax : float = monthly_tax * 12
    monthly_net_income : float = monthly_income - monthly_tax
    yearly_net_income : float = yearly_salary - yearly_tax

    print("------------------------------------------------")

    print(f"The Monthly income: {currency} {monthly_income:,.2f}")
    print(f"Tax rate: {tax_rate:,.2f}%")
    print(f"Monthly tax: {currency} {monthly_tax:,.2f}")
    print(f"Monthly Net Income: {currency} {monthly_net_income:,.2f}")
    print(f"Yearly Salary: {currency} {yearly_salary:,.2f}")
    print(f"Yearly Tax Paid: {currency} {yearly_tax:,.2f}")
    print(f"Yearly Net Income: {currency} {yearly_net_income:,.2f}")

    print("------------------------------------------------")

    print(f"House Rent: {currency} {house_rent:,.2f}")
    print(f"Food Rent: {currency} {food_rent:,.2f}")
    print(f"Coaching Membership: {currency} {coaching_membership:,.2f}")
    print(f"Bpfc Rent: {currency} {bpfc_rent:,.2f}")

    remaining_salary : float = monthly_net_income - house_rent - food_rent - coaching_membership - bpfc_rent
    print("---------------------------------------------")
    print(f"Remaining Salary: {currency} {remaining_salary:,.2f}")
    print("----------------------------------------------")

def main() -> None:
    try:
        monthly_income : float = float(input("Enter Your Monthly Salary: "))
        tax_rate : float = float(input("Enter Your Tax Rate: "))
        currency : str = input("Enter Your Currency: ")
        house_rent : float = float(input("Enter house Rent: "))
        food_rent : float = float(input("Enter Food Rent: "))
        coaching_membership : float = float(input("Enter NxtWave Rent: "))
        bpfc_rent : float = float(input("Enter football fees: "))

    except ValueError:
        print()
        print("Enter a valid Number.")
        print()
        main()
        return


    calculate_finances(monthly_income,tax_rate,currency,house_rent,food_rent,coaching_membership,bpfc_rent)

if __name__ == "__main__":
    main()

