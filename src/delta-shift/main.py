import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Define the ticker for the Swiss Market Index
smi_ticker = "^SSMI"

# Download SMI historical data for the period 2024-01-01 to 2025-01-01
smi = yf.Ticker(smi_ticker)
smi_histo = smi.history(start="2024-01-01", end="2025-01-01")

# Calculate a 30-day moving average of the closing price
smi_histo['30MA'] = smi_histo['Close'].rolling(window=30).mean()

# Create the main figure
plt.figure(figsize=(14, 7))

# Plot the SMI closing price
plt.plot(smi_histo.index, smi_histo['Close'], label='SMI Close', color='blue', linewidth=2)

# Plot the 30-day moving average
plt.plot(smi_histo.index, smi_histo['30MA'], label='30-Day Moving Average', color='red', linestyle='--', linewidth=2)

# Add labels and title
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (CHF)", fontsize=12)
plt.title("Swiss Market Index (SMI) Price with 30-Day Moving Average (2024)", fontsize=14)

# Enable grid for a cleaner look
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend to distinguish the lines
plt.legend(fontsize=12)

# --- Some Cool Extras ---

# 1. Highlight the maximum close point
max_date = smi_histo['Close'].idxmax()
max_value = smi_histo['Close'].max()
plt.scatter(max_date, max_value, color='green', s=100, zorder=5, label='Max Close')
plt.annotate(f"Max: {max_value:.2f}",
             xy=(max_date, max_value),
             xytext=(max_date, max_value + 50),
             arrowprops=dict(facecolor='black', arrowstyle="->"),
             fontsize=10, color='green')

# 2. Fill the area between the close price and the moving average
#    (only fill where the Close is above the moving average)
plt.fill_between(smi_histo.index,
                 smi_histo['Close'],
                 smi_histo['30MA'],
                 where=(smi_histo['Close'] >= smi_histo['30MA']),
                 facecolor='blue',
                 alpha=0.1,
                 interpolate=True)

# 3. Mark the start and end of our analysis period
start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2025, 1, 1)
plt.axvline(start_date, color='purple', linestyle=':', linewidth=1.5, label='Start Date')
plt.axvline(end_date, color='orange', linestyle=':', linewidth=1.5, label='End Date')

# Adjust legend to include all elements (avoid duplicate labels)
plt.legend(fontsize=10, loc='best')

# Show the plot
plt.tight_layout()
plt.show()

