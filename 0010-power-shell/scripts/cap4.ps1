$count1 = 0
$count2 = 0
foreach($i in 1..10) {
    "$((++$count1)): $(($count2++))"
}

$('bbb','aaa','ccc' | sort )[0] # 'aaa'
$('bbb','aaa' | sort )[0] # 'aaa'
$('aaa' | sort )[0] # 'a'

@('bbb','aaa','ccc' | sort )[0] # 'aaa'
@('bbb','aaa' | sort )[0] # 'aaa'
@('aaa' | sort )[0] # 'aaa'

1,2,1+2 # 1,2,1,2

$a = (((1,2),(3,4)),((5,6),(7,8)))
$a[1][0] # 5,6
1..3+4..6
('*' * 5) . ('len' + 'gth')

using assembly System.Windows.Forms
using namespace System.Windows.Forms
$form = [Form] @{
    Text = 'My First Form'
}
$button = [Button] @{
    Text = 'Push Me!'
    Dock = 'Fill'
}
$button.add_Click{
    $form.Close()
}
$form.Controls.Add($button)
$form.ShowDialog()

'|{0,10}| 0x{1:x}|{2,-10}|' -f 10,20,30

echo "Book is red" > old.txt
${c:old.txt} -replace 'is (red|blue)','was $1' > new.txt
${c:old.txt} = ${c:old.txt} -replace 'is (red|blue)','was $1'
${c:old.txt}.Length

Import-Csv .\variables.csv | foreach {Set-Variable -Name $_.Name -Value $_.Value}
Get-Variable -ValueOnly srcHost

Set-Variable -Option ReadOnly -Name srcHost -Value machine1
Set-Variable -Option Constant -Name srcHost -Value machine1

Remove-Variable srcHost
Remove-Variable -Force srcHost
$ref = Get-Variable -Name destHost

function s {param ($x, $y, $z) "x=$x, y=$y, z=$z" }
$list = 1,2,3
s $list
s @list

function s {param ($x, $y, $z) "$x,$y,$z args=$args" }
$list += 5,6,7
s @list
s -y first -x second