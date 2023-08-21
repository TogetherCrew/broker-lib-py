FROM python:3.10-bullseye AS base
WORKDIR /project
COPY . .
RUN pip install .

FROM base as test
RUN chmod +x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]


FROM test as prod
RUN echo "prod passed"