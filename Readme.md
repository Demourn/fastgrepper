# FastGrepper

FastGrepper is a fast and intuitive CLI tool for searching directories, browsing folders, and opening files directly from your terminal.

## Features

- Quickly search for folders and files in a specified directory
- Browse directory contents interactively
- Open files with your default editor or viewer

## Installation

```bash
# clone and run directly
git clone https://github.com/yourusername/fastgrepper.git
cd fastgrepper
python main.py
```

## Usage

```bash
fastgrepper [OPTIONS] <directory>
```

### Options

- `-r`, `--recursive` : Search directories recursively
- `-o`, `--open <file>` : Open a file directly
- `-h`, `--help` : Show help message

### Example

```bash
fastgrepper /path/to/search
fastgrepper -r /path/to/search
fastgrepper -o README.md
```

## License

MIT

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## Author

[Demourne](https://github.com/Demourn)