# A Hashtable is also known as a dictonary, so it has key-value pairs
# Syntax of a hashtable is as follows - @{ <name> = [<value>] ...}
# $hash_var = @{}

# A PSCustomOBject is a usable Objects

# Objects have propertie and methods.
# Object = car
# Properties = color, size, transmission.
# Methods = drive forward, driver reverse. 

$myObject = [PSCustomObject]@{
    Name = 'Mars'
    Language ='PowerShell'
    State = 'Florida'
    }

$myObject | Get-Member
$myObject.Name

$myObject | ConvertTo-Json -Depth 1 | Set-Content -Path $Path
$myObject = Get-Content -Path $Path | ConvertFrom-Json

$myObject | Export-Csv -Path 'C:\Users\Public'


################################

$myHashTable = @{
    Name = 'Rob'
    Language = 'Go'
    State = 'Maryland'

}

$customObject = [pscustomobject]$myHashTable
$customObject | Get-Member



###################################

$string = Write-Output 'Hello World'
# Using Get-Memeber we can see all the properties and methods associated with this object
$string | Get-Member # This will show you the 'Type' of object
$string.Length
