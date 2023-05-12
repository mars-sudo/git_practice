# $rg = 'arm-introdution-01'
# New-AzResourceGroup -Name $rg -Location WestUS3  


New-AzResourceGroupDeployment {
    -Name 'demo-storage' 
    -ReourceGroupName arm-introdution-01 
    -TemplateFile 'demo-storage.json' 
}