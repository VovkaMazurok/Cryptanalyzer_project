# Get user id for macOS and Linux
ifeq ($(shell uname),Darwin)
	USER_ID := $(shell id -u)
else
	USER_ID := $(shell id --user)
endif


.PHONY: echo-i-uid
# Echo user id
echo-i-uid:
	@echo ${USER_ID}

.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run: init-configs d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge


.PHONY: init-configs
# Configuration files initialization
init-configs:
	@cp .env.example .env &&\
		cp compose.override.dev.yaml compose.override.yaml


.PHONY: d-run
# Just run
d-run:
	@export USER_ID=${USER_ID} &&\
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up \
			--build


.PHONY: d-purge
# Purge all data related with services
d-purge:
	@export USER_ID=${USER_ID} &&\
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0

.PHONY: d-compose-inspect
# Get information about current compose configuration
d-compose-inspect:
	@export USER_ID=${USER_ID} &&\
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose convert


.PHONY: init-dev
# Init environment for development
init-dev:
	@make python-i-venv-i-install && \
	make pre-commit-install


.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@python main.py

.PHONY: homework-i-purge
homework-i-purge:
	@echo Goodbye


# [pre-commit]-[BEGIN]
.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run
#un
.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files
#
.PHONY: pre-commit-autoupdate
# Update "rev" version of all pre-commit hooks.
pre-commit-autoupdate:
	@pre-commit autoupdate
#
.PHONY: pre-commit-install
# Install pre-commit.
pre-commit-install:
	@pre-commit install
#
# Pre-commit run for folder:
# https://pre-commit.com/#pre-commit-run:~:text=git%20ls%2Dfiles%20%2D%2D%20%27*.py%27%20%7C%20xargs%20pre%2Dcommit%20run%20%2D%2Dfiles
# git ls-files -- apps/users/ | xargs pre-commit run --files
# [pre-commit]-[END]


# [uv]-[BEGIN]
.PHONY: uv-install
# Install uv.
uv-install:
	@curl -LsSf https://astral.sh/uv/install.sh | sh
#
.PHONY: python-i-venv-i-install
# Create virtual environment and install dependencies.
python-i-venv-i-install:
	@uv sync --frozen
#
.PHONY: python-i-venv-i-deps-upgrade-with-sync
# Upgrade dependencies.
python-i-venv-i-deps-upgrade:
	@uv sync --upgrade
# [uv]-[END]

# [extra_python]-[BEGIN]
.PHONY: install-pre-commit
# Install pre-commit.
install-pre-commit:
	@uv tool install pre-commit &&\
	uv tool upgrade pre-commit
#
.PHONY: install-ruff
# Install black.
install-ruff:
	@uv tool install ruff &&\
	uv tool upgrade ruff
# [extra_python]-[END]
