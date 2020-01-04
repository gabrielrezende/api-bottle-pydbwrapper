FROM "python:3.6-alpine"
ARG SSH_PRIVATE_KEY

ADD . /opt/app-root/src/perp-backend
WORKDIR /opt/app-root/src/perp-backend
EXPOSE 5000

RUN apk update && \
    apk add \
        libffi-dev \
        gcc \
        musl-dev \
        postgresql-dev \
        git  \
        postgresql-libs \
        python3-dev \
        git \
        openssh

# apk add \#--virtual .build-deps \

RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan bitbucket.org > /root/.ssh/known_hosts

RUN echo "$SSH_PRIVATE_KEY" > /root/.ssh/id_rsa && chmod 400 /root/.ssh/id_rsa


# RUN python3 -m pip install -r requirements.txt -r requirements-test.txt --no-cache-dir && \
    # apk --purge del .build-deps
RUN python3 -m pip install -r requirements.txt -r requirements-test.txt --no-cache-dir

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
