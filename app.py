import pandas as pd

def create_dataframe():
    """A function to create a DataFrame"""

    df = pd.DataFrame({
        "Pays": ["Mali", "Senegal", "Guinea"],
        "Président": ["Assimi Goita", "Macky Sall", "Mamady Doumbouya"]
    }, index=["a", "b", "c"])

    return df


if __name__ == "__main__":
    df = create_dataframe()
    print(df)
