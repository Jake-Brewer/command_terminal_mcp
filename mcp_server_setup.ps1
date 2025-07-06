# Deployment script for MCP Server on Windows
# Make sure to run this PowerShell script as Administrator (elevated).

# 1. Verify Python is installed and create a virtual environment
Try {
    # Check for Python 3 availability
    $py = Get-Command python -ErrorAction Stop
}
Catch {
    Write-Error "Python3 is not installed or not in PATH. Install Python 3.x and retry." 
    exit 1
}
# Create the virtual environment in current directory
& python -m venv .venv
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to create Python virtual environment." 
    exit 1
}

# 2. Install Python dependencies from requirements.txt
$reqFile = Join-Path (Get-Location) "requirements.txt"
if (-not (Test-Path $reqFile)) {
    Write-Error "requirements.txt not found in $((Get-Location).Path)." 
    exit 1
}
# Use the venv's pip to install requirements
$venvPip = Join-Path (Get-Location) ".venv/Scripts/pip.exe"
& $venvPip install -r $reqFile
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to install dependencies from requirements.txt."
    exit 1
}

# 3. Copy or create configuration file for the MCP server
$workDir = Convert-Path .
$configFile = Join-Path $workDir "config.json"
if (Test-Path (Join-Path $workDir "config.example.json")) {
    Copy-Item (Join-Path $workDir "config.example.json") $configFile -Force -ErrorAction Stop
}
else {
    # Create a default config.json if no example is present
    $defaultConfig = '{ "setting1": "value1", "setting2": "value2" }'
    $defaultConfig | Out-File -FilePath $configFile -Encoding UTF8 -Force
}
Write-Host "Configuration file is set at $configFile"

# 4. Register the MCP server as a Windows service (runs in background at startup)
# Ensure the script is running with Administrator rights
$adminCheck = [Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()
if (-not $adminCheck.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "This script must be run as Administrator to register a Windows service."
    exit 1
}

$ServiceName = "MCPServer"
# If a service with this name exists, remove it to avoid conflict
if (Get-Service -Name $ServiceName -ErrorAction SilentlyContinue) {
    Write-Warning "Service '$ServiceName' already exists. It will be recreated."
    Try {
        Stop-Service -Name $ServiceName -Force -ErrorAction Stop
    }
    Catch {}
    Try {
        Remove-Service -Name $ServiceName -ErrorAction Stop  # PowerShell 7 has Remove-Service
    }
    Catch {
        # Fallback to sc.exe for removing service if Remove-Service not available
        sc.exe delete $ServiceName | Out-Null
    }
}

# Define the service execution command (Python interpreter and server script with full paths)
$pythonExe = Join-Path $workDir ".venv/Scripts/python.exe"
$serverScript = Join-Path $workDir "server.py"
$binPath = '"' + $pythonExe + '" "' + $serverScript + '"'

# Create the new Windows service for the MCP server
Try {
    New-Service -Name $ServiceName -BinaryPathName $binPath -DisplayName "MCP Server" -Description "MCP Server as Windows Service" -StartupType Automatic -ErrorAction Stop
    Write-Host "Windows Service '$ServiceName' created (to run MCP server on startup)."
}
Catch {
    Write-Error "Failed to create Windows service: $($_.Exception.Message)"
    exit 1
}

# Start the service immediately
Try {
    Start-Service -Name $ServiceName -ErrorAction Stop
    Write-Host "MCP Server service '$ServiceName' started."
}
Catch {
    Write-Warning "Service installed but could not be started automatically. Start it manually via 'Start-Service $ServiceName' or Services console."
}
