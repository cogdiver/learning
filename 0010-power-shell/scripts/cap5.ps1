
1..5 | foreach {$_ * 2}
1..5 | % {$_ * 2}
1..5 | % {$t=0} {$t += $_ * 2} {$t}
1..5 | foreach -Begin {$t=0} -Process {$t += $_ * 2} -End {$t}

$a = 1,(2,3)

$b = $a | foreach { $_ }
$b.Length # 3

$b = $a | foreach { , $_ }
$b.Length # 2

$b = $a | foreach { $_ * 2 }
$b.Length # 5

$b = $a | foreach { $_ * 2 } | foreach { $_ * 2 }
$b.Length # 5

$words= "a,b,c,d,e,a,b,c,a,b,c,a,d" -split ","
$words | ForEach-Object {$h=@{}} {$h[$_] += 1} # empty
$words | ForEach-Object {$h=@{}} {$h[$_] += 1} { $h } # object
$words | foreach -begin {$sum=0} {$sum++} {$sum++} -end {$sum}

'test', 'strings' | foreach {$_.ToUpper()}
'test', 'strings' | foreach ToUpper
'test', 'strings' | foreach Replace -ArgumentList 'st', 'AB'

1..10 | where {-not ($_ -band 1)} # 1..10|?{!($_-band 1)}
$result = for ($i=1; $i -le 10; $i++) {$i}
"$result" # 1 2 3 4 5 6 7 8 9 10