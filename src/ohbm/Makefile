VENV_DIR := .venv
VENV_BIN := $(VENV_DIR)/bin
UV ?= uv
OUTPUT_DIR ?= $(abspath $(CURDIR)/../../build/ohbm)

.PHONY: help venv install run shell clean purge

help:
	@echo "OHBM 2026 agentic simulation targets:"
	@echo "  make run     - Install (editable) and generate figures/summary"
	@echo "  make install - Install editable package into venv"
	@echo "  make shell   - Open shell with venv activated"
	@echo "  make clean   - Remove build outputs"
	@echo "  make purge   - Remove build outputs and venv"
	@echo ""
	@echo "Defaults:"
	@echo "  OUTPUT_DIR=$(OUTPUT_DIR)"

venv:
	$(UV) venv $(VENV_DIR)

install: venv
	$(UV) pip install -e .

run: install
	OUTPUT_DIR=$(OUTPUT_DIR) $(VENV_BIN)/ohbm2026 --output-dir $(OUTPUT_DIR)

shell: venv
	@echo "Starting shell with activated venv (exit to return)..."
	@bash -c "source $(VENV_BIN)/activate && exec bash"

clean:
	rm -rf $(OUTPUT_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

purge: clean
	rm -rf $(VENV_DIR)
