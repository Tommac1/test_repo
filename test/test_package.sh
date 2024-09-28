#!/usr/bin/env bash

die() {
  echo "$1"
  exit 1
}

perform_test() {
  # $1 - a
  # $2 - b
  # $3 - operation
  # $4 expected result

  OUTPUT=$(test_repo "$1" "$2" "$3")
  if [[ "${OUTPUT}" == "$4" ]]; then
    return 0  # Pass.
  else
    echo "Should be: $4"
    echo "Is: ${OUTPUT}"
    return 1  # Fail.
  fi
}

perform_test 3 4 "add" "Result = 7" || die "Failed at test #1"
perform_test 10 4 "sub" "Result = 6" || die "Failed at test #2"
perform_test 3 4 "mul" "Result = 12" || die "Failed at test #3"
perform_test 12 4 "div" "Result = 3" || die "Failed at test #4"
