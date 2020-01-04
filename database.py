from pydbwrapper import Database, Config

import hashlib
import os
import re
import sys

import common.system_variable as s

# if os.environ.get("DATABASE_URL"):
CONFIG = Config(
    config_dict={
        "host": s.DATABASE_HOST,
        "port": int(s.DATABASE_PORT),
        "dbname": s.DATABASE_DB_NAME,
        "user": s.DATABASE_USER,
        "password": s.DATABASE_PASSWORD
    }
)
# else:
#     CONFIG = Config(
#         config_dict={
#             "host": os.environ.get("DATABASE_HOST", "localhost"),
#             "port": int(os.environ.get("DATABASE_PORT", "8001")),
#             "dbname": os.environ.get("DATABASE_DB_NAME", "portal_erp"),
#             "user": os.environ.get("DATABASE_USER", "portal_erp"),
#             "password": os.environ.get("DATABASE_PASSWORD", "portal_erp"),
#         }
#     )


def connect():
    return Database(CONFIG)


def create_table_versionamento(connection):
    connection.execute(
        """
        create table if not exists versionamento (
            script varchar(255) not null primary key,
            hash varchar(50),
            data_aplicacao timestamp
        )
        """
    )


def execute_migrations(connection, pending_migrations):
    print("Executando execute_migrations ")
    for migration in pending_migrations:
        print("Executando: {}".format(migration))
        migration_hash, script = hash_calculate(migration)
        connection.execute(script, skip_load_query=True)
        connection.insert("versionamento").set("script", migration).set(
            "hash", migration_hash
        ).set("data_aplicacao", "current_timestamp", True).execute()


def get_executed_migrations(connection):
    executed_migrations = (
        connection.select("versionamento")
        .fields("script", "hash", "data_aplicacao")
        .order_by("script")
        .execute()
    )
    return executed_migrations


def hash_calculate(migration):
    with open("ddl/{}".format(migration)) as file:
        script = file.read()
    return hashlib.md5(script.encode("utf-8")).hexdigest(), script


def info():
    print("python3 database.py migrate | migration_status")


def migrate():
    pending = migration_status()
    if pending:
        print("Executando migrações pendentes.")
        with connect() as db:
            em = get_executed_migrations(db)
            em = {m.script: m for m in em}
            migrations = os.listdir("ddl")
            migrations.sort()
            print(migrations)
            migrations = [m for m in migrations if m not in em]
            execute_migrations(db, migrations)
    else:
        print("Banco de dados já atualizado.")


def migration_status():
    with connect() as db:
        create_table_versionamento(db)
        executed_migrations = get_executed_migrations(db)
        executed_migrations = {m.script: m for m in executed_migrations}
        migrations = os.listdir("ddl")
        migrations.sort()
        pending = False
        for migration in migrations:
            pending = show_migration_status(migration, executed_migrations) or pending
    return pending


def show_migration_status(migration, executed_migrations):
    pending = False
    if migration not in executed_migrations:
        print("Script {} não foi executado.".format(executed_migrations))
        pending = True
    else:
        m = executed_migrations[migration]
        migration_hash, _ = hash_calculate(migration)
        if migration_hash == m.hash:
            print("Script {} foi executado em {}.".format(migration, m.data_aplicacao))
        else:
            print(
                "Script {} foi executado em {}, porém o arquivo foi modificado.".format(
                    migration, m.data_aplicacao
                )
            )
            pending = True
    return pending


def validate_order(order, fields_table, fields_translated):
    fields_translated = {} if fields_translated is None else fields_translated

    def invalid_field(field):
        return field not in fields_table and field not in fields_translated

    def invalid_sense(sense):
        return sense is not None and sense not in ["asc", "desc"]

    order = re.sub(r"\s{2,}", " ", order.lower())
    order = re.sub(r"\s?,\s?", ",", order)
    sorting_tokens = order.split(",")
    translated_tokens = []
    for token in sorting_tokens:
        t = token.split(" ")
        field = t[0]
        sense = t[1] if len(t) > 1 else None
        if invalid_field(field) or invalid_sense(sense):
            raise ValueError("Ordenação inválida.")
        translated_tokens.append(
            fields_translated.get(field, field)
            + (" " + sense if sense is not None else "")
        )
    return ", ".join(translated_tokens)


def main():
    if len(sys.argv) < 2:
        info()
    elif sys.argv[1] == "migrate":
        migrate()
    elif sys.argv[1] == "migration_status":
        migration_status()
    else:
        info()


if __name__ == "__main__":
    main()
