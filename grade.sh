#!/bin/bash

######## Variable globals -> ########
# The file containing the "main" entry point for the program.
# In C or C++, this is the file containing the main() function
# In Python, this is whichever file you run via python3 whatever.py
# In Bash, this is whichever file you run via python3 whatever.sh
main_file="word_up.py"

# Any arguments you want passed to the main driver, upon excution.
# If you do not have any arguments, just leave as an empty string, ""
main_file_arguments=""

# The language that the assignment is written in.  Currently supported
# options are "cpp", "python", "bash"
language="python"

# Whether or not to score the student using a static analyzer.
# For Python, this is the mypy type-checker.
# For C or C++, this is cppcheck.
# For Bash, this is shellcheck
enable_static_analysis=true

# Whether or not to score the student using an autoformatter (dock points
# if not formatted correctly).
# For Python, this is black.
# For C++, this is clang-format.
# For Bash, this is shfmt
enable_format_check=true

# Whether or not to use fuzzy or ridig diffs
# If you choose true, fuzzy diffs will give partial credit.
# This can be helpful for string-heavy assignments,
# where correctness is reasonable to estimate statistically.
# If you choose false, rigid diffs will be all-or-none.
# This is helpful when the assignment is mathy,
# where correctness is not reasonable to estimate statistically.
fuzzy_partial_credit=false

######## <- Variable globals ########

######## File and type existence tests -> ########
# Load the specified assosicative array with files you want to check for the existence of.
# Key is the file, and Value must be a sub-string within what is produced by the bash command:
# $ file file.whatever
declare -A file_arr
# file_arr=(
#     ["ssh-key0.png"]="PNG image data"
#     ["id_rsa.pub"]="OpenSSH RSA public key"
#     ["gpg2_key.asc"]="PGP public key block Public-Key"
# )
######## <- File and type existence tests ########

######## Custom tests -> ########
# Any tests other than the unit tests and the stdout diff tests belong here,
# and must be bash functions whose names begin with "custom_test".
# Custom tests should report their score by assigning their result (0-100)
# to the custom_test_score, e.g.:
# custom_test_score=100
# Custom tests are performed alphabetically,
# so number them if you want them in order.

custom_test_1_randomized_search() {
    custom_test_score=0
    for i in {1..30}; do
        rm -f test_case.txt correct_output.txt temp_out.txt
        python3 generate_word_search.py
        timeout 20 python3 word_up.py <test_case.txt >temp_out.txt
        if diff temp_out.txt correct_output.txt; then
            custom_test_score=100
        else
            custom_test_score=0
            echo "If you fail this test only occasionally, and due to bad luck, fail on push, just restart the pipeline."
            if [ "$annoying_nodebug" = "onlydothisaftercompletingthebasics" ] || grep 'docker\|lxc' /proc/1/cgroup >/dev/null 2>&1; then
                echo Run this script locally with debugging details.
            else
                echo "Enter to see your diffs, and then :qa to exit Vim"
                read -r
                vim -d temp_out.txt temp_correct.txt
            fi
            rm -f test_case.txt correct_output.txt temp_out.txt
            break
        fi
        rm -f test_case.txt correct_output.txt temp_out.txt
    done
}

######## <- Custom tests ########

source .admin_files/grade_backend.sh
