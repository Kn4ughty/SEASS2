#!/bin/bash
# Download and store jetbrains mono font supporting MACOS and LINUX

# Nerd fonts are a set of fonts that are patched to include icons and other symbols
# Download includes wayyy to many variants so I delete them all for your convience. 

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