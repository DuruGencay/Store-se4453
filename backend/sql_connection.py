import psycopg2

__cnx = None

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

key_vault_url = "https://musicstore-keyvault.vault.azure.net/"

credential = ClientSecretCredential(tenant_id, client_id, client_secret)
client = SecretClient(vault_url=key_vault_url, credential=credential)

secret_name = "duru-secret"
secret_value = client.get_secret(duru-secret)
print(f"Secret value: {secret_value.value}")

secret_name = "duru-username"
secret_value = client.get_secret(duru-username)
print(f"Secret value: {secret_value.value}")

try:
    # Bağlantı oluşturma
    connection = psycopg2.connect(
        user="postgres",
        password="Burçak",
        host="musicstore-server.postgres.database.azure.com",
        port="5432",
        database="grocery_store"
    )
    cursor = connection.cursor()

    # Bağlantı test sorgusu
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL sunucu sürümü: {db_version}")

except Exception as error:
    print(f"Bağlantı hatası: {error}")

finally:
    # Bağlantıyı kapatma
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection:
        connection.close()
        print("PostgreSQL bağlantısı kapatıldı.")


import os
import psycopg2

# Çevresel değişkenlerden PostgreSQL bilgilerini al
PGHOST = os.getenv("PGHOST")
PGUSER = os.getenv("PGUSER")
PGPORT = os.getenv("PGPORT")
PGDATABASE = os.getenv("PGDATABASE")
PGPASSWORD = os.getenv("PGPASSWORD")

# PostgreSQL'e bağlan
try:
    connection = psycopg2.connect(
        host=PGHOST,
        user=PGUSER,
        port=PGPORT,
        database=PGDATABASE,
        password=PGPASSWORD
    )
    print("PostgreSQL bağlantısı başarılı!")
except Exception as e:
    print("Bağlantı hatası:", e)



def get_sql_connection():
    global __cnx

    if __cnx is None:
        __cnx = psycopg2.connect(
            host="musicstore-server.postgres.database.azure.com",  # PGAdmin'deki host adresi
            port="5432",
            database="grocery_store",  # PostgreSQL veritabanı adı
            user="postgres",  # PostgreSQL kullanıcı adı
            password="Burçak"  # PostgreSQL şifresi
        )

    return __cnx
