#!/bin/bash

# Locale for UTF-8 support
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# Function to fetch and clean a random message
get_random_message() {
  local msg
  msg=$(curl -s https://ipgoc.gibranlp.dev/ipgoc | shuf -n 1)
  [[ -z "$msg" ]] && msg="Te Amito Muchito <3"
  echo "$msg"
}

while true; do
  message=$(get_random_message)

  # Show AppleScript dialog with message and buttons
  result=$(osascript <<EOF
display dialog "$message" buttons {"Cerrar", "Otro"} default button "Cerrar" with title "IPGOC <3" with icon note
EOF
)

  # Check if user clicked "Otro"
  if [[ "$result" != *"Otro"* ]]; then
    break
  fi
done
