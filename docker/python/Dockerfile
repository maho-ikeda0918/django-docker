FROM python:3.12

ARG USERNAME
ARG GROUPNAME
ARG UID
ARG GID

ENV PYTHONUNBUFFERED 1

RUN mkdir /workspace

WORKDIR /workspace

ADD requirements.txt /workspace/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
USER $USERNAME

ADD . /workspace/