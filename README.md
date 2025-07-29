# 🎨 HTML2CSS – Auto Generate CSS Skeleton from HTML

### 🧰 A simple CLI tool to convert HTML structures into CSS selectors automatically.


## 📖 About

`html2css` is a Python-based CLI utility that parses your HTML files and generates a clean, minimal `style.css` skeleton based on the structure. It intelligently detects:

- ✅ Element tags
- ✅ `id` and `class` selectors
- ✅ Repeated elements with `:nth-child()`
- ✅ Predefined responsive `@media` queries


## 📦 Install (Recommended via PyPI)

Install globally using pip from [PyPI](https://pypi.org/project/html2css/):

Install globally via pip:

```bash
pip install --upgrade html2css
```

### ✅ Usage (after installation):

```bash
html2css --input demo.html --output demo.css
```

This will read `demo.html` and generate a CSS structure in `demo.css`.

---

## 💠 Alternate Installation: Run Locally via Git

If you don’t want to use pip, you can run it manually:

### 1️⃣ Clone the Repository:

```bash
git clone https://github.com/SanHub-Soln/css_file_generator.git

cd html2css

pip install beautifulsoup4
```

### 2️⃣ Run the Script Directly:

```bash
python html2css.py --input demo.html --output demo.css
```

Make sure Python is installed and available in your system path.


## 🔄 Example Output (demo.css)

```css
:root {}
html {}
body {}

.container .card:nth-child(1) {}
.container .card:nth-child(2) {}

@media screen and (max-width: 600px) {
  /* Styles for phones */
}

@media screen and (min-width: 601px) and (max-width: 768px) {
  /* Styles for tablets */
}

@media screen and (min-width: 769px) and (max-width: 1024px) {
  /* Styles for small desktops */
}

@media screen and (min-width: 1025px) {
  /* Styles for large screens */
}
```




## 🤝 Contribute
PRs welcome! Open an issue for suggestions or bugs.


## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with proper attribution.


## ⭐️ Show Your Support

If you found this helpful, give the project a ⭐️ on GitHub and share it with fellow developers!

