# Powershell Functions
# Building Blocks, group command and logic together
# Three phases to functions: Input > Process > Output

$demoPath = "C:\Users\Mars\Mars-Scripts\ps-edu"

# Scripts are extremely commmon in Powershell. A script is just a text file with a ps1 extension. They can be excuted as such
powershell.ext -file $demoPath\ps-script-1.ps1

# or directly from the current Powershell console
& "$demoPath\ps-script-1.ps1"

# Scripts are little bundles of code in a file but are still a file. Where'd I put that script? What does it do again?
# We need to do the same thing only from withing Powershell itself

Function Do-Thing{
    Write-Output "I did it!"
}
# The functions must be 'loaded' into existing Powershell session, It can then be called just like a script
Do-Thing

# Use the 'Get-Verb; to find the 'approved' verbs for building functions. "Verbs before Nouns", this utilizes best practice. 

$outputOfFunction = Do-Thing
$outputOfFunction -eq "I did it!"

# Scripts with Functions
Functions Find-TextFile{
    param(
        [Parameter()]
        $Name
    )
    Get-ChildItem -Path 'C:\Users\Mars\Mars-Scripts\ps-edu' -Filter "*pcnames.txt"
}

Functions Set-TextFile{
    param(
        # Parameter help description
        [Parameter()]
        $Path,
        [Parameter()]
        $Value
    )
    Set-Content -Path $Path -Value $Value
}

$textFile = FindTextFile -Name pcnames
Set-TextFile =Path $textfile.FullName -Value 'new-name'
Get-Content -Path 'C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt'