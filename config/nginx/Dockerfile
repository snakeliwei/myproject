FROM snakeliwei/docker-alpine-nginx
MAINTAINER Lyndon Li <snakeliwei@gmail.com>

COPY nginx.conf /etc/nginx/
RUN mkdir -p /etc/nginx/sites-enabled \
    && mkdir -p /tmp/nginx \
    && chmod -R 777 /tmp
VOLUME /etc/nginx/sites-enabled 
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
