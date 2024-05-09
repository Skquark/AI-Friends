#!/bin/bash

# Define variables
APP_NAME="DiffusionDeluxe"
APP_SH="sdd-linux.sh"
APP_ICON="icon.icns"
APP_DEST="/Applications"

# Create package directory
mkdir -p "$APP_NAME.pkg"

# Copy files
cp "$APP_SH" "$APP_NAME.pkg$APP_DEST"
cp "Resources/$APP_ICON" "$APP_NAME.pkg"

# Create package using productbuild
pkgbuild --root "$APP_NAME.pkg" \
         --identifier "com.skquark.$APP_NAME" \
         --install-location "$APP_DEST" \
         "$APP_NAME.pkg/$APP_NAME.pkg"

# Build distribution package
productbuild --distribution "Distribution.xml" \
             --package-path "$APP_NAME.pkg" \
             "$APP_NAME Installer.pkg"