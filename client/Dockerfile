# 1. Сборка проекта на vite
FROM node:latest

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

# 2. Развертывание проекта c Nginx
#FROM nginx
#COPY --from=build /app/dist /usr/share/nginx/html
#COPY --from=build /app/.nginx/nginx.conf /etc/nginx/conf.d/default.conf
#CMD ["nginx", "-g", "daemon off"]
#CMD nginx -g "daemon off;"

EXPOSE 5000

CMD ["npm", "run", "preview-host"]

