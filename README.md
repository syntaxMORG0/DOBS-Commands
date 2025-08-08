# 𝑫𝑶𝑩𝑺

Don't worry Open IDE is not sunsetted im just on a sideproject

## Features

- **Math operations:** ADD, SUB, MUL, DIV, POW, MOD, FACT
- **String operations:** PRINT, REVERSE, UPPER, LOWER
- **Data storage:** SET, DEL, SAVE, LOAD (persists to `dobs_data.json`)
- **Condition evaluation:** IF
- **Other:** CLEAR, ABOUT, OPEN (opens URLs in your default browser), HELP, EXIT

## Usage

1. **Start the program:**
   ```bash
   python3 kernel.py
   ```

2. **Type `HELP`** to see all available commands.

3. **Data commands:**
   - `SET` — Store a key-value pair.
   - `DEL` — Delete a key.
   - `SAVE` — Save all data to `dobs_data.json`.
   - `LOAD` — Load data from `dobs_data.json`.

4. **Open a URL:**
   - `OPEN` — Enter a URL to open it in your default browser (`$BROWSER` is used).

5. **Exit:**
   - `EXIT` — Quit the interpreter.

## Example Session

```
1> HELP
1> SET
1 SET> Key: name
1 SET> Value: Alice
2> SAVE
2> Data saved to dobs_data.json
3> LOAD
3> Data loaded: {'name': 'Alice'}
4> PRINT
4 PRINT> Hello, world!
4> Hello, world!
5> EXIT
```

## Requirements

- Python 3.8+
- [colorama](https://pypi.org/project/colorama/)

Install dependencies:
```bash
pip install colorama
```

## License

MIT

---

Made by [![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=SyntaxMORG0&message=Profile&color=lightgrey&logo=github)]
