run:
	docker build -t server .
	docker pull mongo
	docker pull sonarqube

	docker-compose up