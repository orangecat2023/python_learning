
# Program to convert USD to RMB based on the given exchange rate of 1 USD = 6.78 RMB.

def convert_usd_to_rmb():
    try:
        # Input from user
        usd_amount = float(input("请输入美元数值："))
        
        # Exchange rate
        exchange_rate = 6.78
        
        # Calculate RMB equivalent
        rmb_amount = usd_amount * exchange_rate
        
        # Output in the required format
        print(f"USD{usd_amount:.1f}=RMB{rmb_amount:.1f}")
    except ValueError:
        print("请输入有效的美元数值。")

# Run the conversion function
convert_usd_to_rmb()
