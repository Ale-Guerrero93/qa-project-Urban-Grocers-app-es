import configuration
import requests
import data
import json


def get_docs():
  return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def get_logs():
  return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)


def get_users_table():
  return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_new_user(body):
  return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                       json=body,  # inserta el cuerpo de solicitud
                       headers=data.headers)  # inserta los encabezados


def post_products_kits(products_ids):
  return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                       json=products_ids,
                       headers=data.headers)


def post_new_kit(body, auth_token):
  headers = data.headers
  headers["Authorization"] = f"Bearer {auth_token}"

  payload = json.dumps(body)

  return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                       headers=headers,
                       data=payload
                       )
