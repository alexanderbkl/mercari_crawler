# Mercari Japan Crawler

A Selenium-based scraper for [jp.mercari.com](https://jp.mercari.com) that searches for products, translates their names and descriptions from Japanese, converts prices from JPY to EUR, and exports results to a WooCommerce-compatible CSV file.

## Features

- Search Mercari Japan by keyword and scrape N product listings
- Automatic translation of product names and descriptions via Google Translate
- JPY → EUR price conversion with a configurable interest/markup rate
- Exports product data (name, price, description, images, SKU, category) to `products.csv` ready for WooCommerce import
- Two input modes: **interactive (manual)** or **batch via `input.csv`**
- Can be packaged as a standalone Windows executable

## Prerequisites

- Python 3.8+
- [Google Chrome](https://www.google.com/chrome/) installed on your system (ChromeDriver is managed automatically)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run as administrator (required for ChromeDriver on some systems):

```bash
python3 main.py
```

You will be prompted to choose an input mode:

```
[1]: Manual input
[2]: Batch input from input.csv
```

### Mode 1 — Manual input

The program will ask you for the following parameters interactively:

| Parameter | Description | Example |
|---|---|---|
| Keyword | Search term for Mercari Japan | `nintendo` |
| Quantity | Number of products to scrape | `10` |
| Category | WooCommerce category for the exported CSV | `Consolas y videojuegos>Nintendo` |
| Interest rate | Markup percentage applied on top of the JPY→EUR conversion | `50` |
| Target language | Language code for translation (see [Language codes](#language-codes)) | `en` |

### Mode 2 — Batch input (`input.csv`)

Edit the `input.csv` file in the project root. Each row defines one search job:

```csv
Palabra clave,Nº productos,Categoría,Porcentaje,Idioma
Nintendo,2,Sega>Mark 3,70,en
Sega Saturn,1,Sega>Saturn,70,en
```

| Column | Description |
|---|---|
| `Palabra clave` | Search keyword |
| `Nº productos` | Number of products to scrape |
| `Categoría` | WooCommerce product category |
| `Porcentaje` | Interest/markup rate (%) |
| `Idioma` | Target translation language code |

## Output

A `products.csv` file is created (or appended to) in the same directory as `main.py`. It is formatted for direct import into WooCommerce and includes the following columns:

`Explicit URL`, `Type`, `Published`, `Is featured?`, `Visibility in catalog`, `Tax status`, `In stock?`, `Backorders allowed?`, `Sold individually?`, `Allow customer reviews?`, `Parent`, `Name`, `Regular price`, `Stock`, `url`, `Images`, `Description`, `SKU`, `Categories`

> **Price formula:** `EUR price = (JPY price × 0.0068) × (1 + interest_rate / 100)`

## Building a standalone executable (Windows)

```bash
python -m PyInstaller --onefile --uac-admin main.py
```

The resulting `main.exe` will be created in the `./dist` folder.

## Language codes

Use these codes for the **Idioma** / **Target language** field:

| Code | Language | Code | Language | Code | Language |
|---|---|---|---|---|---|
| `af` | Afrikaans | `gu` | Gujarati | `pl` | Polish |
| `sq` | Albanian | `ht` | Haitian Creole | `pt` | Portuguese |
| `am` | Amharic | `ha` | Hausa | `pa` | Punjabi |
| `ar` | Arabic | `haw` | Hawaiian | `ro` | Romanian |
| `hy` | Armenian | `he` | Hebrew | `ru` | Russian |
| `az` | Azerbaijani | `hi` | Hindi | `sm` | Samoan |
| `eu` | Basque | `hmn` | Hmong | `gd` | Scots Gaelic |
| `be` | Belarusian | `hu` | Hungarian | `sr` | Serbian |
| `bn` | Bengali | `is` | Icelandic | `st` | Sesotho |
| `bs` | Bosnian | `ig` | Igbo | `sn` | Shona |
| `bg` | Bulgarian | `id` | Indonesian | `sd` | Sindhi |
| `ca` | Catalan | `ga` | Irish | `si` | Sinhala |
| `ceb` | Cebuano | `it` | Italian | `sk` | Slovak |
| `ny` | Chichewa | `ja` | Japanese | `sl` | Slovenian |
| `zh-cn` | Chinese (Simplified) | `jw` | Javanese | `so` | Somali |
| `zh-tw` | Chinese (Traditional) | `kn` | Kannada | `es` | Spanish |
| `co` | Corsican | `kk` | Kazakh | `su` | Sundanese |
| `hr` | Croatian | `km` | Khmer | `sw` | Swahili |
| `cs` | Czech | `ko` | Korean | `sv` | Swedish |
| `da` | Danish | `ku` | Kurdish (Kurmanji) | `tg` | Tajik |
| `nl` | Dutch | `ky` | Kyrgyz | `ta` | Tamil |
| `en` | English | `lo` | Lao | `te` | Telugu |
| `eo` | Esperanto | `la` | Latin | `th` | Thai |
| `et` | Estonian | `lv` | Latvian | `tr` | Turkish |
| `tl` | Filipino | `lt` | Lithuanian | `uk` | Ukrainian |
| `fi` | Finnish | `lb` | Luxembourgish | `ur` | Urdu |
| `fr` | French | `mk` | Macedonian | `ug` | Uyghur |
| `fy` | Frisian | `mg` | Malagasy | `uz` | Uzbek |
| `gl` | Galician | `ms` | Malay | `vi` | Vietnamese |
| `ka` | Georgian | `ml` | Malayalam | `cy` | Welsh |
| `de` | German | `mt` | Maltese | `xh` | Xhosa |
| `el` | Greek | `mi` | Maori | `yi` | Yiddish |
| `mr` | Marathi | `mn` | Mongolian | `yo` | Yoruba |
| `my` | Myanmar (Burmese) | `ne` | Nepali | `zu` | Zulu |
| `no` | Norwegian | `or` | Odia | `ps` | Pashto |
| `fa` | Persian | | | | |
