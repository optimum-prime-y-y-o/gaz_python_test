# Тестовое задание python разработчик

К реализации предлагается система учета и анализа данных, поступающих с условного устройства.  
Полученные данные привязываются к временной метке и устройству, с которого пришли данные,  
и сохраняются в БД. Набор данных используется для дальнейшего анализа. 

Ниже представлена схема БД, подходящая под все функциональные требования.  
В проекте используется только таблица DeviceStat, её достаточно для реализации всех обязательных требований
![db](https://github.com/optimum-prime-y-y-o/gaz_python_test/blob/master/%D1%81%D1%85%D0%B5%D0%BC%D0%B0.png)
## Запуск
```
docker-compose up -d --build
```
## Реализовано 2 эндпоинта

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/devices/{device_id}/stats/": {
      "post": {
        "summary": "Create Device Stat",
        "operationId": "create_device_stat_devices__device_id__stats__post",
        "parameters": [
          {
            "name": "device_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Device Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DeviceStatCreate"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "get": {
        "summary": "Get Device Stats",
        "operationId": "get_device_stats_devices__device_id__stats__get",
        "parameters": [
          {
            "name": "device_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Device Id"
            }
          },
          {
            "name": "start_date",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "string",
                  "format": "date-time"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Start Date"
            }
          },
          {
            "name": "end_date",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "string",
                  "format": "date-time"
                },
                {
                  "type": "null"
                }
              ],
              "title": "End Date"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    }
  }
```
