#!/bin/bash

# Fetch the file and select a random line as the target
target=$(curl -s https://ipgoc.gibranlp.dev/ipgoc | shuf -n 1)
target_length=${#target}

generate_random_letter() {
  local random_byte
  random_byte=$(od -An -N1 -i /dev/random 2>/dev/null)
  printf "\\x$(printf %x $((random_byte % 94 + 32)))"
}

evolve_message() {
  local message=""
  local found=false

  for ((i = 0; i < target_length; i++)); do
    message+="$(generate_random_letter)"
  done

  while ! "${found}"; do
    found=true
    local current_message=""

    for ((i = 0; i < target_length; i++)); do
      if [[ "${message:i:1}" != "${target:i:1}" ]]; then
        current_message+="$(generate_random_letter)"
        found=false
      else
        current_message+="${target:i:1}"
      fi
    done

    message="${current_message}"
    printf "\r%s" "${message}"
    sleep 0.0001
  done

  echo ""
}

evolve_message

exit 0
