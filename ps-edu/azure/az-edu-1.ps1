# Manage Azure Identities and Governance
# Install Azure Module
Install-Module -Name AzureAD
Connect-Azure-AD

$PasswordProfile = New-Object -TypeName
Microsoft.Open.AzureAD.Model.$PasswordProfile
$PasswordProfile.Password = "P@ssw0rd8!"
$PasswordProfile.EnforceChangePasswordPolicy = $true

New-AzureADUser -DisplayName "Pat Smith" -PasswordProfile $PasswordProfile ` -UserPrincipalName "name@domain.com" -AccountEnabled $true

# Azure CLI
# az ad user create --display-name "Adee Lester" \ 
# --password "P@$$w0rd13!" --user-principal-name "adee@domain.com" \
#  --force-change-password-next-login --output table

# Create Azure AD Group
New-AzureADGroup -Description "Marketing" -DisplayName "Marketing" -MailEnabled $false -SecurityEnabled $true -MailNickName "Marketing"

Add-AzureADGroupMember -ObjectId "73909-erwer" -RefObjectId "alkjaldskfj-asdfs"

# az ad group create --display-name Sales --mail-nickname Sales
# az ad group member check --group Sales --member-id xxxxxxxxxx-xxxxx
# az ad group member add --group Sales --member-id xxxxxxxxxx-xxxxxx

# Bulk Update User Properties by Group
Import-Module AzureAD
Connect-Azure-AD

$adGroupId = "<Azure AD Group ID here>"
$users = Get-AzureADGroupMember -ObjectID $adGroupId
foreach($u in $users)
{
    Write-Host $u.DisplayName
    Set-AzureADUser -ObjectId $u.Mail -Department "<New Vale>"
}

# Powershell get role assignments
Get-AzRoleAssignment
Get-AzDenyAssignment

# Azure CLI get role assignments
az role assignment list

# Createing Custom Roles using Powershell 
(Get-AzRoleDefinition "virtual machine contributor").actions

$role = Get-AzRoleDefinition "Virtual Machine Contributor"

$role.Id = $null

$role.Name = "VM Reader"

$role.Description = "Can see VMs"

$role.Actions.Clear()

$role.Actions.Add("Microsoft.Storage/*/read")

$role.Actions.Add("Microsoft.Network/*/read")

$role.Actions.Add("Microsoft.Computer/*/read")

$role.AssignableScopes.clear()

$role.AssignableScopes.Add("/subscriptions/0000-111-222-aaa-123445677")

NewAzRoleDefiniton -Role $role

(Get-AzRoleDefinition "VM Reader").actions


# Applying Resource Tags
# https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json

# Get tagged resources
Get-AzTag -Detailed

# Get resources by tag name 
(Get-AzResource -TagName department).name

# Get resource by tag value
(Get-AzResource -TagValue ux).name

# Add an existing tag and non-existing tag to a resource with a tag already

$tags =@{'project' = 'ux'; 'location' = 'Dublin'}
$rg = Get-AzResourceGroup -Name 'demo-rg'
$rg.ResourceId
New-AzTag -ResourceId $rg.resouceid -Tag $tags

# Add tags to resource within a resource group
Get-AzResource -ResourceGroupName 'demo-rg' | Set-AzResource -Tag @{'environment' = 'staging'}

# Update exisiting tags on resources, operations (merge, replace, delete)
$tags = @{"environment" = "staging"}

# Azure Policy Creation - Powershell
# Get a reference to the resource group that is the scope of the assignemtn
$rg = Get-AzResourceGroup -Name '<resourceGroupName>'

# Get a reference to the built-in policy definition to assign
$definition = Get-AzPolicyDefinition | Wehre-Object { $_.Properties.DisplayName -eq 'Audit VMs that do not use managed disks'}

# Create the policy assignment with the built-in definition against your resource group
New-AzPolicyAssignment -Name 'audit-vm-manageddisks' -DisplayName 'Audit VMs without managed disks Assignemnt' -Scope $rg.ResourceId -PolicyDefiniton $definition

# Resource Locks
New-AzResourceLock -Locklevel CanNotDelet -LockName LockSite -ResourceName examplesite

az lock create --name LockGroup --lock-type CanNotDelet --resource-group exampleresorucegroup

# Creating and Managing Resource Groups
New-AzResourceGroup -name example-rg -location eastus2

az group create --name example-rg --location eastus2