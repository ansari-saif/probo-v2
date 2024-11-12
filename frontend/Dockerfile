FROM node:18-alpine

WORKDIR /app

RUN npm install -g pnpm

# Copy package files
COPY package*.json ./
COPY pnpm*.yaml ./

# Install dependencies
RUN pnpm install

# Copy rest of the application code
COPY . .

# Build the application
RUN pnpm run build

# Expose port 5173 (Vite's default port)
EXPOSE 5173

# Start the application
CMD ["npm", "run", "dev", "--", "--host"]
