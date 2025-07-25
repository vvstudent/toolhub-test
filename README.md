# 🔧 ToolHub Sample Repository

A comprehensive sample repository for testing ToolHub VS Code extension's GitHub integration capabilities.

## 🎯 Purpose

This repository provides a complete set of sample Python tools designed to test and demonstrate:

- ✅ GitHub repository integration
- ✅ Tool synchronization and import
- ✅ Various parameter types and form controls
- ✅ Rich console output and error handling
- ✅ Multi-category tool organization
- ✅ Enterprise admin features

## 🚀 Quick Start

### 1. **Setup Repository**
```bash
# Option A: Fork this repository
# Option B: Create new repository and copy files
# Option C: Use this repository URL directly for testing
```

### 2. **Configure ToolHub**
1. Open VS Code with ToolHub extension installed
2. Click **ToolHub icon** (🔧) in Activity Bar
3. Click **"Repository Admin"** button
4. Set your **GitHub Personal Access Token**
5. Add repository: `https://github.com/your-username/your-repo`
6. Set tools directory: `python_tools`
7. Click **"🔄 Sync"** to import tools

### 3. **Verify Integration**
- Should import **8 sample tools**
- Tools appear in ToolHub explorer
- Organized by categories (Text Processing, Security, etc.)
- All tools executable with rich parameter forms

## 📦 What's Included

### **📁 File Structure**
```
sample_github_repo/
├── python_tools/              # ← ToolHub tools directory
│   ├── tools.py              # 5 core sample tools
│   ├── utilities.py          # 3 additional utility tools
│   ├── requirements.txt      # Python dependencies
│   └── README.md            # Tools documentation
├── docs/                     # Additional documentation
│   ├── TESTING_GUIDE.md     # Detailed testing instructions
│   └── TROUBLESHOOTING.md   # Common issues and solutions
└── README.md                # This file
```

### **🛠️ Sample Tools Overview**

| Tool | Category | Features Demonstrated |
|------|----------|----------------------|
| 📊 Text Analyzer | Text Processing | Textarea, checkbox, rich analysis output |
| 🔐 Password Generator | Security | Number input, multiple checkboxes, validation |
| 📄 JSON Formatter | Data Processing | Textarea, select dropdown, error handling |
| 🔒 Hash Generator | Security | Textarea, multiselect, multiple algorithms |
| 🔗 URL Encoder/Decoder | Web Development | Textarea, select options, auto-detection |
| 📝 Base64 Encoder/Decoder | Data Processing | Textarea, auto-operation detection |
| 🎨 Color Palette Generator | Design | Text input, select, multiselect, color theory |
| 📱 QR Code Generator | Utilities | Textarea, multiple selects, data formatting |

## 🔧 GitHub Integration Testing

### **Prerequisites**
- ✅ GitHub Personal Access Token with `repo` permissions
- ✅ ToolHub VS Code extension installed
- ✅ Admin privileges configured in ToolHub settings

### **Test Scenarios**

#### **Scenario 1: Basic Integration**
1. Add repository with default settings
2. Sync tools and verify 8 tools imported
3. Test tool execution with various parameters

#### **Scenario 2: Custom Directory**
1. Move tools to different directory (e.g., `custom_tools/`)
2. Update ToolHub configuration
3. Re-sync and verify tools still work

#### **Scenario 3: Branch Testing**
1. Create feature branch with modified tools
2. Switch ToolHub to use feature branch
3. Verify changes are reflected in ToolHub

#### **Scenario 4: Error Handling**
1. Test with invalid repository URL
2. Test with incorrect tools directory
3. Test with invalid GitHub token
4. Verify appropriate error messages

## 📊 Expected Results

### **✅ Success Indicators**
- **Tool Count:** 8 tools imported successfully
- **Categories:** Tools organized in 6 categories
- **Functionality:** All tools executable with proper forms
- **Output:** Rich console output with emojis and formatting
- **Error Handling:** Graceful error messages for invalid inputs

### **🔍 Verification Checklist**
- [ ] Repository added without errors
- [ ] All 8 tools appear in ToolHub explorer
- [ ] Tools are categorized correctly
- [ ] Parameter forms render properly
- [ ] Tool execution produces expected output
- [ ] Error cases handled gracefully
- [ ] Sync operation completes successfully

## 🐛 Troubleshooting

### **Common Issues**

#### **No Tools Imported**
```
Possible Causes:
❌ Incorrect repository URL
❌ Invalid GitHub token
❌ Wrong tools directory path
❌ Repository is private without proper permissions

Solutions:
✅ Verify repository URL format
✅ Check token permissions (needs 'repo' scope)
✅ Confirm 'python_tools' directory exists
✅ Test with public repository first
```

#### **Partial Tool Import**
```
Possible Causes:
❌ Syntax errors in tool files
❌ Missing required tool structure
❌ Import/export issues

Solutions:
✅ Check VS Code Developer Console for errors
✅ Validate Python syntax in tool files
✅ Ensure proper tool export format
```

#### **Sync Failures**
```
Possible Causes:
❌ Network connectivity issues
❌ GitHub API rate limiting
❌ Repository access permissions

Solutions:
✅ Check internet connection
✅ Wait and retry (rate limiting)
✅ Verify repository permissions
```

## 🔒 Security Notes

- **Token Security:** Never commit GitHub tokens to repositories
- **Permissions:** Use minimal required token permissions
- **Admin Access:** Properly configure ToolHub admin users
- **Audit Logging:** All operations are logged for audit purposes

## 📚 Additional Resources

- **[ToolHub Documentation](../docs/TESTING_GUIDE.md)** - Detailed testing guide
- **[Troubleshooting Guide](../docs/TROUBLESHOOTING.md)** - Common issues and solutions
- **[GitHub Token Setup](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)** - Official GitHub documentation

## 🤝 Contributing

To add more sample tools:

1. **Follow Tool Structure:**
   ```python
   def new_tool():
       return {
           "name": "Tool Name",
           "description": "Tool description", 
           "category": "Category",
           "parameters": [...],
           "implementation": "..."
       }
   ```

2. **Add to Export:**
   ```python
   TOOLS = [existing_tools..., new_tool()]
   ```

3. **Test Integration:**
   - Sync repository in ToolHub
   - Verify new tool appears
   - Test functionality

## 📄 License

This sample repository is provided for testing and demonstration purposes under the MIT License.

---

**🎉 Ready to test your ToolHub GitHub integration!**

Use this repository to verify that your ToolHub extension can successfully sync and execute tools from GitHub repositories.