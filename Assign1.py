import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
file_path = 'D:/Electric_Vehicle_Population_Data.csv'
ev_data = pd.read_csv(file_path)

# 1. Document Missing Values: Check for missing values and document their frequency and distribution
missing_values = ev_data.isnull().sum()
missing_percentage = (ev_data.isnull().sum() / len(ev_data) * 100)
missing_summary = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})
print("Missing Values Summary:")
print(missing_summary)

# 2. Missing Value Strategies: Apply mean/median imputation and dropping rows with missing values
# Mean Imputation
ev_data_mean_imputed = ev_data.fillna(ev_data.mean(numeric_only=True))

# Median Imputation
ev_data_median_imputed = ev_data.fillna(ev_data.median(numeric_only=True))

# Drop rows with missing values
ev_data_dropped_na = ev_data.dropna()

# Compare shapes
print("Original Data Shape:", ev_data.shape)
print("Mean Imputed Data Shape:", ev_data_mean_imputed.shape)
print("Median Imputed Data Shape:", ev_data_median_imputed.shape)
print("Data Shape After Dropping NAs:", ev_data_dropped_na.shape)

# 3. Feature Encoding: Apply one-hot encoding to 'Make' and 'Model'
ev_data_encoded = pd.get_dummies(ev_data, columns=['Make', 'Model'], drop_first=True)
print("Sample of One-Hot Encoded Data:")
print(ev_data_encoded.head())

# 4. Normalization: Normalize numerical features
# Define columns to normalize
numerical_cols = ['Electric Range', 'Base MSRP', 'Model Year']
scaler = MinMaxScaler()

# Normalize selected columns and update DataFrame
ev_data_normalized = ev_data.copy()
ev_data_normalized[numerical_cols] = scaler.fit_transform(ev_data_normalized[numerical_cols])
print("Sample of Normalized Data:")
print(ev_data_normalized[numerical_cols].head())

# Descriptive Statistics
descriptive_stats = ev_data[numerical_cols].describe()
print("Descriptive Statistics:")
print(descriptive_stats)

import matplotlib.pyplot as plt

# Count of EVs by County
county_distribution = ev_data['County'].value_counts().nlargest(20)

# Bar plot of EV distribution by county
plt.figure(figsize=(12, 6))
county_distribution.plot(kind='bar')
plt.title('Electric Vehicles Distribution by County')
plt.xlabel('County')
plt.ylabel('Number of EVs')
plt.xticks(rotation=45)
plt.show()

# Model Popularity Analysis
model_popularity = ev_data['Model'].value_counts().nlargest(20)

# Bar plot for model popularity
plt.figure(figsize=(12, 6))
model_popularity.plot(kind='bar')
plt.title('Popularity of Different EV Models')
plt.xlabel('EV Model')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Correlation Matrix
correlation_matrix = ev_data_normalized[numerical_cols].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Histogram for Electric Range
plt.figure(figsize=(10, 6))
ev_data['Electric Range'].hist(bins=30, color='blue', alpha=0.7)
plt.title('Histogram of Electric Range')
plt.xlabel('Electric Range')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()

# Scatter plot between Electric Range and Base MSRP
plt.figure(figsize=(10, 6))
plt.scatter(ev_data_normalized['Electric Range'], ev_data_normalized['Base MSRP'], alpha=0.5)
plt.title('Electric Range vs. Base MSRP')
plt.xlabel('Electric Range')
plt.ylabel('Base MSRP')
plt.grid(True)
plt.show()

# Boxplot for Electric Range by Model Year
plt.figure(figsize=(10, 6))
sns.boxplot(x='Model Year', y='Electric Range', data=ev_data)
plt.title('Boxplot of Electric Range by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Electric Range')
plt.xticks(rotation=45)
plt.show()

# Bar chart of EV distribution by County
plt.figure(figsize=(12, 6))
county_counts = ev_data['County'].value_counts().head(10)  # Top 10 counties
county_counts.plot(kind='bar', color='green', alpha=0.7)
plt.title('Top 10 Counties with the Most Electric Vehicles')
plt.xlabel('County')
plt.ylabel('Number of EVs')
plt.xticks(rotation=45)
plt.show()

# Get the top 10 counties by total number of EVs
top_counties = ev_data['County'].value_counts().nlargest(20).index
# Filter the data to include only the top counties
ev_types_top_counties = ev_data[ev_data['County'].isin(top_counties)]
# Stacked bar chart for EV types across counties
ev_types_by_county = ev_types_top_counties.groupby(['County', 'Electric Vehicle Type']).size().unstack(fill_value=0)

# Plotting
ev_types_by_county.plot(kind='bar', stacked=True, figsize=(12, 6), alpha=0.7)
plt.title('Distribution of Electric Vehicle Types by County')
plt.xlabel('County')
plt.ylabel('Number of EVs')
plt.xticks(rotation=45)
plt.legend(title='Electric Vehicle Type')
plt.show()

# Count of EV registrations by Model Year
ev_adoption_trends = ev_data['Model Year'].value_counts().sort_index()

# Line plot for EV adoption trends
plt.figure(figsize=(10, 6))
ev_adoption_trends.plot(kind='line', marker='o', color='purple', alpha=0.7)
plt.title('EV Adoption Trends by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Number of EVs Registered')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Group by Model Year and Model
model_popularity_over_time = ev_data.groupby(['Model Year', 'Model']).size().unstack(fill_value=0)

# Plotting model popularity over time (top 5 models for clarity)
top_models = model_popularity_over_time.sum().nlargest(5).index
model_popularity_over_time[top_models].plot(kind='line', figsize=(12, 6), marker='o')
plt.title('Popularity of Top EV Models Over Time')
plt.xlabel('Model Year')
plt.ylabel('Number of Registrations')
plt.legend(title='EV Model', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()




