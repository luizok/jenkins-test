FROM node:lts-alpine3.14

WORKDIR /home/node_server
COPY ./package.json .
RUN npm install
COPY . .

# CMD ["node", "index.js"]
CMD ["npm", "run", "test"]
