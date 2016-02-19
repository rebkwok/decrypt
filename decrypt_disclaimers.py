import click
import csv
import os
import time


from django.utils.encoding import smart_str
from simplecrypt import encrypt, decrypt


PASSWORD = os.environ.get('SIMPLECRYPT_PASSWORD')


@click.command()
@click.argument('input', type=click.File('rb'))
@click.option('--output')
@click.option('--fieldsep', default='&&&&&')
@click.option('--rowsep', default='@@@@@')
def decrypt_disclaimers(input, output, fieldsep, rowsep):

    if output is None:
        # timestamp the filename with the datetime it was downloaded
        timestamp = time.strftime(
            '%Y%m%d%H%M', time.gmtime(os.path.getctime(input.name))
        )
        output = 'disclaimers_backup_{}.csv'.format(timestamp)

    encrypted_text = input.read()
    decrypted_text = decrypt(PASSWORD, encrypted_text)
    decrypted_text = str(decrypted_text).lstrip("b'").rstrip("'")
    decrypted_data = decrypted_text.split(fieldsep)

    with open(output, 'wt') as out:
        wr = csv.writer(out)

        for entry in decrypted_data:
            data = entry.split(rowsep)
            wr.writerow([smart_str(datum) for datum in data])

    print(
        '{} records decrypted and written to {}'.format(
            len(decrypted_data) - 1, output
        )
    )


if __name__ == '__main__':
    decrypt_disclaimers()
