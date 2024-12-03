# About the project ***`API_regression_with_inference`***

### Ноутбук с EDA/Model: [Здесь](src/ml/notebooks/regression_with_inference_pro.ipynb)


-----
## Демонстрация работы `API + Ridge regression model`

- **Swagger UI документация для сервиса Car Price Predictor на базе FastAPI**

![swagger.png](assets/swagger.png)

- **Эндпоинты:**
  - **POST** `/predict_item` — используется для предсказания стоимости машины по переданным признакам одного объекта
  - **POST** `/predict_items` — используется для предсказания стоимости нескольких машин по признакам из загруженного CSV-файла
  - **GET** `/` — корневой маршрут

### Предсказание одного объекта

- **Пример работы сервиса `№1`:**

![img.png](assets/img.png)

- **Пример работы сервиса `№2`:**

![img_1.png](assets/img_1.png)

### Предсказание нескольких объектов, на основе переданных признаков в csv-файле

- **Пример работы сервиса:**

![img_2.png](assets/img_2.png)

![img_3.png](assets/img_3.png)