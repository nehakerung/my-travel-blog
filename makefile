.PHONY: runserver
runserver:
	python manage.py runserver --settings=my_travel_blog.settings

.PHONY: start
start:
# to start mysql connection
	brew services start mysql
.PHONY: stop
stop:
# stop mysql connection
	brew services stop mysql

.PHONY: dev-init
dev-init:
	poetry run python manage.py migrate

.PHONY: lint
lint:
	poetry run pylint my_travel_blog
	poetry run black my_travel_blog --check