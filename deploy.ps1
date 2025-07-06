# deploy.ps1
param(
    [string]$Root = (Split-Path -Parent $MyInvocation.MyCommand.Path),
    [string]$Service