# Example ForEach-Object and if statement script
Get-Content -Path C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt | ForEach-Object {
    Test-Connection -Computername $_ -Quiet -Count 1 
        }


Get-Content -Path C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt | ForEach-Object { 
  Test-Connection -Computername $PS_Item -Quiet -Count 1
  }


  Get-Content -Path C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt | ForEach-Object {
    if (Test-Connection -Computername $_ -Quiet -Count 1)
    {Write-Output "Hello PC"} 
        }


Get-Content -Path C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt | ForEach-Object { 
    if 
    ((Test-Connection -Computername $PS_Item -Quiet -Count 1) -eq $true){
      'the machine is online'
        } 
    }

    Get-Content -Path C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt | ForEach-Object {
    if (Test-Connection -Computername $_ -Quiet -Count 1)
    {$spotify = Get-Process spotify*
    $spotify}
    }

    # Example ForEach-Object and if statement script
Get-Content -Path C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt | ForEach-Object {
  Test-Connection -Computername $_ -Quiet -Count 1 
      }

Get-Content -Path C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt | ForEach-Object { 
Test-Connection -Computername $PS_Item -Quiet -Count 1
}


Get-Content -Path C:\Users\Mars\Mars-Scripts\ps-edu\pcnames.txt | ForEach-Object { 
  if 
  ((Test-Connection -Computername $PS_Item -Quiet -Count 1) -eq $true){
    'the machine is online'
      } 
  }