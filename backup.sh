#!/usr/bin/env bash

OS_EXCLUDE=(
    --exclude='.DS_Store'
)

PYTHON_EXCLUDE=(
    --exclude='venv/'
    --exclude='*.pyc'
)

DOTNET_EXCLUDE=(
    --exclude='bin/'
    --exclude='obj/'
)

NODE_EXCLUDE=(
    --exclude='node_modules/'
)

MISC_EXCLUDE=(
    --exclude='.Trash-*'
    --exclude='build/'
    --exclude='dist/'
)

EXCLUDE=(
    ${OS_EXCLUDE[@]}
    ${PYTHON_EXCLUDE[@]}
    ${DOTNET_EXCLUDE[@]}
    ${NODE_EXCLUDE[@]}
    ${MISC_EXCLUDE[@]}
)

rsync \
    -avz \
    --compress-level=9 \
    --delete \
    --delete-excluded \
    --no-links \
    --filter='P .Trash-10*' \
    ${EXCLUDE[@]} \
    ~/src/ \
    ~/nas/projects/