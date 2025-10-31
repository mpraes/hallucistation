# Use nginx alpine for lightweight static file serving
FROM nginx:alpine

# Set environment variables
ENV NGINX_PORT=8000

# Copy static files to nginx html directory
COPY static/ /usr/share/nginx/html/

# Copy data files to nginx html directory
COPY data/ /usr/share/nginx/html/data/

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create a non-root user for nginx
RUN adduser -D -s /bin/sh nginx_user

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8000/ || exit 1

# Command to run nginx
CMD ["nginx", "-g", "daemon off;"]