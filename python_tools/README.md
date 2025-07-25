# 🔧 ToolHub Sample Repository

This repository contains sample Python tools designed to demonstrate the ToolHub VS Code extension's GitHub integration capabilities.

## 📁 Repository Structure

```
sample_github_repo/
├── python_tools/           # Main tools directory
│   ├── tools.py           # Core sample tools
│   ├── utilities.py       # Additional utility tools  
│   ├── requirements.txt   # Python dependencies
│   └── README.md         # This file
├── docs/                 # Documentation (optional)
└── README.md            # Repository overview
```

## 🛠️ Available Tools

### **Core Tools** (`tools.py`)

1. **📊 Text Analyzer**
   - Analyzes text for word count, character count, readability
   - Provides word frequency analysis
   - Calculates Flesch Reading Ease score

2. **🔐 Password Generator**
   - Generates secure passwords with customizable options
   - Supports multiple character sets
   - Includes strength analysis

3. **📄 JSON Formatter**
   - Formats and validates JSON data
   - Supports various indentation options
   - Provides syntax error detection

4. **🔒 Hash Generator**
   - Generates MD5, SHA1, SHA256, SHA512 hashes
   - Supports multiple output formats
   - Includes security recommendations

5. **🔗 URL Encoder/Decoder**
   - Encodes and decodes URLs
   - Supports different encoding types
   - Shows character-by-character changes

### **Utility Tools** (`utilities.py`)

6. **📝 Base64 Encoder/Decoder**
   - Encodes text to Base64 and vice versa
   - Auto-detects operation needed
   - Supports line wrapping

7. **🎨 Color Palette Generator**
   - Generates harmonious color palettes
   - Supports multiple color harmony types
   - Outputs in various formats (HEX, RGB, HSL, CSS)

8. **📱 QR Code Generator**
   - Generates QR code specifications
   - Supports multiple data types (URL, WiFi, Email, etc.)
   - Provides usage recommendations

## 🚀 Testing with ToolHub

### **Setup Instructions**

1. **Create GitHub Repository:**
   ```bash
   # Create a new repository on GitHub
   # Upload these files to: your-repo/python_tools/
   ```

2. **Configure ToolHub:**
   - Open VS Code with ToolHub extension
   - Click "Repository Admin" in ToolHub panel
   - Set your GitHub Personal Access Token
   - Add repository: `https://github.com/your-username/your-repo`
   - Set tools directory: `python_tools`

3. **Sync Tools:**
   - Click "🔄 Sync" to import tools
   - Tools will appear in ToolHub explorer

### **Expected Results**

After syncing, you should see **8 tools** in ToolHub:

- 📊 Text Analyzer
- 🔐 Password Generator  
- 📄 JSON Formatter
- 🔒 Hash Generator
- 🔗 URL Encoder/Decoder
- 📝 Base64 Encoder/Decoder
- 🎨 Color Palette Generator
- 📱 QR Code Generator

### **Testing Features**

Each tool demonstrates different ToolHub capabilities:

- **Form Controls:** Text inputs, textareas, dropdowns, checkboxes, multi-select
- **Parameter Types:** Required/optional, defaults, validation, min/max values
- **Categories:** Tools are organized by category (Text Processing, Security, etc.)
- **Rich Output:** Formatted console output with emojis and structure
- **Error Handling:** Graceful error messages and user guidance

## 🔧 Tool Development Guidelines

These sample tools follow ToolHub best practices:

### **Tool Structure**
```python
def tool_name():
    return {
        "name": "Display Name",
        "description": "Tool description",
        "category": "Category Name",
        "parameters": [...],
        "implementation": "..."
    }
```

### **Parameter Types**
- `text` - Single line text input
- `textarea` - Multi-line text input  
- `number` - Numeric input with min/max
- `select` - Dropdown selection
- `multiselect` - Multiple choice selection
- `checkbox` - Boolean toggle

### **Best Practices**
- ✅ Use descriptive names and descriptions
- ✅ Provide helpful placeholders and defaults
- ✅ Include parameter validation
- ✅ Add rich console output with emojis
- ✅ Handle errors gracefully
- ✅ Provide usage tips and guidance

## 📋 Requirements

- **Python 3.6+** (uses only built-in libraries)
- **ToolHub VS Code Extension**
- **GitHub Personal Access Token** with repo permissions

## 🔍 Troubleshooting

### **No Tools Appear**
- Verify repository URL is correct
- Check GitHub token permissions
- Ensure `python_tools` directory exists
- Check ToolHub console for error messages

### **Sync Fails**
- Verify GitHub token is valid
- Check repository is accessible
- Ensure tools directory path is correct
- Review network connectivity

### **Tool Execution Errors**
- Check Python syntax in tool implementations
- Verify all required parameters are provided
- Review console output for specific error messages

## 📞 Support

For ToolHub extension support:
- Check VS Code Developer Console (`Help > Toggle Developer Tools`)
- Look for ToolHub logs (🚀, 🔧, 🔄 prefixes)
- Verify admin privileges in VS Code settings

## 📄 License

This sample repository is provided for testing and demonstration purposes.

---

**Happy Testing! 🎉**

Use these tools to verify your ToolHub GitHub integration is working correctly.