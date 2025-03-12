include .env

DC=docker compose
DE=docker exec
CN=$(CONTAINER_NAME)
CON=-u$(USER) -p$(PASSWORD) $(DATABASE_NAME)

up:	
	@if [ -n "$$(docker ps --filter 'publish=$(PORT)' -q)" ]; then \
		docker stop $$(docker ps --filter 'publish=$(PORT)' -q); \
	fi

	$(DC) up --force-recreate -d

down:
	$(DC) down

restart: down up

clear: 
	docker volume rm $(CN)_mysql_data

reset: down clear up

mysql:
	$(DE) -it $(CN) mysql $(CON)

mysql-backup:
	$(DE) -it $(CN) mysqldump $(CON) > backup/backup.sql

.PHONY: up down restart mysql mysql-backup
