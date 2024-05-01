# Use official Node.js image as base image
FROM node:20.11-alpine

# Set working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Next.js application
RUN npm run build

# Expose port 3000 (default Next.js port)
EXPOSE 3030

# Command to run the Next.js application
CMD ["npm", "start"]
