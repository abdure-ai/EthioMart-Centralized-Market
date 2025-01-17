import pandas as pd

# Load the CSV file
file_path = r"..\data\structured_messages.csv"  # Replace with your file path
df = pd.read_csv(file_path)

# Step 1: Inspect Missing Values
print("Missing Values Per Column:")
print(df.isnull().sum())

# Step 2: Handle Missing Values
# Option 1: Fill missing values with default values
df['sender'] = df['sender'].fillna('Unknown')  # Replace missing sender with 'Unknown'
df['date'] = df['date'].fillna('Unknown')  # Replace missing dates with 'Unknown'
df['content_cleaned'] = df['content_cleaned'].fillna('No Content')  # Replace missing cleaned text with empty string
df['price'] = df['price'].fillna('Not Available')  # Replace missing price with 'Not Available'
df['location'] = df['location'].fillna('Unknown')  # Replace missing locations with 'Unknown'
df['contact_info'] = df['contact_info'].fillna('No Contact Info')  # Replace missing contact info
df['telegram_links'] = df['telegram_links'].fillna('No Links')  # Replace missing Telegram links

# Option 2: Drop rows with missing values in critical columns
#df = df.dropna(subset=['content', 'price'])  # Only drop rows where 'content' or 'price' is missing

# Step 3: Save the Cleaned Data
cleaned_file_path = r"..\data\structured_messages_cleaned.csv"  
df.to_csv(cleaned_file_path, index=False, encoding='utf-8')

print(f"Cleaned data saved to {cleaned_file_path}")
