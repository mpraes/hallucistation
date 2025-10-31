# Hallucistation - Docker Development Makefile
# ==============================================

# Variables
DOCKER_COMPOSE = docker-compose
DOCKER = docker
APP_NAME = hallucistation
CONTAINER_NAME = hallucistation-frontend
IMAGE_NAME = hallucistation:latest
PORT = 8000

# Colors for output
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

.PHONY: help build up down restart logs shell test clean dev prod status health

# Default target
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "$(GREEN)Hallucistation Docker Commands$(NC)"
	@echo "================================"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "$(YELLOW)%-15s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Development Commands
# ====================

build: ## Build the Docker image
	@echo "$(GREEN)Building Docker image...$(NC)"
	$(DOCKER_COMPOSE) build

up: ## Start the frontend application
	@echo "$(GREEN)Starting Hallucistation frontend...$(NC)"
	$(DOCKER_COMPOSE) up -d
	@echo "$(GREEN)Frontend is running at http://localhost:$(PORT)$(NC)"

dev: ## Start in development mode with logs
	@echo "$(GREEN)Starting Hallucistation frontend with logs...$(NC)"
	$(DOCKER_COMPOSE) up

down: ## Stop and remove containers
	@echo "$(YELLOW)Stopping Hallucistation...$(NC)"
	$(DOCKER_COMPOSE) down

restart: ## Restart the frontend
	@echo "$(YELLOW)Restarting Hallucistation frontend...$(NC)"
	$(DOCKER_COMPOSE) restart

# Production Commands
# ===================

prod: ## Start in production mode
	@echo "$(GREEN)Starting Hallucistation frontend in production mode...$(NC)"
	$(DOCKER_COMPOSE) up -d
	@echo "$(GREEN)Frontend is running at http://localhost:$(PORT)$(NC)"

# Monitoring Commands
# ===================

logs: ## Show application logs
	$(DOCKER_COMPOSE) logs -f $(APP_NAME)

logs-tail: ## Show last 100 lines of logs
	$(DOCKER_COMPOSE) logs --tail=100 $(APP_NAME)

status: ## Show container status
	@echo "$(GREEN)Container Status:$(NC)"
	$(DOCKER_COMPOSE) ps

health: ## Check frontend health
	@echo "$(GREEN)Checking frontend health...$(NC)"
	@curl -f http://localhost:$(PORT)/health 2>/dev/null && echo "$(GREEN)✓ Frontend is healthy$(NC)" || echo "$(RED)✗ Frontend is not responding$(NC)"

# Development Tools
# =================

shell: ## Open a shell in the running container
	@echo "$(GREEN)Opening shell in container...$(NC)"
	$(DOCKER) exec -it $(CONTAINER_NAME) /bin/bash

shell-root: ## Open a root shell in the running container
	@echo "$(GREEN)Opening root shell in container...$(NC)"
	$(DOCKER) exec -it -u root $(CONTAINER_NAME) /bin/bash

test: ## Open frontend in browser for testing
	@echo "$(GREEN)Opening frontend for testing...$(NC)"
	@command -v xdg-open >/dev/null && xdg-open http://localhost:$(PORT) || echo "Please open http://localhost:$(PORT) in your browser"

test-coverage: ## Test frontend functionality
	@echo "$(GREEN)Testing frontend functionality...$(NC)"
	@curl -s http://localhost:$(PORT)/health && echo "$(GREEN)✓ Health check passed$(NC)" || echo "$(RED)✗ Health check failed$(NC)"
	@curl -s http://localhost:$(PORT)/ | grep -q "Oráculo Alucinado" && echo "$(GREEN)✓ Frontend loaded$(NC)" || echo "$(RED)✗ Frontend not loaded$(NC)"

# Maintenance Commands
# ====================

rebuild: ## Rebuild and restart the frontend
	@echo "$(YELLOW)Rebuilding frontend...$(NC)"
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) build --no-cache
	$(DOCKER_COMPOSE) up -d
	@echo "$(GREEN)Frontend rebuilt and restarted$(NC)"

clean: ## Remove containers, images, and volumes
	@echo "$(RED)Cleaning up Docker resources...$(NC)"
	$(DOCKER_COMPOSE) down -v --rmi all
	$(DOCKER) system prune -f

clean-all: ## Remove everything including unused Docker resources
	@echo "$(RED)Performing deep clean...$(NC)"
	$(DOCKER_COMPOSE) down -v --rmi all
	$(DOCKER) system prune -af --volumes

# Database/Data Commands
# ======================

backup-static: ## Backup static files
	@echo "$(GREEN)Backing up static files...$(NC)"
	mkdir -p backups
	tar czf ./backups/static-backup-$(shell date +%Y%m%d-%H%M%S).tar.gz static/
	@echo "$(GREEN)Static files backup completed$(NC)"

# Quick Commands
# ==============

quick-start: build up ## Quick start: build and run
	@echo "$(GREEN)Quick start completed!$(NC)"

quick-test: ## Quick test: build, run, test, and cleanup
	@make build
	@make up
	@sleep 10
	@make test
	@make down

# Frontend Testing Commands
# =========================

frontend-test: ## Test the frontend functionality
	@echo "$(GREEN)Testing frontend...$(NC)"
	@echo "$(YELLOW)Testing health endpoint:$(NC)"
	@curl -s http://localhost:$(PORT)/health && echo " - $(GREEN)✓ Health OK$(NC)" || echo " - $(RED)✗ Health Failed$(NC)"
	@echo "$(YELLOW)Testing main page:$(NC)"
	@curl -s http://localhost:$(PORT)/ | grep -q "Oráculo Alucinado" && echo " - $(GREEN)✓ Page Loaded$(NC)" || echo " - $(RED)✗ Page Failed$(NC)"

open: ## Open frontend in browser
	@echo "$(GREEN)Opening frontend at http://localhost:$(PORT)$(NC)"
	@command -v xdg-open >/dev/null && xdg-open http://localhost:$(PORT) || echo "Please open http://localhost:$(PORT) in your browser"

# Information Commands
# ====================

info: ## Show frontend information
	@echo "$(GREEN)Hallucistation Frontend Info$(NC)"
	@echo "============================="
	@echo "Application Name: $(APP_NAME)"
	@echo "Container Name: $(CONTAINER_NAME)"
	@echo "Port: $(PORT)"
	@echo "Frontend URL: http://localhost:$(PORT)"
	@echo "Health Check: http://localhost:$(PORT)/health"

urls: ## Show all important URLs
	@echo "$(GREEN)Important URLs:$(NC)"
	@echo "Frontend: http://localhost:$(PORT)"
	@echo "Health Check: http://localhost:$(PORT)/health"