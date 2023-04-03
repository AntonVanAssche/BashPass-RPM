#!/usr/bin/env bash

set -o errexit  # Abort on nonzero exit code.
set -o noglob   # Disable globbing.
set +o xtrace   # Disable debug mode.
set -o pipefail # Don't hide errors within pipes.

readonly NAME='bashpass-remote'
readonly VERSION='1.0'

# Whenever an error occurs, we want to notify the user about it.
# This is a basic function that wil print the corresponding error
# message to stderr, and will exit with the given exit status.
error_out() {
    printf '\n'
    printf 'An error occurred: %s' "${1}" >&2
    printf '\n'
    exit "${2}"
}

# The script expects BashPass to be in the same directory as this script.
# So we will have to check if it is there.
[[ -d BashPass-Remote ]] || \
    error_out 'BashPass-Remote is not in the same directory as this script.' 1

# Prepare the tarball.
mkdir -p "${NAME}-${VERSION}"
cp -r "BashPass-Remote/${NAME}" "${NAME}-${VERSION}"
cp -r "BashPass-Remote/docs/${NAME}.1.gz" "${NAME}-${VERSION}"

tar -czf "${NAME}-${VERSION}.tar.gz" "${NAME}-${VERSION}"

# Prepare the RPM build environment.
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

# Copy the tarball to the SOURCES directory.
cp -r "${NAME}-${VERSION}.tar.gz" ~/rpmbuild/SOURCES

# Copy the spec file to the SPECS directory.
cp -r "${NAME}.spec" ~/rpmbuild/SPECS

# Build the RPMs.
rpmbuild -bb ~/rpmbuild/SPECS/"${NAME}.spec"
