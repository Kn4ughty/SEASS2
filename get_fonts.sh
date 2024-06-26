#!/bin/bash
# Download and store jetbrains mono font supporting MACOS and LINUX
mkdir -p font
curl -L "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/JetBrainsMono.zip" -o font/JetBrainsMono.zip
unzip -qu font/JetBrainsMono.zip -d font
rm font/JetBrainsMono.zip

cp font/JetBrainsMonoNerdFont-Regular.ttf font/JetBrainsMonoNerdFont-Regular.ttf.bak

# Remove all other fonts ending in .ttf
rm font/*.ttf

# Copy back the font we want

mv font/JetBrainsMonoNerdFont-Regular.ttf.bak font/JetBrains.ttf


# Cleanup
rm font/README.md