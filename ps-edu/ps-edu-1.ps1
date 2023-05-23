# Object and the Pipeline.
# Objects have propertie and methods.
# Object = car
# Properties = color, size, transmission.
# Methods = drive forward, driver reverse. 

# Let's create a variable
# Here, $string is a variable that we've created to be an object
$string = Write-Output 'Hello World'
$string

# Using Get-Memeber we can see all the properties and methods associated with this object
$string | Get-Member # This will show you the 'Type' of object

# To reference any of the Get-Member Properties, use dot notation
$string.Length

# To reference any of the Get-Memeber Methods, use dot notation with parenthees
$string.ToUpper() # Empty parentheses means that thte method has no arguments
$string.ToLower()
$string.Replace('Hello','Goodbye')

# Building a powershell Hast Table - a group of key value pairs
$hashtable = @{Color = 'Red';Transmission ='Automatic'; Convertable =$false}

$hashtable | Get-Member # Here we will see the 'Type' of object is a System.Collections.Hashtable

[pscustomobject]$hashtable # This creates custom properties for the object. 

$car = [PSCustomObejct]$hashtable
$car | Get-Memeber # Here we will see the 'TypeName' of this object is now a PSCustomObject with the 3 properties created in the Hash Table


Get-Content -Path 'C:\Users\~' | ForEach-Object {[pscustomobject]@{ComputerName =$PSItem}} | Test-Connection
