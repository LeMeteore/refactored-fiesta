import pandas as pd

def create_dataframe():
    df = pd.DataFrame({
        "Pays": ["Mali", "Senegal", "Guinea", "Togo"],
        "Président": ["Assimi Goita", "Macky Sall", "Mamady Doumbouya", "Faure Gnassingbé"]
    }, index=["a", "b", "c", "d"])

    return df


if __name__ == "__main__":
    df = create_dataframe()
    print(df)
