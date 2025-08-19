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
