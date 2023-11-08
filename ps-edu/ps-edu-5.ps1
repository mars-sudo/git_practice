# Collection Filtering
# There are two methods of collection filtering
# The Where-Object Command and the .Where()method

$array = 0..10
$array

# As long as the where filter returns $true or some output other than $false
$array | Where-Object -FilterScript {$_}
$array | Where-Object -FilterScript {$true}
$array | Where-Object -FilterScript {$false}
$array | Where-Object -FilterScript {$null}
$array | Where-Object -FilterScript {$_ -gt 2}
$array | Where-Object {$_ -gt 2}

# This is the where method, so we are declaring the variable array with .Where({}). This will be faster and better for performance
$array.where({$_})
$array.where({$_ -gt 2})
$array.where({$_ -in @(3,4,5,6,7,8,9,10)})
$array.where({'hello'})
$array.foreach({'hello'})

# Advanced Filtering
# Best practice to "Filter left", provider-specific, useful for large environments

# Provider-specific filtering
# File system has the C: drive --no output but no errors either.
# The ilter knows this is a file system and to filter on files
Get-ChildItem -Path 'C:\Windows' -Filter '*.doc'

# Returns everything because it doesn't know what * .doc should filter on
Get-ChildItem -Path 'AD:\DC=mylab,DC=local' -Filter '*.doc'

Get-Help about_ActiveDirecotry_Filter

# Limiting search for AD cmdlets
(Get-ADUser -filter *).Count
(Get-ADUser -Filter * -SearchBase 'OU=AutomationList,DC=mylab,DC=local').Count
(Get-AdUser -Filter * -SearchScope Base).Count
(Get-AdUser -Filter * -SearchScope Subtree).Count



