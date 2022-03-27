# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import click

# @click.command()
# @click.option('--db_id', type=click.STRING, required=True, help='db id plz')
# @click.option('--db_pw', type=click.STRING, required=True, help='db password plz')
# @click.option('--log_level', type=click.STRING, required=False, default='INFO')
# @click.option('--log_name', type=click.STRING, required=False, default='alpha')

@click.command()
#@click.pass_context

# General options.
@click.option('--a', type=float)
@click.option('--b', type=float)

def main(a, b):
    # Use a breakpoint in the code line below to debug your script.
    print(a*b)
    return a*b

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':
    main()