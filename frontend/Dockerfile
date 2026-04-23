# Stage 1: builder
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Stage 2: runtime
FROM node:18-alpine
WORKDIR /app
RUN adduser --disabled-password --gecos "" appuser
USER appuser
COPY --from=builder /app .
CMD ["npm", "start"]
EXPOSE 3000
HEALTHCHECK --interval=10s --timeout=5s --retries=10 --start-period=30s \
  CMD wget -qO- http://localhost:80 > /dev/null || exit 1
