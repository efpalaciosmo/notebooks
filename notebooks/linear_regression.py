import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium", sql_output="pandas")


@app.cell
def _():
    from __future__ import annotations

    import marimo as mo

    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt

    from sklearn.model_selection import train_test_split
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline

    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import OneHotEncoder, StandardScaler

    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    return (
        ColumnTransformer,
        LinearRegression,
        OneHotEncoder,
        Pipeline,
        SimpleImputer,
        StandardScaler,
        mean_absolute_error,
        mean_squared_error,
        mo,
        np,
        pd,
        plt,
        r2_score,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Load dataset
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv("data/cardataset.csv")
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    print(f"Shape: {df.shape}")
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Transform columns
    """)
    return


@app.cell
def _(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    print(df.columns.to_list())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Transform columns with string
    """)
    return


@app.cell
def _(df):
    for col in df.columns:
        if df[col].dtype == "object" or df[col].dtype == str:
            df[col] = df[col].str.lower().str.replace(" ", "_")

    df.head()
    return


@app.cell
def _(mo):
    mo.md("""
    Remove duplicated
    """)
    return


@app.cell
def _(df):
    print(f"Number of null values {df['msrp'].isnull().sum()}")
    return


@app.cell
def _(df):
    df.drop_duplicates(inplace=True)
    print(f"Shape after remove duplicates {df.shape}")
    return


@app.cell
def _(df):
    df.dropna(subset=["msrp"], inplace=True)
    return


@app.cell
def _(mo):
    mo.md("""
    EDA
    """)
    return


@app.cell
def _(df, mo, plt):
    mo.md("Target Distribution")

    plt.figure(figsize=(8, 5))
    plt.hist(df["msrp"], bins=50)
    plt.title("Distribution ef MSRP")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df, np, plt):
    plt.figure(figsize=(8, 5))
    plt.hist(np.log1p(df["msrp"]), bins=50)
    plt.title("Distribution of log(MSRP)")
    plt.xlabel("log(Price)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df, plt):
    missing = df.isnull().sum()[df.isnull().sum() > 0].sort_values(ascending=True)

    if len(missing)>0:
        plt.figure(figsize=(8, 5))
        missing.plot(kind="bar")
        plt.title("Missing values")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
    return


@app.cell
def _(df, plt):
    avg_price = (
        df.groupby(by=["make"])['msrp']
        .mean().round(2)
        .sort_values(ascending=False)
        .head(15)
    )

    plt.figure(figsize=(8, 6))
    plt.barh(avg_price.index, avg_price.values)
    plt.title("Top 15 brands by average msrp")
    plt.xlabel("Average Price")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""
    Correlation matrix
    """)
    return


@app.cell
def _(df, plt):
    numeric_df = df.select_dtypes(include=["int64", "float64"])

    corr = numeric_df.corr()

    plt.figure(figsize=(8, 6))
    plt.imshow(corr, aspect="auto")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""
    Features / Target
    """)
    return


@app.cell
def _(df, np):
    TARGET = "msrp"
    USE_LOG_TARGET = True

    X = df.drop(columns=[TARGET])
    _y = df[TARGET]

    if USE_LOG_TARGET:
        y = np.log1p(_y)

    numeric_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    numeric_features
    return USE_LOG_TARGET, X, numeric_features, y


@app.cell
def _(X):
    categorical_features = X.select_dtypes(
        include=["object", "str"]
    ).columns.tolist()

    categorical_features
    return (categorical_features,)


@app.cell
def _(mo):
    mo.md("""
    Preprocessing Pipeline
    """)
    return


@app.cell
def _(
    ColumnTransformer,
    OneHotEncoder,
    Pipeline,
    SimpleImputer,
    StandardScaler,
    categorical_features,
    numeric_features,
):
    numeric_transformer = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    categorical_transformer = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    preprocessor
    return (preprocessor,)


