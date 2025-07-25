# 🔧 ToolHub GitHub Integration - Troubleshooting Guide

This guide helps you diagnose and resolve common issues when testing ToolHub's GitHub integration.

## 🚨 Quick Diagnostic Checklist

Before diving into specific issues, run through this quick checklist:

- [ ] **VS Code Extension:** ToolHub extension installed and enabled
- [ ] **GitHub Token:** Valid Personal Access Token with correct permissions
- [ ] **Repository Access:** Repository exists and is accessible
- [ ] **Admin Privileges:** User has admin access in ToolHub settings
- [ ] **Network Connection:** Stable internet connection
- [ ] **File Structure:** Correct directory structure in repository

## 🔍 Common Issues and Solutions

### **1. Repository Connection Issues**

#### **❌ "Repository validation failed"**

**Symptoms:**
- Cannot add repository to ToolHub
- Error message about repository validation
- Repository appears as "Inactive"

**Possible Causes:**
```
🔍 Invalid repository URL format
🔍 Repository doesn't exist or is private
🔍 GitHub token lacks necessary permissions
🔍 Network connectivity issues
```

**Solutions:**
```
✅ Verify URL format: https://github.com/username/repository
✅ Check repository exists and is accessible
✅ Ensure token has 'repo' permission for private repos
✅ Test with public repository first
✅ Check internet connection and GitHub status
```

**Debug Steps:**
1. Open VS Code Developer Console (`Help > Toggle Developer Tools`)
2. Look for network errors in Console tab
3. Check Network tab for failed GitHub API calls
4. Verify repository URL in browser

---

### **2. Authentication Issues**

#### **❌ "Invalid GitHub token" or "Authentication failed"**

**Symptoms:**
- Cannot set GitHub token
- Authentication errors when adding repositories
- Token validation fails

**Possible Causes:**
```
🔍 Token has expired or been revoked
🔍 Token lacks required permissions
🔍 Token format is incorrect (extra spaces, etc.)
🔍 GitHub account issues
```

**Solutions:**
```
✅ Generate new Personal Access Token
✅ Ensure token has 'repo' permission
✅ Copy token without extra spaces or characters
✅ Test token with GitHub API directly
✅ Check GitHub account status
```

