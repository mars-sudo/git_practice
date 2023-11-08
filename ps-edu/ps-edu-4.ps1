# Let's grab all the computer in AD, but for tesing just use _____

Get-ADComputer
Get-ADComputer L7100

# Filter is a mandatory parameter, we must use a * to find all computers
Get-AdComputer -Filter *

# Not all properties are shown by default. This is common amongst all AD Module commands
Get-ADComputer -Filter * -Propteries * | Select-Object -First 1

# Les's grab all the user accounts in AD
Get-ADUsers

Get-ADUser -Filter *
Get-ADUser -Filter {Name -eq "Ruby Teusday"}
Get-ADUser -Filter {Name -eq "Ruby Teusday"} -Properties PasswordExpired

Get-ADUser | Get-MemberGet-Help Get-ADUser -Full

Get-AdUser -Filter {UserPrincipalName -eq "rteusday@sample.org"}

Get-ADUser -Filter * -Properties *

Get-ADUser -Filter 'Name -like "*Teusday"' | FT Name,SamAccountName,ObjectClass -A

# Start Example
$demoPath = "C:\Users\~"

# Le's find usernames for a list of FirstName/LastName employees in a csv
# This is a CSV file, but this can be a SQL DB, an Oracle DB, Excel, or any data source
$csvusers = Import-Csv -Path "$demoPath\users.csv"
$csvusers

$allAdUsers = Get-ADuser -Filter *
($allADusers).Count

foreach ($u in $allADusers) {
    $u
}

$i=0
foreach ($csvuser in $csvusers){
    if ($allAdUsers | Where-Object {$_.givenName -eq $csv.User.FirstName -and $_.surName -eq $csvUser.LastName}){
        $i++
    }
    $csvuser.FirstName
}

Get-AdGroup -Filter *

Get-AdGroupMember -Filter *

# Let's build "custom" output to show each group along with each member in that group
$domainAdmins = Get-ADGroupMember -Identity 'Domain Admins'
$domainAdmins | Select Name

# This might work without a lot of hassle
$groups = Get-AdGroup -Filter * -Properties Members | Select-Object Name,Members
$groups | Where {$_.Name -eq 'domain admins'}
$groups | Where {$_.Name -eq 'domain admins'} | Select -ExpandProperty Members

# Let's limit groups to only users

## Not possible with $groups as-is
Get-AdGroupMember -Identity 'Domain Admins' | Select name,ObjectClass
Get-AdGroupMember -Identity 'Domain Admins' | Where {$_.ObjectClass -eq 'user'}

# Have to redesign this, this sorta works but hard to read
$groups = Get-AdGroup -Filter *
foreach($group in $groups){
    $group.Name
    Get-ADGroupMember -Identity $group | where {$_.ObjectClass -eq 'user'} | Select-Object -Property Name
}


# Let's use custom object to make this better looking and more easily parseable. better --not perfect
foreach ($group in $groups){
    $output = @{}
    $output.GroupName = $group.Name  
    $groupMembers = Get-ADGroupMember -Idenitty $group | where {$_.ObjectClass -eq 'User'} | Select-Object -ExcludeProperty Name
    $output.Members = $groupMembers
    [pscustomobject]$output
}

# More tweeks
foreach ($group in $groups){
    # Create a hashtable to store proterites in temporarily for each $group
    $output = @{}
    # Begin assigning keys to hashtable
    $output.GroupName = $group.Name
    # Capture all the group members
    $groupMembers = Get-AdGroupMember -Identity $group | Where {$_.ObjectClass -eq 'User'} | Select-Object -Property Name
    # Only output a custom object if there were members in that group
    if ($groupMembers){
        $output.Members = $groupMembers
        [pscustomobject]$output
    }
}

# Best Output
# This is the foreach method, when you declare a variable with a $_.foreach([])
$groups.foreach({
    # Create a hashtable to store properties in temporarily for each $group
    $output = @{}
    # Begin assigning keys to the hashtable
    $output.GroupName = $_.Name
    # Captre all of the group members
    $groupMembers = Get-ADGroupMember -Identity $_ | Where {$_.ObjectClass -eq 'User'} | Select-Object -Property Name
    # Only output a custom object if there were members in that group
    if($groupMembers){
        $output.Members = $groupMembers
        [pscustomobject]$output
    }
}) | Format-Table -Autosize