@app.cell
def _(mo):
    mo.md("""
    Model Pipeline
    """)
    return


@app.cell
def _(LinearRegression, Pipeline, preprocessor):
    model = Pipeline(
        steps = [
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression())
        ]
    )

    model
    return (model,)


@app.cell
def _(X, mo, train_test_split, y):
    mo.md("Train / Test Split")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )
    return X_test, X_train, y_test, y_train


@app.cell
def _(mo):
    mo.md("""
    Train Model
    """)
    return


@app.cell
def _(X_train, model, y_train):
    model.fit(X_train, y_train)
    return


@app.cell
def _(mo):
    mo.md("""
    Predictions
    """)
    return


@app.cell
def _(X_test, model):
    predictions = model.predict(X_test)
    return (predictions,)


@app.cell
def _(USE_LOG_TARGET, np, predictions, y_test):
    # Reverse log transform if used
    if USE_LOG_TARGET:
        y_test_eval = np.expm1(y_test)
        predicctions_eval = np.expm1(predictions)
    else:
        y_test_eval = y_test
        predicctions_eval = predictions

    return predicctions_eval, y_test_eval


@app.cell
def _(mo):
    mo.md("""
    Metrics
    """)
    return


@app.cell
def _(
    mean_absolute_error,
    mean_squared_error,
    np,
    predicctions_eval,
    r2_score,
    y_test_eval,
):
    mae = mean_absolute_error(y_test_eval, predicctions_eval)
    rmse = np.sqrt(mean_squared_error(y_test_eval, predicctions_eval))
    r2 = r2_score(y_test_eval, predicctions_eval)

    print("\n======================")
    print("MODEL PERFORMANCE")
    print("======================")
    print("MAE :", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R2  :", round(r2, 4))

    return


@app.cell
def _(plt, predicctions_eval, y_test_eval):
    plt.figure(figsize=(8, 5))
    plt.scatter(y_test_eval, predicctions_eval, alpha=0.4)
    plt.title("Actual vs Predicte Price")
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(plt, predicctions_eval, y_test_eval):
    residuals = y_test_eval - predicctions_eval

    plt.figure(figsize=(8, 5))
    plt.scatter(predicctions_eval, residuals, alpha=0.4)
    plt.axhline(0, linestyle="--")
    plt.title("Residual Plot")
    plt.xlabel("Predicted Price")
    plt.ylabel("Residual")
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""
    Sample Prediction
    """)
    return


@app.cell
def _(pd):
    new_car = pd.DataFrame([{
        "make": "bmw",
        "model": "3_series",
        "year": 2016,
        "engine_fuel_type": "premium_unleaded_(required)",
        "engine_hp": 300,
        "engine_cylinders": 6,
        "transmission_type": "automatic",
        "driven_wheels": "rear_wheel_drive",
        "number_of_doors": 4,
        "market_category": "luxury,performance",
        "vehicle_size": "midsize",
        "vehicle_style": "sedan",
        "highway_mpg": 31,
        "city_mpg": 22,
        "popularity": 3916
    }])
    return (new_car,)


@app.cell
def _(USE_LOG_TARGET, model, new_car, np):
    pred_new = np.expm1(model.predict(new_car)) if USE_LOG_TARGET else model.predict(new_car)

    return (pred_new,)


@app.cell
def _(pred_new):
    print("\nEstimated price of new car:")
    print(round(pred_new[0], 2))
    return


@app.cell
def _(mo, model):
    mo.md("Feature Corfficients")

    reg = model.named_steps["regressor"]
    print(f"Intercept: {reg.intercept_}")
    print(f"Number of learned coefficents: {reg.coef_}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Matemáticas detrás del proyecto de predicción de precio de carros

    ## 1. Problema supervisado

    Dado un vector de características

    $$
    x = (x_1,x_2,\dots,x_p),
    $$

    queremos aprender una función

    $$
    f:\mathbb{R}^p \to \mathbb{R}
    $$

    tal que

    $$
    \hat y = f(x),
    $$

    donde $y$ es el precio real del carro y $\hat y$ el precio predicho.

    ---

    ## 2. Matriz de datos

    Con $n$ observaciones:

    $$
    X \in \mathbb{R}^{n \times p}, \qquad
    y \in \mathbb{R}^{n}.
    $$

    Cada fila de $X$ representa un vehículo.

    ---

    ## 3. One-Hot Encoding

    Si una variable categórica tiene $k$ categorías, se transforma en vectores base:

    $$
    c_i \mapsto e_i \in \mathbb{R}^k,
    $$

    donde $e_i$ tiene un 1 en la posición $i$ y 0 en las demás.

    ---

    ## 4. Escalamiento estándar

    Para una variable numérica $x_j$:

    $$
    z_j = \frac{x_j-\mu_j}{\sigma_j},
    $$

    donde $\mu_j$ es la media y $\sigma_j$ la desviación estándar.

    ---

    ## 5. Regresión lineal

    El modelo supone:

    $$
    \hat y = \beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p.
    $$

    Forma matricial:

    $$
    \hat y = X\beta + \beta_0 \mathbf{1}.
    $$

    ---

    ## 6. Función de costo

    Se minimiza la suma de errores cuadrados:

    $$
    RSS(\beta) = \sum_{i=1}^{n} (y_i-\hat y_i)^2.
    $$

    Problema:

    $$
    \min_{\beta_0,\beta} RSS(\beta).
    $$

    ---

    ## 7. Solución cerrada

    Agregando una columna de unos a $X$:

    $$
    \tilde X = [\mathbf{1}\; X],
    $$

    la solución clásica es:

    $$
    \hat\beta = (\tilde X^\top \tilde X)^{-1}\tilde X^\top y.
    $$

    ---

    ## 8. Interpretación geométrica

    $\hat y$ es la proyección ortogonal de $y$ sobre el espacio columna de $\tilde X$:

    $$
    \hat y = P_{\operatorname{col}(\tilde X)}(y).
    $$

    El residual

    $$
    r = y-\hat y
    $$

    cumple

    $$
    \tilde X^\top r = 0.
    $$

    ---

    ## 9. Transformación logarítmica

    Para reducir sesgo en precios altos:

    $$
    y' = \log(1+y).
    $$

    Luego de predecir en escala log:

    $$
    \hat y = e^{\hat y'} - 1.
    $$

    ---

    ## 10. Métricas

    ### MAE

    $$
    MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat y_i|.
    $$

    ### MSE

    $$
    MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2.
    $$

    ### RMSE

    $$
    RMSE = \sqrt{MSE}.
    $$

    ### Coeficiente $R^2$

    $$
    R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i-\hat y_i)^2}{\sum_{i=1}^{n}(y_i-\bar y)^2},
    $$

    donde

    $$
    \bar y = \frac{1}{n}\sum_{i=1}^{n} y_i.
    $$

    ---

    ## 11. Residuos

    Para cada observación:

    $$
    r_i = y_i-\hat y_i.
    $$

    Idealmente deben verse centrados en 0 y sin patrón.

    ---

    ## 12. Predicción final

    Para un carro nuevo $x_{new}$:

    $$
    \hat y_{new} = \beta_0 + \sum_{j=1}^{p}\beta_j x_{new,j}.
    $$

    Si se usó log-transform:

    $$
    \hat y_{new} = \exp\!\left(\beta_0+\sum_{j=1}^{p}\beta_j x_{new,j}\right)-1.
    $$

    ---

    ## 13. Resumen del pipeline

    $$
    X_{raw} \xrightarrow{T} X_{proc} \xrightarrow{\text{fit}} \hat\beta
    \xrightarrow{\text{predict}} \hat y.
    $$

    donde $T$ incluye imputación, escalamiento y codificación categórica.
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


if __name__ == "__main__":
    app.run()
