.PHONY: install
install:
	poetry install

.PHONY: mm
mm:
	poetry run python -m core.manage migrate

.PHONY: mk
mk:
	poetry run python -m core.manage makemigrations

.PHONY: rs
rs:
	poetry run python -m core.manage runserver

.PHONY: sp
sp:
	poetry run python -m core.manage createsuperuser

.PHONY: upd
upd: install mm;