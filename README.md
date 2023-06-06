# Auto-GPT OANDA Plugin 📈
The AutoGPT MetaTrader Plugin is a software tool that enables traders to connect their MetaTrader 4 or 5 trading account to Auto-GPT.

[![GitHub Repo stars](https://img.shields.io/github/stars/RuiHirano/Auto-GPT-OANDA-Plugin?style=social)](https://github.com/RuiHirano/Auto-GPT-OANDA-Plugin/stargazers)


## 💡 Key Features:
- 💰 **Place Trades**
- ℹ️ **Account Information**
- ⛔️ **Close Trade**
- ❌ **Close All Trades**
- 🕯 **Candlestick Data**
- 📝 **Modify Trades**
- 📝 **Indicators** (In progress)

## 🔧 Installation

Follow these steps to configure the Auto-GPT OANDA Plugin:

### 1. Clone the Auto-GPT-OANDA-Plugin repository
Clone this repository and navigate to the `Auto-GPT-OANDA-Plugin` folder in your terminal:

```bash
git clone https://github.com/RuiHirano/Auto-GPT-OANDA-Plugin.git
```

### 2. Install required dependencies
Execute the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Package the plugin as a Zip file
Compress the `Auto-GPT-OANDA-Plugin` folder or [download the repository as a zip file](https://github.com/RuiHirano/Auto-GPT-OANDA-Plugin/archive/refs/heads/master.zip).

### 4. Install Auto-GPT
If you haven't already, clone the [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) repository, follow its installation instructions, and navigate to the `Auto-GPT` folder.

### 5. Copy the Zip file into the Auto-GPT Plugin folder
Transfer the zip file from step 3 into the `plugins` subfolder within the `Auto-GPT` repo.

### 6. Locate the `.env.template` file
Find the file named `.env.template` in the main `/Auto-GPT` folder.

### 7. Create and rename a copy of the file
Duplicate the `.env.template` file and rename the copy to `.env` inside the `/Auto-GPT` folder.

### 8. Edit the `.env` file
Open the `.env` file in a text editor. Note: Files starting with a dot might be hidden by your operating system.

### 9. Add MetaTrader configuration settings
Append the following configuration settings to the end of the file:

```ini
################################################################################
### OANDA
################################################################################
OANDA_ACCOUNT_ID=
OANDA_ACCESS_TOKEN=
OANDA_ENVIRONMENT=
OANDA_ENABLE_COMMANDS=order_create,order_cancel,order_details,order_list,trade_close,trade_details,trades_list,position_close,position_details,position_list,instruments_candles,get_account_summary,get_account_instruments,autochartist,calendar,commitments_of_traders,spreads
```
- Create a OANDA MT4/MT5 account and generate API access token.
- Set `OANDA_ACCOUNT_ID` to your OANDA account ID. 
- Set `OANDA_ACCESS_TOKEN` to your OANDA access token.
- Set `OANDA_ENVIRONMENT`, `live` or `practice`.
- Set `OANDA_ENABLE_COMMANDS` to be enabled commands.

### 10. Allowlist Plugin
In your `.env` search for `ALLOWLISTED_PLUGINS` and add this Plugin:

```ini
################################################################################
### ALLOWLISTED PLUGINS
################################################################################
#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=AutoGPTOANDAPlugin
```
### 11. Review Available Commands
You can review the available commands and indicators [here](/src/auto_gpt_oanda_plugin/commands.txt).

## 🧪 Test the Auto-GPT OANDA Plugin

Writing...

## 📉 Indicators (In-Progress):
-  **Relative Strength Index (RSI)**
-  **Volume**
-  **Moving Averages (SMA, EMA, WMA, MAE, OsMA, MACD)**
-  **Fibonacci Retracement**
-  **Bollinger Bands**
-  **Money Fund Index (MFI)**