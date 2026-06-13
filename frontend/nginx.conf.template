FROM node:20-alpine AS build

WORKDIR /app

COPY package.json .
RUN npm install

COPY . .
RUN npm run build


FROM nginx:1.27-alpine

# Nginx official image automatically renders templates from this folder
# using environment variables when the container starts.
COPY nginx.conf.template /etc/nginx/templates/default.conf.template

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80