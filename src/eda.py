import os
import matplotlib.pyplot as plt

def run_eda(df):
    os.makedirs("outputs", exist_ok=True)

    # 1. Sales by Region
    plt.figure()
    df.groupby("Region")["Sales"].sum().plot(kind="bar")
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.savefig("outputs/sales_by_region.png")
    plt.close()

    # 2. Marketing Spend vs Sales
    plt.figure()
    plt.scatter(df["Marketing_Spend"], df["Sales"])
    plt.title("Marketing Spend vs Sales")
    plt.xlabel("Marketing Spend")
    plt.ylabel("Sales")
    plt.savefig("outputs/marketing_vs_sales.png")
    plt.close()

    # 3. Profit Trend
    plt.figure()
    plt.plot(df["Date"], df["Profit"])
    plt.title("Profit Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Profit")
    plt.savefig("outputs/profit_trend.png")
    plt.close()
