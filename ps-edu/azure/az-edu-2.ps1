# Implement and Manage Azure Storage, Deploy and Manage Azure Compute Resources.



# WAImportExportTool
.\WAImportExport.exe PrepImport
/j:<Journalfile>
/id:<SessionId>
#[/logdir:,LogDirectory>]
#[/sk:<StorageAccountKey>] [/silentmode]
#[/InitialDriveSet:<driveset.csv>]
/DataSet:<dataset.csv>

# CLI tool run on 64-bit Windows Only!
# Encyption, decryption and data copy. 
# Determine number of drives needed for export job

# AzCopy Syntax
azcopy [command] [arguments] --[flag-name]=[flag-value]

# Move an Azure VM using PowerShell
#Move-AzResource -DestinationResourceGroupName 'ps-course-rg' -ResourceId <myResourceId,myResourceId,myResourceId>

#Move-AzResource -DestinationSubscriptionId "4kshdie-blah-blah-blah" -DestinationResourceGroupName 'ps-course-rg' -ResourceId <myResourceId,myResourceId,myResourceId>

# Redeploy Virtual Machines
Set-AzVM -Redeploy -ResourceGroupName 'ps-course-rg' -Name "linux-1"

az vm redeploy --resource-Group ps-course-rg --name linux-1

# Creating an Azure Container Instance
# Create a resource group
az group create --name ps-course-rg --location centralus

# Create and deploy container
az container create --resource-group  ps-course-rg --name mycontainer --image mcr.microsoft.com/azuredocs/aci-helloworld --dns-name-label az104-demo --ports 80 --restart-policy Always

# Create a Azure Kubernetes Service (AKS) Single Node Cluster
az aks create --resource-group ps-course-rg --name PSAKSCluster --vm-set-type VirtualMachineScaleSets --node-count 2 --generate-ssh-keys --load-balancer-sku standard

# Create App Service using Azure CLI
# Create resource group
az group create --name ps-app-rg --location centralus

# Create app service plan
az appservice paln create --name psasp --resource-group ps-app-rg --sku F1 --is-linux

# Create web app
az webapp create --name dotnetapp --resource-group ps-app-rg --plan psasp

# Creating a VM using Powershell
New-AzResourceGroup -Name 'ps-course-rg' -Location 'CentralUS'
New-AzVm -ResourceGroupName 'ps-course-rg' -Name 'windows-1' - Location 'CentralUS' -VirtualNetworkName 'main-vnet' -SubnetName 'backend' -SecurityGroupName 'myNetworkSecurityGroup' -PublicIpAddressName 'myPublicIpAddress' -OpenPorts 80,3389

az group create --name ps-course-rg --location centralus
az vm create --resource-Group ps-course-rg --name windows-1 --image win2016datacenter --admin-username azureuser

