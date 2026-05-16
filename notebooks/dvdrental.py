import marimo
import pandas as pd
__generated_with = "0.23.1"
app = marimo.App(width="medium", sql_output="pandas")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import os
    import sqlalchemy

    _password = os.environ.get("POSTGRES_PASSWORD", "npg_Q6pYH9caGkjI")
    DATABASE_URL = (
        f"postgresql://neondb_owner:{_password}"
        "@ep-wispy-snow-a8m6tctu-pooler.eastus2.azure.neon.tech/dvdrental?sslmode=require"
    )

    engine = sqlalchemy.create_engine(DATABASE_URL)
    return (engine,)

@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 1

    Lista los distintos valores de `rating` presentes en `film`, ordenados alfabéticamente.
    """)
    return

@app.cell(hide_code=True)
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT DISTINCT rating FROM film ;
        """,
        engine=engine
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 2

    Muestra las 20 películas más largas con `title`, `length`, `rating` y `rental_rate`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 3

    Encuentra todos los clientes inactivos (`active = 0`) mostrando `customer_id`, nombre completo y email.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 4

    Lista los clientes de la tienda 1 (`store_id = 1`) con `customer_id`, nombre completo y email.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 5

    Cuenta cuántas películas hay por cada `release_year`. Incluye también las filas donde el año sea `NULL`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 6

    Muestra los actores cuyo `last_name` empieza por `S`, ordenados por apellido y nombre.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 7

    Encuentra las películas con `replacement_cost` entre 20 y 25 y `rating = 'PG-13'`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 8

    Calcula, para los alquileres ya devueltos, la duración del alquiler en días usando `return_date - rental_date`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 9

    Muestra las películas cuyo título contiene la palabra `LOVE`, sin distinguir mayúsculas/minúsculas.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 10

    Encuentra las películas cuyo campo `special_features` contiene `Behind the Scenes`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 11

    Lista todas las películas con su idioma (`film.title`, `language.name`).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 12

    Muestra cada película junto con todos sus actores (`film.title`, nombre completo del actor).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 13

    Muestra cada película junto con todas sus categorías (`film.title`, `category.name`).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 14

    Lista los clientes con su ciudad y país (`customer`, `address`, `city`, `country`).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 15

    Muestra cada alquiler con `rental_id`, fecha de alquiler, nombre del cliente y título de la película alquilada.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 16

    Lista todos los pagos con el cliente que pagó y el empleado (`staff`) que atendió la transacción.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 17

    Cuenta cuántas copias de cada película hay en inventario por tienda.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 18

    Encuentra las películas que nunca han sido agregadas al inventario.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 19

    Encuentra los actores que nunca han participado en películas con `rating = 'R'`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 20

    Muestra cada tienda con el nombre completo de su gerente, ciudad y país.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 21

    Cuenta cuántas películas hay por `rating`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 22

    Calcula la duración promedio y la tarifa de alquiler promedio por categoría.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 23

    Calcula el monto total pagado por cada cliente y ordénalos de mayor a menor.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 24

    Cuenta cuántos alquileres ocurrieron por mes usando `date_trunc('month', rental_date)`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 25

    Calcula los ingresos totales por tienda usando la tabla `payment`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 26

    Encuentra los clientes con más de 30 alquileres.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 27

    Obtén el top 10 de actores con más películas en las que han participado.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 28

    Encuentra las categorías con costo de reemplazo promedio mayor a 20.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 29

    Calcula qué porcentaje del catálogo representa cada `rating` sobre el total de películas.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 30

    Calcula la mediana de `amount` en `payment` por cliente usando funciones de percentil de PostgreSQL.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 31

    Encuentra las películas cuya duración (`length`) es mayor que la duración promedio de todas las películas.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 32

    Encuentra los clientes cuyo gasto total supera el gasto total promedio por cliente.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 33

    Encuentra las películas que pertenecen a la misma categoría que `ACADEMY DINOSAUR`, excluyendo la propia película.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 34

    Encuentra los clientes que nunca han realizado un alquiler.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 35

    Encuentra las películas que han sido alquiladas al menos una vez en cada tienda.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 36

    Encuentra las categorías cuyo número de películas es mayor que el promedio de películas por categoría.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 37

    Para cada `rating`, muestra las películas cuyo `rental_rate` es mayor que el promedio de su mismo `rating`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 38

    Encuentra los actores que han trabajado en al menos una película de todas las categorías existentes.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 39

    Encuentra los clientes que han pagado al menos un monto superior al promedio global de pagos.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 40

    Encuentra las películas que nunca han sido alquiladas por clientes de la tienda 2.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 41

    Usa un CTE para calcular por cliente: número de alquileres, total pagado y ticket promedio.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 42

    Usa un CTE para obtener la primera y la última fecha de alquiler de cada cliente.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 43

    Construye un CTE que derive los ingresos por película a partir de `payment -> rental -> inventory -> film`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 44

    Usa un CTE para clasificar clientes en `low`, `medium` y `high value` según su gasto total.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 45

    Construye una tabla de cohortes por mes de creación de cliente (`customer.create_date`) y cuenta cuántos hicieron su primer alquiler en cada mes.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 46

    Usa CTEs para detectar posibles clientes duplicados con mismo nombre, apellido y dirección.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 47

    Calcula la utilización del inventario por tienda: copias totales, copias alquiladas al menos una vez y porcentaje de utilización.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 48

    Usa un CTE para encontrar la película más alquilada dentro de cada categoría.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 49

    Construye una consulta tipo 'vista analítica' con una fila por cliente que incluya datos demográficos, geografía, número de alquileres y gasto total.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 50

    Genera con CTEs una tabla mensual por tienda con `rentals`, `revenue`, `unique_customers` y `avg_payment_amount`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 51

    Rankea a los clientes por gasto total dentro de cada tienda usando `dense_rank()`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 52

    Calcula el acumulado diario de ingresos usando `sum(amount) over (...)`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 53

    Calcula el promedio móvil de 7 días del número de alquileres diarios.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 54

    Obtén el top 3 de películas más alquiladas por categoría usando `row_number()` o `dense_rank()`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 55

    Para cada cliente, calcula los días transcurridos entre un alquiler y el siguiente usando `lag()`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 56

    Calcula el percentil de longitud de cada película dentro de su `rating` usando `percent_rank()` o `cume_dist()`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 57

    Obtén el primer y el último pago de cada cliente usando funciones ventana.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 58

    Calcula qué proporción del revenue de cada tienda aporta cada empleado (`staff`).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 59

    Calcula el acumulado mensual de alquileres por categoría a lo largo del tiempo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 60

    Encuentra los clientes cuyo último pago fue mayor que su promedio histórico de pagos.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 61

    Identifica alquileres devueltos tarde: aquellos donde los días alquilados superan `film.rental_duration`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 62

    Compara cuántos alquileres se hicieron en fines de semana vs días de semana.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 63

    Calcula los clientes activos por mes (`monthly active customers`).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 64

    Calcula el tiempo promedio de devolución por categoría.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 65

    Encuentra el trimestre con mayores ingresos en cada año.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 66

    Analiza el patrón horario: alquileres e ingresos por hora del día.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 67

    Encuentra clientes inactivos: aquellos que no alquilaron nada en los últimos 90 días del dataset.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 68

    Construye una tabla de retención: mes de primera compra vs clientes que repiten en los meses 1, 2 y 3.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 69

    Calcula la mediana de días entre alquileres consecutivos para clientes recurrentes.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 70

    Calcula cuánto revenue genera cada cliente en sus primeros 30 días desde `create_date`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 71

    Construye una métrica tipo CLV por cliente con `total_revenue`, `total_rentals` y `avg_payment_amount`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 72

    Define churn como 'sin alquiler en los últimos 60 días del dataset' y calcula la tasa de churn por tienda.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 73

    Encuentra pares de categorías que suelen ser consumidas por los mismos clientes (cross-sell).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 74

    Encuentra los pares de actores que más veces han participado juntos en una misma película.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 75

    Identifica películas con alta demanda pero bajo inventario: muchas rentas y pocas copias disponibles.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 76

    Compara las preferencias de categoría entre tiendas y muestra en qué categorías difieren más.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 77

    Obtén el top 3 de categorías por ingresos dentro de cada país.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 78

    Analiza la relación entre duración de la película y revenue generado, segmentando por `rating`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 79

    Construye una segmentación RFM (`recency`, `frequency`, `monetary`) para los clientes.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 80

    Evalúa la productividad de `staff`: pagos procesados, revenue total y ticket promedio por empleado.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 81

    Escribe una consulta que audite cuántos `NULL` hay por columna en la tabla `customer`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 82

    Verifica si existen pagos con `amount <= 0`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 83

    Busca emails duplicados en `customer`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 84

    Detecta alquileres donde `return_date` sea anterior a `rental_date`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 85

    Verifica integridad referencial lógica buscando registros huérfanos entre `payment`, `rental`, `inventory`, `customer` y `staff`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 86

    Genera una consulta incremental basada en `last_update` para extraer solo cambios recientes de `film`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 87

    Construye una consulta que produzca una fact table diaria a nivel `store_id`, `film_id`, `date` con `rentals`, `revenue` y `unique_customers`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 88

    Crea una consulta que compare el revenue total de `payment` contra el revenue atribuido a películas y detecte diferencias.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 89

    Escribe la consulta base para una vista materializada mensual por tienda y categoría.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 90

    Diseña una consulta que detecte clientes potencialmente fusionables usando similitud en nombre, apellido y dirección.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 91

    Para cada país, devuelve el top 5 de clientes por revenue incluyendo empates.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 92

    Devuelve una sola fila por cliente con: categoría favorita, actor favorito, última fecha de alquiler y gasto total.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 93

    Encuentra las películas cuya cantidad de alquileres en el último mes disponible al menos se duplicó respecto al mes anterior.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 94

    Detecta pagos anómalos: montos que estén a más de 3 desviaciones estándar del promedio diario de su tienda.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 95

    Encuentra las categorías cuya contribución porcentual al revenue ha crecido por al menos 3 meses consecutivos.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 96

    Para cada tienda, encuentra el conjunto mínimo de películas que explica el 80% de los alquileres (análisis de Pareto).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 97

    Identifica clientes cuyo mix de categorías en sus últimos 5 alquileres es muy distinto de su historial previo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 98

    Encuentra los clientes que han alquilado al menos una película de todas las categorías disponibles en su tienda habitual.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 99

    Construye un funnel por cliente: creado -> primer alquiler -> segundo alquiler dentro de 30 días.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Pregunta 100

    Construye una consulta ejecutiva mensual por tienda con `active_customers`, `rentals`, `revenue`, `AOV`, `avg_return_days`, `pct_late_returns` y `top_category`.
    """)
    return


if __name__ == "__main__":
    app.run()
