param (
    [int]$threads = 10,
    [int]$loops = 1
)

$JMETER_BIN = "C:\Users\final\Downloads\apache-jmeter-5.6.3\apache-jmeter-5.6.3\bin\jmeter.bat"
$JMX_FILE = "ACIT3855.jmx"

# Clean old artifacts to avoid JMeter directory-not-empty errors
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue results.jtl, report

Write-Host "Running headless JMeter: $threads threads, $loops loop(s)..." -ForegroundColor Cyan

& $JMETER_BIN -n -t $JMX_FILE "-Jthreads=$threads" "-Jloops=$loops" -l results.jtl -e -o report

Write-Host "Done! Report generated in .\report\index.html" -ForegroundColor Green