FROM pypy:3.8-slim as base

ENV PYTHONUNBUFFERED 1

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y upgrade

RUN pip install virtualenv
ENV PATH="/venv/bin:$PATH"
RUN virtualenv /venv

FROM base as builder

RUN apt-get -y install --no-install-recommends syslog-ng postgresql build-essential libpq-dev

WORKDIR /venv
RUN /bin/bash -c "source /venv/bin/activate"
COPY requirements.txt /venv/requirements.txt
RUN pip install psycopg2cffi --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

RUN rm /venv/requirements.txt

WORKDIR /cubex

COPY . .

RUN python -m compileall . -b
RUN find . -name "*.py" -exec rm -rf {} \;

RUN rm requirements.txt
RUN rm Dockerfile

FROM base as packager

RUN apt-get -y install --no-install-recommends libpq-dev postgresql-client postgresql-client-common

RUN useradd cubex
RUN mkdir /cubex
RUN chown -R cubex:cubex /cubex

USER cubex

COPY --from=builder /venv /venv
COPY --from=builder /cubex /cubex

WORKDIR /cubex
RUN /bin/bash -c "source /venv/bin/activate"

EXPOSE 8000
CMD gunicorn --timeout 120 --workers=5 -b 0.0.0.0:8000 --log-level=error framework.wsgi
