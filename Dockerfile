
FROM python:2.7.12

# set the localtime
RUN \
    echo "Asia/shanghai" > /etc/timezone && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# work directory
WORKDIR /cartier/codebase

#ARG cartier_branch

RUN git clone https://github.com/haifengrundadi/cartier.git

WORKDIR /cartier/codebase/cartier

RUN pip install -r requirements.txt

CMD ["py.test", "-s", "tests/smoketest"]