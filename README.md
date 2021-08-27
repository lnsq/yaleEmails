# Yale Emails
This repository utlizes the API functionality from https://yalies.io/ to pull email information from the Yale University directory. 

## Setup
1. Python3

Make sure you have Python3 installed.

https://www.python.org/downloads/

2. requirements.txt

The `requirements.txt` file lists all the Python libraries needed, and can be installed by running the following command:

```
pip install -r requirements.txt
```

## Useage
Refer to https://yalies.io/apidocs for more details. 

The user needs to provide an authorization token, which can be generated at the Yalies.io API doc page. The user also needs to provide a .json file that describes their query. There is an example .json file in the repository that will return the emails of students in Yale College in the class of 2025. For convenience, it's also below:

```
{
    "filters": 
    {
        "school_code": ["YC"], 
        "year": 2025
    }
}
```

Once these two requirements are fulfilled, the following command can be run:

```
python /path/to/dir/get_emails.py -t <token> -p <filename.json>
```

If you would like to save the emails to a separate .csv file, the following command can be run:

```
python /path/to/dir/get_emails.py -t <token> -p <filename>.json > <out_filename>.csv
```
