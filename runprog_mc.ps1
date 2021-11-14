$Orders = @('RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD')

foreach ($o in $Orders) {
    Start-Process powershell.exe -ArgumentList "./runprog.ps1 bfs $o"
}   

foreach ($o in $Orders) {
    Start-Process powershell.exe -ArgumentList "./runprog.ps1 dfs $o"
}

Start-Process powershell.exe -ArgumentList "./runprog.ps1 astr hamm"
Start-Process powershell.exe -ArgumentList "./runprog.ps1 astr manh"