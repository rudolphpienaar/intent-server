#!/usr/bin/env bash
#
# Build script for Intent-Action Service paper
# Generates PDF, HTML, and DOCX from AsciiDoc source
# Builds TWO versions: Research Paper + Team Proposal
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Directories
RESEARCH_DIR="paper-research"
ENGINEERING_DIR="paper-engineering"
BRIEF_DIR="engineering-brief"
BUILD_DIR="build"
RESEARCH_FILE="${RESEARCH_DIR}/main.adoc"
ENGINEERING_FILE="${ENGINEERING_DIR}/main.adoc"
BRIEF_FILE="${BRIEF_DIR}/main.adoc"

# Check if asciidoctor is installed
check_dependencies() {
    local missing=0

    if ! command -v asciidoctor &> /dev/null; then
        echo -e "${RED}✗ asciidoctor not found${NC}"
        echo "  Install: gem install asciidoctor"
        missing=1
    fi

    if ! command -v asciidoctor-pdf &> /dev/null; then
        echo -e "${YELLOW}⚠ asciidoctor-pdf not found (PDF generation will be skipped)${NC}"
        echo "  Install: gem install asciidoctor-pdf"
    fi

    if [ $missing -eq 1 ]; then
        exit 1
    fi
}

# Create build directory
prepare_build_dir() {
    echo "Creating build directory..."
    mkdir -p "${BUILD_DIR}"
}

# Build HTML for a specific version
build_html() {
    local input_file="$1"
    local output_file="$2"
    local version_name="$3"

    echo -e "${GREEN}Building ${version_name} HTML...${NC}"
    asciidoctor \
        -a data-uri \
        -a allow-uri-read \
        -o "${output_file}" \
        "${input_file}"

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ ${version_name} HTML: ${output_file}${NC}"
    else
        echo -e "${RED}✗ ${version_name} HTML failed${NC}"
        exit 1
    fi
}

# Build PDF for a specific version
build_pdf() {
    local input_file="$1"
    local output_file="$2"
    local version_name="$3"
    local theme_file="$4"

    if command -v asciidoctor-pdf &> /dev/null; then
        echo -e "${GREEN}Building ${version_name} PDF...${NC}"

        # Build command with optional theme
        local cmd="asciidoctor-pdf -a allow-uri-read"
        if [ -n "${theme_file}" ] && [ -f "${theme_file}" ]; then
            cmd="${cmd} -a pdf-theme=${theme_file}"
        fi
        cmd="${cmd} -o \"${output_file}\" \"${input_file}\""

        eval ${cmd}

        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ ${version_name} PDF: ${output_file}${NC}"
        else
            echo -e "${RED}✗ ${version_name} PDF failed${NC}"
        fi
    else
        echo -e "${YELLOW}⚠ Skipping ${version_name} PDF (asciidoctor-pdf not installed)${NC}"
    fi
}

# Build DOCX for a specific version (via pandoc)
build_docx() {
    local html_file="$1"
    local output_file="$2"
    local version_name="$3"

    if command -v pandoc &> /dev/null; then
        echo -e "${GREEN}Building ${version_name} DOCX...${NC}"
        pandoc \
            -f html \
            -t docx \
            -o "${output_file}" \
            "${html_file}"

        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ ${version_name} DOCX: ${output_file}${NC}"
        else
            echo -e "${RED}✗ ${version_name} DOCX failed${NC}"
        fi
    fi
}

# Build all formats for all versions
build_all_versions() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  Building RESEARCH VERSION${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    build_html "${RESEARCH_FILE}" "${BUILD_DIR}/paper_research.html" "Research"
    build_pdf "${RESEARCH_FILE}" "${BUILD_DIR}/paper_research.pdf" "Research"
    build_docx "${BUILD_DIR}/paper_research.html" "${BUILD_DIR}/paper_research.docx" "Research"

    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  Building ENGINEERING VERSION (Full)${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    build_html "${ENGINEERING_FILE}" "${BUILD_DIR}/paper_engineering.html" "Engineering"
    build_pdf "${ENGINEERING_FILE}" "${BUILD_DIR}/paper_engineering.pdf" "Engineering"
    build_docx "${BUILD_DIR}/paper_engineering.html" "${BUILD_DIR}/paper_engineering.docx" "Engineering"

    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  Building ENGINEERING BRIEF (Short)${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    build_html "${BRIEF_FILE}" "${BUILD_DIR}/engineering_brief.html" "Brief"
    build_pdf "${BRIEF_FILE}" "${BUILD_DIR}/engineering_brief.pdf" "Brief" "${BRIEF_DIR}/compact-theme.yml"
    build_docx "${BUILD_DIR}/engineering_brief.html" "${BUILD_DIR}/engineering_brief.docx" "Brief"
}

# Show file sizes
show_summary() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}✓ Build Complete!${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "Generated files in ${BUILD_DIR}/:"
    echo ""
    echo -e "${YELLOW}Research Version (for journal submission):${NC}"
    ls -lh "${BUILD_DIR}"/paper_research.* 2>/dev/null | awk '{print "  "$9" ("$5")"}'
    echo ""
    echo -e "${YELLOW}Engineering Version - Full (comprehensive internal doc):${NC}"
    ls -lh "${BUILD_DIR}"/paper_engineering.* 2>/dev/null | awk '{print "  "$9" ("$5")"}'
    echo ""
    echo -e "${YELLOW}Engineering Brief (concise team presentation):${NC}"
    ls -lh "${BUILD_DIR}"/engineering_brief.* 2>/dev/null | awk '{print "  "$9" ("$5")"}'
    echo ""
}

# Main
main() {
    echo -e "${BLUE}══════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  Intent-Action Service Document Builder${NC}"
    echo -e "${BLUE}  3 versions: Research + Engineering + Brief${NC}"
    echo -e "${BLUE}══════════════════════════════════════════════════${NC}"
    echo ""

    check_dependencies
    prepare_build_dir
    build_all_versions
    show_summary
}

main "$@"