**Token Setup Guide:**
1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Click "Generate new token (classic)"
3. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `public_repo` (Access public repositories)
4. Copy token immediately (you won't see it again)

---

### **3. Tool Import Issues**

#### **❌ "No tools found" or "Sync completed: 0 tools imported"**

**Symptoms:**
- Sync operation completes but no tools appear
- Empty ToolHub explorer after sync
- "No tools found in directory" message

**Possible Causes:**
```
🔍 Incorrect tools directory path
🔍 Tools directory doesn't exist in repository
🔍 Tool files have syntax errors
🔍 Tool files don't follow required format
🔍 Wrong branch specified
```

**Solutions:**
```
✅ Verify 'python_tools' directory exists in repository
✅ Check tools directory path in ToolHub configuration
✅ Ensure tool files have correct Python syntax
✅ Verify tool export format (TOOLS = [...])
✅ Check correct branch is specified
```

**File Structure Verification:**
```
your-repository/
├── python_tools/          ← This directory must exist
│   ├── tools.py          ← Tool files must be here
│   ├── utilities.py      ← Additional tool files
│   └── requirements.txt  ← Optional dependencies
└── README.md
```

---

### **4. Tool Execution Issues**

#### **❌ Tools imported but fail to execute**

**Symptoms:**
- Tools appear in ToolHub explorer
- Tool execution produces errors
- Parameter forms don't render correctly

**Possible Causes:**
```
🔍 Python syntax errors in tool implementation
🔍 Missing required parameters
🔍 Incorrect tool structure
🔍 Import/dependency issues
```

**Solutions:**
```
✅ Check Python syntax in tool files
✅ Verify tool structure matches required format
✅ Test tool code independently
✅ Check parameter definitions
✅ Review error messages in console
```

**Tool Structure Validation:**
```python
def valid_tool():
    return {
        "name": "Tool Name",           # Required
        "description": "Description",  # Required
        "category": "Category",        # Required
        "parameters": [...],           # Required (can be empty)
        "implementation": "..."        # Required
    }
```

---

### **5. Admin Access Issues**

#### **❌ "Admin privileges required"**

**Symptoms:**
- Cannot access Repository Admin panel
- Admin features are disabled
- "Insufficient privileges" messages

**Possible Causes:**
```
🔍 User not in admin users list
🔍 Incorrect username detection
🔍 Admin settings not configured
```

**Solutions:**
```
✅ Check VS Code settings for 'toolhub.adminUsers'
✅ Add current username to admin list
✅ Use ["*"] for development (allows all users)
✅ Verify username detection (check console logs)
```

**Admin Configuration:**
1. Open VS Code Settings (`File > Preferences > Settings`)
2. Search for "toolhub"
3. Find "Toolhub: Admin Users"
4. Add your username or use `["*"]` for testing

---

### **6. Sync Operation Issues**

#### **❌ Sync hangs or fails repeatedly**

**Symptoms:**
- Sync operation never completes
- Repeated sync failures
- Timeout errors

**Possible Causes:**
```
🔍 Large repository with many files
🔍 Network timeout issues
🔍 GitHub API rate limiting
🔍 Repository access permissions
```

**Solutions:**
```
✅ Wait for rate limit reset (usually 1 hour)
✅ Check repository size and complexity
✅ Verify stable network connection
✅ Try syncing smaller repository first
✅ Check GitHub API status
```

---

### **7. Parameter Form Issues**

#### **❌ Tool parameters don't render correctly**

**Symptoms:**
- Missing form fields
- Incorrect input types
- Default values not working

**Possible Causes:**
```
🔍 Invalid parameter definitions
🔍 Unsupported parameter types
🔍 Missing required parameter properties
```

**Solutions:**
```
✅ Verify parameter structure
✅ Use supported parameter types
✅ Include required properties (name, type, description)
✅ Test with minimal parameter set
```

**Supported Parameter Types:**
```python
{
    "name": "param_name",
    "type": "text|textarea|number|select|multiselect|checkbox",
    "description": "Parameter description",
    "required": True|False,
    "default": "default_value",
    # Additional type-specific properties
}
```

## 🛠️ Debug Tools and Techniques

### **VS Code Developer Console**

1. Open: `Help > Toggle Developer Tools`
2. Go to **Console** tab
3. Look for ToolHub messages:
   ```
   🚀 ToolHub: [INFO] messages
   🔧 ToolHub: [DEBUG] messages  
   ❌ ToolHub: [ERROR] messages
   ```

### **Network Debugging**

1. Open Developer Tools
2. Go to **Network** tab
3. Filter by "github.com"
4. Check for failed API calls
5. Examine response codes and messages

### **Extension Host Console**

1. Open Command Palette (`Ctrl+Shift+P`)
2. Run "Developer: Reload Window"
3. Check for TypeScript compilation errors
4. Look for extension loading issues

## 📊 Diagnostic Commands

### **Test GitHub Token Manually**
```bash
# Test token with curl
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user

# Expected response: Your GitHub user information
```

### **Verify Repository Access**
```bash
# Test repository access
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/repos/username/repository

# Expected response: Repository information
```

### **Check File Structure**
```bash
# List repository contents
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/repos/username/repository/contents

# Check tools directory
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/repos/username/repository/contents/python_tools
```

## 🔄 Step-by-Step Debugging Process

### **When Nothing Works:**

1. **Start Fresh:**
   ```
   ✅ Reload VS Code window
   ✅ Clear ToolHub configuration
   ✅ Generate new GitHub token
   ✅ Test with sample repository
   ```

2. **Isolate the Issue:**
   ```
   ✅ Test with public repository first
   ✅ Use minimal tool set
   ✅ Check each step individually
   ✅ Compare with working example
   ```

3. **Gather Information:**
   ```
   ✅ Screenshot error messages
   ✅ Copy console logs
   ✅ Note exact steps taken
   ✅ Document environment details
   ```

### **When Partial Functionality Works:**

1. **Identify Working Parts:**
   ```
   ✅ Which operations succeed?
   ✅ Which tools work vs. fail?
   ✅ What parameters cause issues?
   ```

2. **Compare Differences:**
   ```
   ✅ Working vs. failing tools
   ✅ Successful vs. failed operations
   ✅ Different parameter types
   ```

3. **Incremental Testing:**
   ```
   ✅ Add complexity gradually
   ✅ Test one change at a time
   ✅ Verify each step works
   ```

## 📞 Getting Help

### **Information to Gather Before Seeking Help:**

1. **Environment Details:**
   - VS Code version
   - ToolHub extension version
   - Operating system
   - Node.js version (if relevant)

2. **Error Information:**
   - Exact error messages
   - Console logs
   - Network errors
   - Steps to reproduce

3. **Configuration:**
   - Repository URL (can be anonymized)
   - Tools directory structure
   - Admin settings
   - Token permissions

### **Self-Help Resources:**

1. **VS Code Extension Logs:**
   - Check Output panel
   - Select "ToolHub" from dropdown
   - Look for detailed error messages

2. **GitHub Documentation:**
   - [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
   - [Repository API](https://docs.github.com/en/rest/repos)
   - [API Rate Limiting](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)

## ✅ Prevention Tips

### **Best Practices:**

1. **Token Management:**
   - Use tokens with minimal required permissions
   - Regenerate tokens periodically
   - Never commit tokens to repositories

2. **Repository Structure:**
   - Keep tools directory organized
   - Use consistent file naming
   - Include proper documentation

3. **Testing Strategy:**
   - Test with public repositories first
   - Start with simple tools
   - Verify each component individually

4. **Error Handling:**
   - Check logs regularly
   - Test error scenarios
   - Have rollback plans

---

**🎯 Remember:** Most issues are configuration-related and can be resolved by carefully checking the setup steps and verifying each component works independently.

If you're still experiencing issues after following this guide, gather the diagnostic information listed above and consult the ToolHub documentation or support channels.