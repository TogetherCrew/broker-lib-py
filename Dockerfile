FROM python:3.10-bullseye AS base
WORKDIR /project

COPY requirements*.txt ./
COPY setup.py ./
COPY docker-entrypoint.sh ./
COPY README.md ./

RUN pip install .

COPY . .

FROM base as test
RUN chmod +x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]


FROM test as prod
RUN echo "prod passed"