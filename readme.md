## Setup
`pip install -r requirements.txt `

## Run Tests
`python tests/app_test.py`

## Run application
`python app.py`

## Initialize Database
This application uses built in sqlite3. We don't require any setup.

### Description
My approach was to use sqlite3 to create a relational table that can hold the transaction information. I use flask as my framework to prove the api that drives the file submission.
An external thread reads the files that have been uploaded and inserts them into
the database. The external thread also removes those threads to save us space and to
indicate the file has already been processed.
Considering the fact that my time was limited there are plenty of features that I would have added. First and foremost, it was important for me to make sure that
the file uploading was handled properly as well as inserting into the table. This is the main driver of the application and was within what I could do in 2 hours.

Some features to be added:
1) Normalization - Currently we are only appending records into a singular existing table. We can easly convert this into third normal form by providing different tables with primary keys and foreign keys.

```
Customer Table
---------------
id (PRIMARY KEY)
firt_name
last_name
street_address
zip

Products
----------
product_id (PRIMARY KEY)
product_name

Purchases
-------------
user_id (FOREIGN KEY)
purchase_id (FOREIGN KEY)
product_purchase_amount
timestamp
```

2) ORM - An ORM would help us maintain code quality and allow us a way to seamlessly insert records into the tables.

3) Irregularity Detection - Currently any data can be parsed and inserting which makes as vulnerable to sql injections. We can handle this error by only taking in data of a certain format
and serializing. An ORM can help us by making it easy to provide validity checks across columns.

4) Tests - The tests I provided are very simple. I would like to add tests for the individual routes.
