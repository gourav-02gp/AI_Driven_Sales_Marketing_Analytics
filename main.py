from src.data_preprocessing import load_and_clean_data
from src.eda import run_eda
from src.model import train_model, predict_sales

def main():
    print("Loading data...")
    df = load_and_clean_data()

    print("Running EDA...")
    run_eda(df)

    print("Training ML model...")
    model = train_model(df)

    spend = float(input("Enter marketing spend amount: "))
    predicted_sales = predict_sales(model, spend)

    print("Predicted Sales:", round(predicted_sales, 2))
    print("Project executed successfully!")

if __name__ == "__main__":
    main()
