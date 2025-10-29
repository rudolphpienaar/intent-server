#!/usr/bin/env bash
#
# Word count script for paper sections
# Helps track against journal word limits
#
# Usage: ./word-count.sh [research|engineering]
# Default: counts both versions

VERSION="${1:-both}"

count_version() {
    local paper_dir="$1"
    local version_name="$2"

    echo ""
    echo "Word count for ${version_name} version:"
    echo "========================================"

    local total=0

    for file in "${paper_dir}/sections"/*.adoc; do
        if [ -f "$file" ]; then
            # Strip AsciiDoc markup and count words
            count=$(sed 's/=\+//g; s/\[.*\]//g; s/:.*://g' "$file" | wc -w)
            total=$((total + count))
            basename=$(basename "$file" .adoc)
            printf "%-30s %6d words\n" "$basename" "$count"
        fi
    done

    echo "========================================"
    printf "%-30s %6d words\n" "TOTAL" "$total"
}

if [ "$VERSION" = "research" ] || [ "$VERSION" = "both" ]; then
    count_version "paper-research" "RESEARCH"
fi

if [ "$VERSION" = "engineering" ] || [ "$VERSION" = "both" ]; then
    count_version "paper-engineering" "ENGINEERING"
fi

echo ""

# Typical journal limits
echo "Typical journal word limits:"
echo "  - IEEE Software: 6,000-8,000"
echo "  - J. Biomed. Informatics: ~10,000"
echo "  - Software Practice & Experience: 8,000-10,000"
