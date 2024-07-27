'abc' * 3
'abc' * 0

$a=1,2,3
$a.Length # 3
$a = $a * 2
$a.Length # 6
$a.ForEach({$_ * 10})

'123' / '4' # 30.75


# Assignment operators
# = += -= *= /= %=

$a,$b,$c = 1,2,3,4
$a,$b = $b,$a

$false,$true -contains $false

$names = 'powershell', 'powershell_ise'
Get-Process | where Name -in $names

'abcdef' -match '(?<o1>a)(?<o2>((?<e3>b)(?<e4>c))de)f'
$matches

(net config workstation)[1]
$p='^Full Computer.* (?<computer>[^.]+)\.?(?<domain>[^.]*)'
(net config workstation)[1] -match $p

'1,2,3,4' -replace '\s*,\s*','+'

$in = 1,2,3
$out = -join $in
$out = $in -join '+'

Invoke-Expression (1..10 -join '*')

'a:b:c:d:e' -split ':'
'a:b:c:d:e' -split ':',3
'a*b*c' -split '*'
'a*b*c' -split '*',0,'SimpleMatch'

$colors = "Black,Brown,Red,Orange,Yellow,Green,Blue,Violet,Gray,White"
$count=@(0)
$colors -split {$_ -eq ',' -and ++$count[0] % 2 -eq 0 }