#!/bin/bash

# Define default values for options
add_files_in_current_dir=false
directory=""
file_extension=""
specified_files=()

# Parse command-line options and arguments
while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
        -a)
            add_files_in_current_dir=true
            shift
            ;;
        -p)
            directory="$2"
            shift 2
            ;;
        -e)
            file_extension="$2"
            shift 2
            ;;
        -f)
            # Collect all specified files following -f flag
            shift
            while [[ $# -gt 0 && ! "$1" =~ ^- ]]; do
                specified_files+=("$1")
                shift
            done
            ;;
        *)
            echo "Invalid option: $key"
            exit 1
            ;;
    esac
done

# Process files in the current directory based on options
if [ "$add_files_in_current_dir" = true ] && [ -n "$file_extension" ]; then
    for filename in *."$file_extension"; do
        if [ -f "$filename" ]; then
            git add "$filename"
            git commit -m "Committing file $filename"
            git push
        fi
    done
fi

# Process files in a specified directory (if -p flag is used)
if [ -n "$directory" ] && [ -n "$file_extension" ]; then
    for filename in "$directory"/*."$file_extension"; do
        if [ -f "$filename" ]; then
            git add "$filename"
            git commit -m "Committing file $filename"
            git push
        fi
    done
fi

# Process specified filenames (if -f flag is used)
for filename in "${specified_files[@]}"; do
    if [ -f "$filename" ]; then
        git add "$filename"
        git commit -m "Committing file $filename"
        git push
    else
        echo "Error: File '$filename' not found"
    fi
done

