2 + '3.0' + '4' # 9
2 + '3.0' + '4' # 9
'2' + '3.0' + 4 # 23.04

(2 + '3.0' + '4').GetType().FullName # System.Double
2 + '3.0' + '4' | Get-Member

[System.AppDomain]::CurrentDomain
[System.AppDomain]::CurrentDomain.GetAssemblies()

"Embed double quote like this "" or this `" "
'Embed single quote like this '' '

$foo = "FOO"
"This is a string in double quotes: $foo"
'This is a string in single quotes: $foo'

"Expanding three statements in a string: $(1; 2; 3)"

$a = @"
One is "1"
Two is '2'
Three is $(2+1)
The date is "$(Get-Date)"
"@

$user = @{
    FirstName = 'John'
    LastName = 'Smith'
    PhoneNumber = '555-1212'
}
$user.FirstName
$user.firstname
$user['firstname']
$user['firstname','lastname']

$h = [ordered]@{
    a=1
    b=2
    c=3
}
foreach ($pair in $h.GetEnumerator()) {
    $pair.key + " is " + $pair.value
}


$a = 1,2,3
$a.GetType().FullName
# System.Object[]

$i = [int] '123'

$s = 'one','two','three'
[string]::Join(' + ', $s)