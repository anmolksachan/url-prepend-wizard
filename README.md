
# prepend.py - Script to add https:// in front of list of domain names

`prepend.py` is a Python script that takes a file name as input and prepends a banner to the beginning of the file. The output file is saved in the `output` folder.

The given code is a Python script that takes a file containing URLs as input, prepends 'https://' to each URL, and saves the modified URLs to an output directory. The script uses the argparse module to handle command-line arguments, where the input file path is passed using the --file flag, and the output directory path is passed using the --output-dir flag (default: './output').

The prepend_urls() function reads the input file and splits its contents into a list of URLs, prepends 'https://' to each URL using list comprehension, and writes the modified URLs to a new file in the output directory. The function also prints the number of modified URLs and the path of the output file.

## Usage

To use `prepend.py`, run the following command in your terminal:

`python prepend.py --file input.txt` 

Replace `input.txt` with the name of your input file.

If you do not specify an output file name, `prepend.py` will automatically generate one based on the input file name. If you do not want to specify an input file name, `prepend.py` will prompt you to enter one.

If you need help, run the following command:

`python prepend.py --help` 

## Examples

Here are some examples of how to use `prepend.py`:

`python prepend.py --file example.txt` 

This will prepend the default banner to `example.txt` and save the output file in the `output` folder as `example_prepended.txt`.

`python prepend.py --file example.txt --output output_file.txt` 

This will prepend the default banner to `example.txt` and save the output file in the `output` folder as `output_file.txt`.

## Sample Run

<img width="305" alt="image" src="https://user-images.githubusercontent.com/60771253/234646075-f2d9c116-abf8-436a-8792-5dc64d493747.png">

<img width="258" alt="image" src="https://user-images.githubusercontent.com/60771253/234646119-262e4d29-1ba2-4522-9915-19e6edc97b97.png">

<img width="258" alt="image" src="https://user-images.githubusercontent.com/60771253/234646167-4a369f7c-d13f-4c0c-b6ee-2ca30ab2d0f3.png">

## License

`prepend.py` is licensed under the [MIT License](https://raw.githubusercontent.com/anmolksachan/url-prepend-wizard/main/LICENSE).
