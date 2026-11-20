# Render pages of a PDF to PNG using the Windows built-in PDF renderer (Windows.Data.Pdf).
# No install needed. Usage (from PowerShell 5.1):
#   . ([scriptblock]::Create((Get-Content -Raw 'render_pdf.ps1')))
#   Render-PdfPages -Pdf 'C:\full\path\book.pdf' -First 1 -Last 5 -OutDir 'C:\out' -Prefix 'ch3' -Width 1500
# Pages are 1-based PDF pages. Output files: <Prefix>-<NN>.png

function Render-PdfPages {
  param(
    [Parameter(Mandatory = $true)][string]$Pdf,
    [Parameter(Mandatory = $true)][int]$First,
    [Parameter(Mandatory = $true)][int]$Last,
    [Parameter(Mandatory = $true)][string]$OutDir,
    [string]$Prefix = 'p',
    [int]$Width = 1500
  )
  $ErrorActionPreference = 'Stop'
  Add-Type -AssemblyName System.Runtime.WindowsRuntime
  [void][Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
  [void][Windows.Data.Pdf.PdfDocument, Windows.Data.Pdf, ContentType = WindowsRuntime]
  [void][Windows.Data.Pdf.PdfPageRenderOptions, Windows.Data.Pdf, ContentType = WindowsRuntime]
  [void][Windows.Storage.Streams.InMemoryRandomAccessStream, Windows.Storage.Streams, ContentType = WindowsRuntime]
  [void][Windows.UI.Colors, Windows.UI, ContentType = WindowsRuntime]

  $asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
      $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
      $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]

  function Wait-Op($op, [Type]$type) {
    $t = $asTaskGeneric.MakeGenericMethod($type).Invoke($null, @($op))
    [void]$t.Wait(-1)
    return $t.Result
  }
  $asTaskAction = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
      $_.Name -eq 'AsTask' -and -not $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and
      $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncAction' })[0]
  function Wait-Action($act) {
    $t = $asTaskAction.Invoke($null, @($act))
    [void]$t.Wait(-1)
  }

  if (-not (Test-Path $OutDir)) { [void](New-Item -ItemType Directory -Force $OutDir) }
  $file = Wait-Op ([Windows.Storage.StorageFile]::GetFileFromPathAsync($Pdf)) ([Windows.Storage.StorageFile])
  $doc = Wait-Op ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])
  Write-Output ("PageCount: {0}" -f $doc.PageCount)
  for ($i = $First; $i -le $Last; $i++) {
    if ($i -lt 1 -or $i -gt $doc.PageCount) { Write-Output "skip $i (out of range)"; continue }
    $page = $doc.GetPage([uint32]($i - 1))
    $stream = New-Object Windows.Storage.Streams.InMemoryRandomAccessStream
    $opts = New-Object Windows.Data.Pdf.PdfPageRenderOptions
    $opts.DestinationWidth = [uint32]$Width
    $opts.BackgroundColor = [Windows.UI.Colors]::White
    Wait-Action ($page.RenderToStreamAsync($stream, $opts))
    $stream.Seek(0)
    $reader = [System.IO.WindowsRuntimeStreamExtensions]::AsStreamForRead($stream)
    $out = Join-Path $OutDir ('{0}-{1:D2}.png' -f $Prefix, $i)
    $fs = [System.IO.File]::Create($out)
    $reader.CopyTo($fs)
    $fs.Close(); $reader.Close(); $stream.Dispose(); $page.Dispose()
    Write-Output ("wrote {0}" -f $out)
  }
}
