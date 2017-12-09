FROM python:3.6
MAINTAINER Emad Mokhtar emad@emadmokhtar.com
ENV PYTHONUNBUFFERED 1
ENV APP_PATH /app
RUN mkdir $APP_PATH
ADD . $APP_PATH

WORKDIR $APP_PATH

# Install requirements
RUN pip install -r requirements/requirements.txt

# Migrate data models
RUN python manage.py migrate

# Load data
RUN python manage.py loaddata dump_data/sura.json
RUN python manage.py loaddata dump_data/quran_text.json
RUN python manage.py loaddata dump_data/tafseer.json


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
