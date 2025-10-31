#!/usr/bin/env bash
#
# Copy updated figures from figures-source/png to all three paper directories
#

set -e

SOURCE_DIR="figures-source/png"
TARGETS=(
    "engineering-brief/figures"
    "paper-engineering/figures"
    "paper-research/figures"
)

echo "Copying figures from ${SOURCE_DIR} to paper directories..."
echo

# Copy Status Quo figure
if [ -f "${SOURCE_DIR}/ChRIS_arch_IAS - Status Quo.png" ]; then
    for target in "${TARGETS[@]}"; do
        cp "${SOURCE_DIR}/ChRIS_arch_IAS - Status Quo.png" \
           "${target}/fig01_current_architecture_v2.png"
        echo "✓ Copied Status Quo → ${target}/fig01_current_architecture_v2.png"
    done
else
    echo "⚠ Warning: Status Quo figure not found in ${SOURCE_DIR}"
fi

echo

# Copy IAS figure
if [ -f "${SOURCE_DIR}/ChRIS_arch_IAS - IAS.png" ]; then
    for target in "${TARGETS[@]}"; do
        cp "${SOURCE_DIR}/ChRIS_arch_IAS - IAS.png" \
           "${target}/fig04_external_ias_v2.png"
        echo "✓ Copied IAS → ${target}/fig04_external_ias_v2.png"
    done
else
    echo "⚠ Warning: IAS figure not found in ${SOURCE_DIR}"
fi

echo
echo "✓ All figures copied successfully"
echo
echo "Figure sizes:"
ls -lh engineering-brief/figures/fig*_v2.png | awk '{print "  " $9 " (" $5 ")"}'
