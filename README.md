# wordcountsimple
================

📖 Overview
-----------

The `wordcountsimple` project is a Python implementation of a simple word count program. This program takes a text file as input and outputs the frequency of each word in the file.

⚙️ Installation Instructions
---------------------------

### Using pip

You can install the `wordcountsimple` package using pip:
```
pip install .
```
### From Source

To install from source, clone the repository and run:
```
python setup.py install
```
🚀 Usage Examples
-----------------

### Command Line Interface

The `wordcountsimple` program can be used from the command line:
```
$ python wordcountsimple.py example.txt
```
This will output the word frequency for the file `example.txt`.

### Python API

The `wordcountsimple` module can also be used as a Python API:
```python
import wordcountsimple

wordcounts = wordcountsimple.count_words('example.txt')
print(wordcounts)
```
This will output a dictionary with the word frequency for the file `example.txt`.

✅ Testing Information
-------------------

### Running Tests

To run the tests, use the following command:
```
python -m unittest discover tests
```
This will run the test suite for the `wordcountsimple` package.

### Test Coverage

The test suite covers the following functionality:

* Counting words in a file
* Handling empty files
* Handling non-text files

📜 License
---------

The `wordcountsimple` project is licensed under the MIT License. See [LICENSE](LICENSE) for details.