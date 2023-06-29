from tqdm import tqdm

# Example arrays
arrays = [
    ['apple', 'banana', 'cherry'],
    ['dog', 'cat', 'elephant', 'giraffe'],
    ['red', 'green', 'blue', 'yellow', 'orange'],
    ['sun', 'moon'],
    ['one', 'two', 'three', 'four', 'five', 'six'],
    ['car', 'bike'],
    ['python', 'java', 'javascript'],
    ['open', 'close'],
    ['summer', 'winter', 'spring', 'fall'],
    ['up', 'down', 'left', 'right']
]

# Progress bar for overall progress
overall_progress = tqdm(total=len(arrays), desc="Overall Progress", ncols=100)

# Iterate through each array
for array in arrays:
    # Progress bar for current array
    current_progress = tqdm(array, desc="Current Array Progress", leave=False)

    # Iterate through each value in the array
    for value in current_progress:
        # Process the value here (display, perform calculations, etc.)
        print(value)

        # Update the progress bar for the current array
        current_progress.set_postfix({"Current Value": value})
        current_progress.update(1)

    # Update the overall progress bar
    overall_progress.update(1)

    # Close the progress bar for the current array
    current_progress.close()

# Close the overall progress bar
overall_progress.close()
