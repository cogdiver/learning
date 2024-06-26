# Query Sintax
# https://learn.microsoft.com/en-us/cli/azure/query-azure-cli?tabs=concepts%2Cbash

# List Storage blobs
az storage account list \
    --query "[].{Name:name, Location:location}" \
    --output table
az storage account list \
    --query "[?name == 'storagepropedeutico'].{Name:name, Location:location}" \
    --output json

# Create Storage
az storage account create \
    --name BlobStorageTest \
    --resource-group VinkOSDatabricks \
    # --location ubicacion \
    # --sku Standard_LRS
