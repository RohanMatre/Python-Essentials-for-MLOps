import json
import click

def formatter(string, sort_keys=True,indent=4):
    #load incoming string into JSON
    loaded_json = json.loads(string)
    # dump as string 
    return json.dumps(loaded_json,sort_keys=sort_keys, indent = indent)

@click.command()
@click.argument('path')
def main(path):
    with open(path, 'r') as _f:
        print(
            formatter(_f.read(), sort_keys=sort_keys)
        )

if __name__ == '__main__':
    main()