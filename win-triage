<#
.SYNOPSIS
    This script will pull various information about a system based
    on the Blue Team Field Manual (BTFM) and Blue Team Handbook.
.NOTES
    File Name     : win-triage.ps1
    Author        : Paul Soriano (pvsoriano@gmail.com)
#>

# Pull system information
function sys-info {
    Write-Host ""
    Write-Host "##### Current date as of the script running ######"
    Get-Date
    Write-Host "#######################"
    Hostname
    Write-Host "#######################"
    Systeminfo
    Write-Host "#######################"
    wmic bios get serialnumber
}
