import pyodbc


def conectar():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=DESKTOP-LJNH04A;"
        "DATABASE=SistemaLogin;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )