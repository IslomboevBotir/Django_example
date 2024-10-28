FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=src.invest_era.settings
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["gunicorn", "src.invest_era.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
