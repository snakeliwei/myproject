FROM bestone/rubyenv:1.1
MAINTAINER Lyndon li <snakeliwei@qq.com>

RUN mkdir -p /app
VOLUME /app
COPY Gemfile /app
COPY Gemfile.lock /app
WORKDIR /app
RUN /bin/bash -l -c "source /etc/profile.d/rvm.sh" \
    && /bin/bash -l -c "bundle install"

EXPOSE 8091
CMD ["./backend.sh"]
