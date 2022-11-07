FROM node:17.3-alpine
WORKDIR /app/frontend
COPY package.json package-lock.json ./
RUN npm install
COPY . ./
CMD ["npm", "run", "start"]