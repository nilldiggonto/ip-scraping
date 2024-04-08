FROM nginx:1.21-alpine

RUN rm /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/
COPY conf.d/default.conf /etc/nginx/conf.d/
