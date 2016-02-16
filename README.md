## Decrypt data

Original data are django db fields converted to string and joined with a
separator between fields and a different separator between rows.  Decrypts
data and exports as csv file

### Dependencies
django
simple-crypt
click


### Usage
Define SIMPLECRYPT_PASSWORD environment variable; same password used to
encrypt the data

```
python decrypt_disclaimers.py file_path_to_decrypt
```

### Optional arguments:
--output: output file path
--fieldsep: a string used to separate field names when outputed from django
--rowsep: a string used to separate records/rows when outputed from django
