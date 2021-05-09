# Pytest + Selenium Login Test

## Requirements
```bash
python -m pip install -r requirements.txt
```


## Download ChromeDriver
[Chrome Driver Download](https://chromedriver.chromium.org/downloads)

1. Download chrome driver from the above page and put into the folder `src/drivers/chromedriver`



## Setup
Set your account/password into `env_config` script and source the file.
```bash
source env_config
```


## Run Tests
```
pytest tests -v
```
