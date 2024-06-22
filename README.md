# Cargo Backend project не полный

## Запуск проекта

1. Клонируйте репозиторий и перейдите в директорию проекта:
    ```bash
    git clone <URL>
    cd cargo_backend
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    # venv\Scripts\activate  # Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Запустите сервер:
    ```bash
    uvicorn main:app --reload
    ```

## Эндпоинты API

### TrackCode
- **POST /trackCodes/**: Создать продукт с трек кодом и с данными по местоположению.
- **GET /trackCodes/{track_code}**: Получить информацию о конкретном продукте.
- **PATCH /trackCodes/{track_code}**: Обновить информацию о конкретном продукте.
- **DELETE /trackCodes/{track_code}**: Удалить продукт.

## Применение эндпойнтов API

1. В теле запроса **POST /trackCodes/** отправляется json объект с нужными данными для создания продукта в базе данных:
    - **trackCode** типа **int**. Соответсвенно сам трек коди в виде числа.
    - **dateRegistrationClient** типа **boolean**. Дата регистраций клиента. Тут вопрос был ли данный товар регистрирован клиентом? Если да то отправляется **true**, если нет то **false**.
    - **receivedInStockInChina** типа **boolean**. Продукт доставлено ли на склад в Китае? Если да то отправляется **true**, если нет то **false**.
    - **receivedAtTheWarehouseInAlmaty** типа **boolean**. Продукт доставлено ли на склад в Алмате? Если да то отправляется **true**, если нет то **false**.
    - **receivedByTheClient** типа **boolean**. Продукт был ли получен клиентом? Если да то отправляется **true**, если нет то **false**.

Пример отпрвки json объекта:
    ```json
    {
    "trackCode": 123456789,
    "dateRegistrationClient": true,
    "receivedInStockInChina": true,
    "receivedAtTheWarehouseInAlmaty": false,
    "receivedByTheClient": false
    }
    ```

2. В запросе **GET /trackCodes/{track_code}** вместо **track_code** пишется номер трек кода.

3. В теле запроса **PATCH /trackCodes/{track_code}** отправляется json объект с нужными данными для обновления продукта, а вместо **track_code** пишется номер трек кода.

4. В запросе **DELETE /trackCodes/{track_code}** вместо **track_code** пишется номер трек кода.