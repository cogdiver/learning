# ls
Get-ChildItem -Path .. > .\foo.txt

# cat
Get-Content -Path .\foo.txt

# help
Get-Help ls

# variables
$n = (2+2)*3
$n

$files = Get-ChildItem
$files[0]

# sort
Get-ChildItem | Sort-Object -Property length -Descending
Get-ChildItem | Sort-Object -Property length -Descending | Select-Object -First 1
Get-ChildItem | Sort-Object -Property length -Descending | Select-Object -First 1 -Property Directory

# for
$total = 0
Get-ChildItem | ForEach-Object {$total += $_.length }
$total

# procesos
Get-Process | sort -Descending ws | select -First 3

# while
$i=0
while ($i++ -lt 10) { if ($i % 2) {"$i is odd"}}
foreach ($i in 1..10) { if ($i % 2) {"$i is odd"}}
1..10 | ForEach-Object { if ($_ % 2) {"$_ is odd"}}

# echo
Write-Output "Hello
there
how are
you?"

# comments
echo hi#there
echo hi #there
(echo hi)#there
echo hi;#there
echo hi+#there
function hi#there { "Hi there" }
hi#there
<#
This is a comment
that spans
multiple lines
#>
<# a comment #> "Some code"

# format
Get-ChildItem .. | Format-Table name
Get-Command Format-* | Format-Table name
Get-Process *ss | Out-GridView
