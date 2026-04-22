# =========================
# STAGE 1: BUILDER
# =========================
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .


# =========================
# STAGE 2: RUNTIME
# =========================
FROM node:18-alpine

WORKDIR /app

# create non-root user
RUN adduser -D appuser

# install only runtime dependency for healthcheck
RUN apk add --no-cache wget

# copy built app from builder stage
COPY --from=builder /app /app

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=10s --timeout=5s --retries=10 --start-period=30s \
CMD wget -qO- http://localhost:3000 > /dev/null || exit 1

CMD ["node", "app.js"]