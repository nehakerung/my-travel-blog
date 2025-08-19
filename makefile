.PHONY: runserver
runserver:
# to start mysql connection
	brew services start mysql
	python manage.py runserver --settings=my_travel_blog.settings

.PHONY: break
break:
# stop mysql connection
	brew services stop mysql
