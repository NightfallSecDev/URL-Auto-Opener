import webbrowser
import time

# Get file input from user
file_path = input("Enter the path to your text file: ")

# Get time delay input from user (in seconds)
try:
    delay = int(input("Enter the time delay between each URL (in seconds): "))
except ValueError:
    print("Invalid input for time delay. Please enter an integer value.")
    exit()

try:
    # Read URLs from file
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

    for url in urls:
        print(f"Opening: {url}")
        webbrowser.open(url)  # Open URL in default browser
        time.sleep(delay)  # Wait before proceeding
        print(f"Checked: {url}")

    print("All URLs have been opened and checked.")

except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
