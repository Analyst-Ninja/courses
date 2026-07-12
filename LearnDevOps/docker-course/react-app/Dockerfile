FROM node:20-alpine3.19

RUN apk update && apk upgrade

RUN addgroup app && adduser -S -G app app 

USER app

WORKDIR /app

COPY . .

USER root

RUN chown -R app:app .

USER app

RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev"]