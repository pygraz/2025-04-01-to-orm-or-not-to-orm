# Django: To ORM or not to ORM

This is a Python Django example application to show when how to use both Django's object relation mapping (ORM) and raw SQL for reporting in the same application.

> [!NOTE]  
> This repository and talk have been the basis for a more up-to-date talk at the
> PyCon Austria. You can find the related slides and source code at
> <https://github.com/roskakori/django-reporting-with-raw-sql>.

## Environment settings

The project requires an environment file named `.env` to know about the [PostgreSQL](https://www.postgresql.org/) database settings and the preferred default password for demo data.

For example:

```dotenv
# The default password for demo data.
MT_DEFAULT_PASSWORD="deMo.123"

# PotgreSQL database connection
MT_POSTGRES_HOST=localhost
MT_POSTGRES_PORT=5422
MT_POSTGRES_DATABASE=minitrack_local
MT_POSTGRES_USERNAME=minitrack_local
MT_POSTGRES_PASSWORD=${MT_DEFAULT_PASSWORD}
```

### PostgreSQL from docker container

By default, the application will connect to a local server running on port 5432 to a database `minitrack_local` with a user `minitrack_local` and the password `deMo.123`. The repository includes a `compose.yaml` which can be used with [Docker](https://www.docker.com/):

```bash
docker compose up
```

### Existing PostgreSQL server

If you already have access to an existing Postgre server, specify the settings in the `.env`.

## Project setup

The project requires [uv](https://docs.astral.sh/uv/).

To set up the project, run:

```bash
uv sync --group dev
```

In order to keep code clean even after your own modifications, activate the pre-commit hooks:

```bash
uv run pre-commit install --install-hooks
```

Next, apply the database migrations:

```bash
uv run python manage.py migrate
```

After that, create an admin user to log in. The fastest way for that is:

```bash
uv run python manage.py make_demo_admin
```

This adds an admin user named "admin" with the password specified with the environment variable `MT_DEFAULT_PASSWORD` (default: "deMo.123").

Alternatively, you can use the standard management command `createsuperuser` and specify all the details yourself:

```bash
uv run python manage.py createsuperuser --username admin
```

Then run the server

```bash
uv run python manage.py runserver
```

Now connect to <http://localhost:8000/> and use the login from the `createsuperuser` form above.

You can use the admin UI to create and edit data.

To get you started quickly, create a few random demo data by running:

```bash
uv run python manage.py make_demo
```

## License

Copyright (c) 2025 Python User Group Graz. Distributed under the [MIT License](LICENSE).
