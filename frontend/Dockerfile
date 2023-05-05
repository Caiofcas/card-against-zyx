FROM node:19.4

WORKDIR /app/

COPY ./frontend/package.json .
COPY ./frontend/package-lock.json .
COPY ./frontend/tsconfig.json .
COPY ./frontend/svelte.config.js .
COPY ./frontend/vite.config.ts .

RUN npm install
