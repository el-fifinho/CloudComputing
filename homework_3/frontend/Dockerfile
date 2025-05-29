# # Build stage
# FROM node:18 as build-stage
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build

# # Serve stage
# FROM nginx:stable-alpine
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

# Step 1: Build the Vue app
FROM node:18 AS builder

WORKDIR /app

# Copy project files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the source and build it
COPY . .
RUN npm run build

# Step 2: Serve the built app with Nginx
FROM nginx:stable-alpine

# Copy the built app to nginx's web directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Optional: Replace default nginx config with a custom one (if needed)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 (the default for nginx)
EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]
