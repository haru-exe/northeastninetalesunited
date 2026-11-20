param(
    [Parameter(Mandatory=$true)][string]$PdfPath,
    [Parameter(Mandatory=$true)][string]$OutDir,
    [int]$Height = 2400,
    [int]$FirstPage = 1,
    [int]$LastPage = 0
)
# Renders pages of a PDF to PNG using the Windows built-in renderer (Windows.Data.Pdf).
Add-Type -AssemblyName System.Runtime.WindowsRuntime
[void][Windows.Storage.StorageFile,Windows.Storage,ContentType=WindowsRuntime]
[void][Windows.Data.Pdf.PdfDocument,Windows.Data.Pdf,ContentType=WindowsRuntime]
[void][Windows.Storage.Streams.InMemoryRandomAccessStream,Windows.Storage.Streams,ContentType=WindowsRuntime]

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
$asTaskAction = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and -not $_.IsGenericMethod -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncAction' })[0]

function Await-Op($op, $resultType) {
    $task = $asTaskGeneric.MakeGenericMethod($resultType).Invoke($null, @($op))
    [void]$task.Wait(-1)
    return $task.Result
}
function Await-Action($act) {
    $task = $asTaskAction.Invoke($null, @($act))
    [void]$task.Wait(-1)
}

if (-not (Test-Path -LiteralPath $OutDir)) { New-Item -ItemType Directory -Path $OutDir | Out-Null }
$file = Await-Op ([Windows.Storage.StorageFile]::GetFileFromPathAsync($PdfPath)) ([Windows.Storage.StorageFile])
$doc  = Await-Op ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])
$n = [int]$doc.PageCount
if ($LastPage -le 0 -or $LastPage -gt $n) { $LastPage = $n }
Write-Output ("PageCount = " + $n)
for ($i = $FirstPage; $i -le $LastPage; $i++) {
    $page = $doc.GetPage($i - 1)
    $opts = New-Object Windows.Data.Pdf.PdfPageRenderOptions
    $opts.DestinationHeight = [uint32]$Height
    $stream = New-Object Windows.Storage.Streams.InMemoryRandomAccessStream
    Await-Action ($page.RenderToStreamAsync($stream, $opts))
    $inStream = [System.IO.WindowsRuntimeStreamExtensions]::AsStreamForRead($stream)
    $outPath = Join-Path $OutDir ("p{0:D2}.png" -f $i)
    $fs = [System.IO.File]::Open($outPath, [System.IO.FileMode]::Create)
    $inStream.CopyTo($fs)
    $fs.Close(); $inStream.Close(); $stream.Dispose()
    Write-Output ("page {0}: size {1} x {2} pt -> {3}" -f $i, $page.Size.Width, $page.Size.Height, $outPath)
    $page.Dispose()
}
