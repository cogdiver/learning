function hello { "Hello there $args, how are you?" }
hello # Hello there , how are you?
hello Bob # Hello there Bob, how are you?
hello Bob Alice Ted Carol # Hello there Bob Alice Ted Carol, how are you?

function hello {
    $ofs=","
    "Hello there $args and how are you?"
}
hello Bob Carol Ted Alice # Hello there Bob,Carol,Ted,Alice and how are you?

function count-args {
    "`$args.count=" + $args.count
    "`$args[0].count=" + $args[0].count
}
count-args 1 2 3 # 3,1
Count-Args 1,2,3 # 1,3
count-args 1,2,3 4,5,6,7 # 2,3

function subtract ($from, $count) { $from - $count }
subtract 5 3 # 2
subtract -from 5 -count 2 # 3
subtract -count 2 -from 5 # 3
subtract -from 5 6 # -1
subtract -count 5 6 # 1

function nadd ([int] $x, [int] $y) {$x + $y}
nadd 1 2 # 3
nadd '1' '2' # '3'
# nadd 'a' 'b' # Error

function a ($x, $y) {
    "x is $x"
    "y is $y"
    "args is $args"
}
a 1 2 3 4
<#
x is 1
y is 2
args is 3 4
#>

function add ($x=1, $y=2) { $x + $y }
add # 3

function dow ([datetime] $d = $(Get-Date)) { $d.dayofweek }
dow # Sunday
dow 'jan 16, 1999' # Saturday

function get-soup ([switch] $please, [string] $soup= 'chicken noodle') {
    if ($please) { "Here's your $soup soup" }
    else { 'No soup for you!' }
}
get-soup # No soup for you!
get-soup tomato # No soup for you!
get-soup -please # Here's your chicken noodle soup
get-soup -please tomato # Here's your tomato soup
get-soup tomato -please # Here's your tomato soup
get-soup -soup tomato -please # Here's your tomato soup

function foo ([switch] $s) { "s is $s" }
function bar ([switch] $x) { "x is $x"; foo -s: $x }
foo # s is False
foo -s # s is True
bar # x is False; s is False
bar -x # # x is True; s is True

function numbers { 2+2; 9/3; [math]::sqrt(27) }
numbers # 4 3 5.19615242270663
$result = numbers
$result.Length # 3

function numbers {
    $i=1
    while ($i -le 10) {
        $i
        $i++
    }
}
$result = numbers
$result.GetType().FullName # System.Object[]
$result.Length # 10

function sum {
    $total=0;
    foreach ($n in $input) { $total += $n }
    $total
}
sum 1 2 3 # 0
1,2,3 | sum # 6

function my-cmdlet ($x) {
    <#
    Comentario de la funcion
    #>
    begin { $c=0; "In Begin, c is $c, x is $x" }
    process { $c++; "In Process, c is $c, x is $x, `$_ is $_" }
    end { "In End, c is $c, x is $x" }
}
10,20,30 | my-cmdlet 22
<#
In Begin, c is 0, x is 22
In Process, c is 1, x is 22, $_ is 10
In Process, c is 2, x is 22, $_ is 20
In Process, c is 3, x is 22, $_ is 30
In End, c is 3, x is 22
#>
my-cmdlet 22
<#
In Begin, c is 0, x is 22
In Process, c is 1, x is 22, $_ is
In End, c is 1, x is 22
#>

function my-cmdlet ($x) { "In Process, x is $x, `$_ is $_, input is $input" }
10,20,30 | my-cmdlet 22 # In Process, x is 22, $_ is

filter my-cmdlet ($x) { "In Process, x is $x, `$_ is $_, input is $input" }
10,20,30 | my-cmdlet 22
<#
In Process, x is 22, $_ is 10, input is 10
In Process, x is 22, $_ is 20, input is 20
In Process, x is 22, $_ is 30, input is 30
#>

Get-ChildItem -Path function:\mkdir
(Get-ChildItem function:\).count # n
function clippy { "I see you're writing a function." }
(Get-ChildItem function:\).count # n+1
Get-ChildItem function:\clippy
Get-ChildItem function:\clippy |
Format-Table CommandType, Name, Definition -AutoSize -Wrap
Remove-Item function:/clippy
(Get-ChildItem function:\).count # n

function one { "x is $x" }
function two { $x = 22; one }
$x=7
one # x is 7
two # x is 22
one # x is 7

function one { "x is $global:x" }
one # x is 7
two # x is 7
one # x is 7
