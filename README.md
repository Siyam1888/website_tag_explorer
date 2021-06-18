# website_tag_explorer
### Finds popular marketing tags on websites using the [Website Evidence Collector](https://github.com/EU-EDPS/website-evidence-collector)

## Set Up
- Install the latest version of [node.js](https://nodejs.org) 
- Follow the instructions from this [Installation Guide](https://github.com/EU-EDPS/website-evidence-collector#readme)
- Add the folder where npm-packages live usually `C:\Users\[Username]\AppData\Roaming\npm` in windows
- install `pipenv`
    ```sh
    pip install pipenv
    ```
- install the required dependencies from the `pipfile`
    ```sh
    pipenv install
    ```
## Run
- Run the following command to execute the script
    ```sh
    pipenv run python tag_explorer.py
    ```

## Tweaks
- Edit the variable `filename` to change the path of input excel file
- Name the excel sheet with input urls as `Input`
