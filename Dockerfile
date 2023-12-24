FROM python:3.10-alpine as base

RUN apk add --no-cache build-base

FROM base as builder
COPY requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt

FROM base
# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY . /app
WORKDIR /app

# command to run on container start
ENTRYPOINT [ "python", "./main.py" ]